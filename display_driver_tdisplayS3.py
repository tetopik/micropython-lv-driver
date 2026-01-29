import lvgl as lv

def display_init():
    from esp import osdebug
    osdebug(None)

    from micropython import const, alloc_emergency_exception_buf as aeeb
    aeeb(100)

    from machine import freq
    freq(240_000_000)

    from gc import collect
    collect()
    
    _WIDTH = const(170)
    _HEIGHT = const(320)
    _PWR = const(15)
    _BL = const(38)
    _RST = const(5)
    _DC = const(7)
    _WR = const(8)
    _CS = const(6)
    _FREQ = const(20_000_000)
    _DATA0 = const(39)
    _DATA1 = const(40)
    _DATA2 = const(41)
    _DATA3 = const(42)
    _DATA4 = const(45)
    _DATA5 = const(46)
    _DATA6 = const(47)
    _DATA7 = const(48)

    from lcd_bus import I80Bus
    display_bus = I80Bus(
        dc=_DC,
        wr=_WR,
        cs=_CS,
        freq=_FREQ,
        data0=_DATA0,
        data1=_DATA1,
        data2=_DATA2,
        data3=_DATA3,
        data4=_DATA4,
        data5=_DATA5,
        data6=_DATA6,
        data7=_DATA7)

    from machine import Pin
    Pin(9, Pin.OUT, value=True) # RD

    from st7789 import ST7789, STATE_PWM, STATE_HIGH, STATE_LOW, BYTE_ORDER_RGB
    display = ST7789(
        data_bus=display_bus,
        display_width=_WIDTH,
        display_height=_HEIGHT,
        backlight_pin=_BL,
        backlight_on_state=STATE_PWM,
        power_pin=_PWR,
        power_on_state=STATE_HIGH,
        reset_pin=_RST,
        reset_state=STATE_LOW,
        color_space=lv.COLOR_FORMAT.RGB888,
        offset_y=35,
        color_byte_order=BYTE_ORDER_RGB)
    
    display.set_power(True)
    display.init()
    display.set_rotation(lv.DISPLAY_ROTATION._270)
    display.set_backlight(75)
    
    scrn = lv.screen_active()
    # scrn.set_style_bg_color(lv.color_hex(0x8BDCEB), 0) #CYAN
    scrn.set_style_bg_color(lv.color_hex(0xFFFF00), 0) #YELLOW

    from task_handler import TaskHandler
    th = TaskHandler(duration=20)
    
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