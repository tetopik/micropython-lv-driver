def config():
    from gc import collect
    collect()

    from micropython import const, alloc_emergency_exception_buf as aeeb
    aeeb(100)

    from machine import freq
    freq(240_000_000)

    HOST = const(1)
    MOSI = const(35)
    MISO = const(37)
    SCK  = const(36)
    DC   = const(38)
    CS1  = const(34) # Displ CS
    CS2  = const(33) # Touch CS
    FRQ1 = const(60_000_000) # Displ Freq
    FRQ2 = const(2_500_000)  # Touch Freq
    BLK  = const(39)
    
    import lvgl as lv
    from os import uname
    version = f'LVGL {lv.version_major()}.{lv.version_minor()}.{lv.version_patch()} on MPY {uname().release}'

    from machine import SPI
    spi_bus = SPI.Bus(host=HOST, mosi=MOSI, miso=MISO, sck=SCK)
    
    from lcd_bus import SPIBus as LCDBus
    dsp_bus = LCDBus(spi_bus=spi_bus, dc=DC, cs=CS1, freq=FRQ1)
    tch_bus = SPI.Device(spi_bus=spi_bus, freq=FRQ2, cs=CS2)
    
    from ili9341 import ILI9341 as Driver, STATE_PWM, BYTE_ORDER_BGR
    display = Driver(
        data_bus=dsp_bus,
        display_width=240,
        display_height=320,
        backlight_pin=BLK,
        backlight_on_state=STATE_PWM,
        color_space=lv.COLOR_FORMAT.RGB565,
        color_byte_order=BYTE_ORDER_BGR,
        rgb565_byte_swap=True)
    display.init(1)
    
    from xpt2046 import XPT2046
    indev = XPT2046(tch_bus)
    # indev.enable_input_priority()
    if not indev.is_calibrated:
        display.set_backlight(100)
        indev.calibrate()
        indev._cal.mirrorX = True
        indev._cal.mirrorY = True
        indev._cal.save()
    display.set_rotation(lv.DISPLAY_ROTATION._90)
    display.set_backlight(75)
    
    from task_handler import TaskHandler
    th = TaskHandler()
    
    return version, display, indev

version, display, indev = config()