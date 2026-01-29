def display_init():
    from gc import collect
    collect()

    from micropython import const, alloc_emergency_exception_buf as aeeb
    aeeb(100)

    from machine import freq
    freq(240_000_000)
    
    from esp import osdebug
    osdebug(None)

    _DSP_HOST = const(1)
    _DSP_MOSI = const(13)
    _DSP_MISO = const(12)
    _DSP_SCK  = const(14)
    _DSP_DC   = const(2)
    _DSP_BLK  = const(21)
    _DSP_CS   = const(15)
    _DSP_FREQ = const(24_000_000)
    
    _TCH_MOSI = const(32)
    _TCH_MISO = const(39)
    _TCH_SCK  = const(25)
    _TCH_CS   = const(33)
    _TCH_IRQ  = const(36)
    _TCH_FREQ = const(2_000_000)
    
    _SDC_HOST = const(2)
    _SDC_MOSI = const(23)
    _SDC_MISO = const(19)
    _SDC_SCK  = const(18)
    _SDC_CS   = const(5)
    _SDC_FREQ = const(10_000_000)

    from machine import SoftSPI, SPI, SDCard
    dsp_spi = SPI.Bus(host=_DSP_HOST, mosi=_DSP_MOSI, miso=_DSP_MISO, sck=_DSP_SCK)
    tch_spi = SoftSPI(baudrate=_TCH_FREQ, mosi=_TCH_MOSI, miso=_TCH_MISO, sck=_TCH_SCK)
    sdc_spi = SPI.Bus(host=_SDC_HOST, mosi=_SDC_MOSI, miso=_SDC_MISO, sck=_SDC_SCK)
    
    from lcd_bus import SPIBus
    dsp_bus = SPIBus(spi_bus=dsp_spi, dc=_DSP_DC, cs=_DSP_CS, freq=_DSP_FREQ)
    
    try:
        from os import mount, listdir
        sd = SDCard(spi_bus=sdc_spi, cs=_SDC_CS, freq=_SDC_FREQ)
        mount(sd, '/sd')
        print('SDCard Mounted')
        print(listdir('/sd'))
    except Exception as e:
        print(f'SDCard Error: {e}')
    
    import ili9341
    display = ili9341.ILI9341(
        data_bus = dsp_bus,
        display_width  = 240,
        display_height = 320,
        backlight_pin  = _DSP_BLK,
        backlight_on_state = ili9341.STATE_PWM,
        color_space = lv.COLOR_FORMAT.RGB565,
        color_byte_order = ili9341.BYTE_ORDER_BGR,
        rgb565_byte_swap = True)
    display.init(1)
    
    from machine import Pin
    from xpt2046 import XPT2046
    indev = XPT2046(tch_spi)
    Pin(_TCH_CS, Pin.OUT, value=False)
    if indev.is_calibrated:
        display.set_backlight(100)
        indev.enable_input_priority()
        # indev.calibrate()
        indev._cal.mirrorX = True
        indev._cal.mirrorY = True
        indev._cal.alphaX  = -1.153846
        indev._cal.betaX   = 0.005417118
        indev._cal.deltaX  = 257.5298
        indev._cal.alphaY  = 0.0
        indev._cal.betaY   = 1.220657
        indev._cal.deltaY  = -20.04695
        indev._cal.save()
    display.set_rotation(lv.DISPLAY_ROTATION._270)
    
    from task_handler import TaskHandler
    th = TaskHandler()
    
    from time import sleep
    for i in range(1, 101):
        display.set_backlight(i)
        sleep(0.02)
        
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