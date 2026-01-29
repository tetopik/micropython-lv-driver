import lvgl as lv

def display_init():
    from micropython import const, alloc_emergency_exception_buf as aeeb
    from gc import collect
    from esp import osdebug
    from machine import freq
    
    osdebug(None)
    freq(160_000_000)
    aeeb(100)
    collect()

    DC   = const(11)
    CS   = const(10)
    SCK  = const(12)
    MOSI = const(13)
    MISO = const(-1)
    BLK  = const(14)
    RST  = const(1)
    
    from machine import SPI
    from lcd_bus import SPIBus
    spi_bus = SPI.Bus(host=1, mosi=MOSI, miso=MISO, sck=SCK)
    dsp_bus = SPIBus(spi_bus=spi_bus, dc=DC, cs=CS, freq=80_000_000)
    
    from st7789 import ST7789, STATE_LOW, STATE_PWM, BYTE_ORDER_BGR
    display = ST7789(
        data_bus=dsp_bus,
        display_width=170,
        display_height=320,
        reset_pin=RST,
        reset_state=STATE_LOW,
        backlight_pin=BLK,
        backlight_on_state=STATE_PWM,
        offset_x=0,
        offset_y=35,
        color_space=lv.COLOR_FORMAT.RGB565,
        color_byte_order=BYTE_ORDER_BGR,
        rgb565_byte_swap=True)
    
    display.init()
    display.set_rotation(lv.DISPLAY_ROTATION._270)
    display.set_backlight(50)
    
    scrn = lv.screen_active()
    # scrn.set_style_bg_color(lv.color_hex(0x8BDCEB), 0) #CYAN
    scrn.set_style_bg_color(lv.color_hex(0xFFFF00), 0) #YELLOW
    
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