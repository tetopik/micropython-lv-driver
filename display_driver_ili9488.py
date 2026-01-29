def display_init():
    from micropython import const, alloc_emergency_exception_buf as aeeb
    from gc import collect
    from esp import osdebug
    from machine import freq
    
    osdebug(None)
    freq(160_000_000)
    aeeb(100)
    collect()

    _SPI_HOST = const(1)
    _SPI_MOSI = const(6)
    _SPI_MISO = const(5)
    _SPI_SCK  = const(10)
    _DSP_DC   = const(3)
    _DSP_BLK  = const(2)
    _DSP_CS   = const(4)
    _TCH_CS   = const(7)
    _SDC_CS   = const(1)
    _DSP_FREQ = const(40_000_000)
    _TCH_FREQ = const(2_500_000)
    _SDC_FREQ = const(10_000_000)

    from machine import SPI, SDCard
    spi_bus = SPI.Bus(host=_SPI_HOST, mosi=_SPI_MOSI, miso=_SPI_MISO, sck=_SPI_SCK)
    
    from lcd_bus import SPIBus
    dsp_bus = SPIBus(spi_bus=spi_bus, dc=_DSP_DC, cs=_DSP_CS, freq=_DSP_FREQ)
    tch_bus = SPI.Device(spi_bus=spi_bus, freq=_TCH_FREQ, cs=_TCH_CS)
    
    import ili9488
    display = ili9488.ILI9488(
        data_bus=dsp_bus,
        display_width=320,
        display_height=480,
        backlight_pin=_DSP_BLK,
        backlight_on_state=ili9488.STATE_PWM,
        color_space=lv.COLOR_FORMAT.RGB888,
        color_byte_order=ili9488.BYTE_ORDER_RGB,
        rgb565_byte_swap=True)
    display.init()
    
    from xpt2046 import XPT2046
    indev = XPT2046(tch_bus)
    indev.enable_input_priority()
    if not indev.is_calibrated:
        # display.set_backlight(100)
        # indev.calibrate()
        indev._cal.mirrorX = False
        indev._cal.mirrorY = False
        indev._cal.alphaX  = 1.130645
        indev._cal.betaX   = 0.01209246
        indev._cal.deltaX  = -22.69894
        indev._cal.alphaY  = -0.01953398
        indev._cal.betaY   = -1.123204
        indev._cal.deltaY  = 514.9211
        indev._cal.save()
    display.set_rotation(lv.DISPLAY_ROTATION._90)
    
    scrn = lv.screen_active()
    scrn.set_style_bg_color(lv.color_hex(0x000000), 0)

    from task_handler import TaskHandler
    th = TaskHandler()
    
    from time import sleep
    for i in range(1, 101):
        display.set_backlight(i)
        sleep(0.02)
    
    try:
        from os import mount, listdir
        sd = SDCard(spi_bus=spi_bus, cs=_SDC_CS, freq=_SDC_FREQ)
        mount(sd, '/sd')
        print('SDCard Mounted')
        print(listdir('/sd'))
    except Exception as e:
        print(f'SDCard Error: {e}')
        
    return display, indev

def drive_letter():
    '''
    How to convert font files refer here: https://github.com/lvgl/lv_font_conv
    lv_font_conv --size 20 --format bin --bpp 1 --font Alibaba-PuHuiTi-Medium.subset.ttf --range 0x20-0x7f --no-compress -o font-PHT-en-20.bin

    font12 = lv.binfont_create(f'S:{path}/ui_font12.bin')

    with open(f'{path}/background.png', 'rb') as f: png_data = f.read()
    png_image_dsc = lv.image_dsc_t({
        'data_size': len(png_data),
        'data': png_data})
    '''
    
    from fs_driver import fs_register
    fs_drv = lv.fs_drv_t()
    fs_register(fs_drv, 'S')
    
    import sys
    sys.path.append('')
    try:
        path = __file__[:__file__.rfind('/')] if __file__.find('/') >= 0 else '.'
    except NameError:
        path = ''
    return path

import lvgl as lv
display, indev = display_init()
path = drive_letter()