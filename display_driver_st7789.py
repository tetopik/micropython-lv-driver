import lvgl as lv

def display_init():
    from esp import osdebug
    from micropython import const, alloc_emergency_exception_buf as aeeb
    from gc import collect
    from machine import freq
    
    freq(160_000_000)
    osdebug(None)
    aeeb(100)
    collect()
    
    _FREQ = const(40_000_000)
    
    _POLARITY = const(1)
    _PHASE    = const(0)
    _SPI_MODE = (_POLARITY << 1) | _PHASE
    
    _HOST = const(1)
    _MISO = const(-1)
    _CS   = const(-1)
    _BLK  = const(0)
    _DC   = const(1)
    _MOSI = const(2)
    _SCK  = const(3)
    
    from machine import SPI
    from lcd_bus import SPIBus
    spi_bus = SPI.Bus(host=_HOST, mosi=_MOSI, miso=_MISO, sck=_SCK)
    dsp_bus = SPIBus(spi_bus=spi_bus, spi_mode=_SPI_MODE, dc=_DC, cs=_CS, freq=_FREQ)
    
    import st7789
    display = st7789.ST7789(
        data_bus=dsp_bus,
        #display_width=135,
        display_width=240,
        display_height=240,
        #reset_pin=_RST,
        #reset_state=st7789.STATE_LOW,
        backlight_pin=_BLK,
        backlight_on_state=st7789.STATE_PWM,
        #offset_x=40,
        #offset_y=53,
        color_space=lv.COLOR_FORMAT.RGB565,
        color_byte_order=st7789.BYTE_ORDER_BGR,
        rgb565_byte_swap=True)
    display.init()
    
    display.set_rotation(lv.DISPLAY_ROTATION._0)
    display.set_backlight(50)
    
    scrn = lv.screen_active()
    scrn.set_style_bg_color(lv.color_hex(0x000000), 0)
    
    from task_handler import TaskHandler
    th = TaskHandler()
    
    return display

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

display = display_init()
path    = drive_letter()