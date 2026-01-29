def config():
    from esp import osdebug
    from micropython import const, alloc_emergency_exception_buf as aeeb
    from gc import collect
    from machine import freq
    
    freq(160_000_000)
    osdebug(None)
    aeeb(100)
    collect()
    
    _HOST = const(1)
    _MISO = const(-1)
    _FREQ = const(40_000_000)

    _CS   = const(0)
    _BLK  = const(-1)
    _DC   = const(1)
    _RST  = const(2)
    _MOSI = const(3)
    _SCK  = const(4)
    
    from machine import SPI
    from lcd_bus import SPIBus
    spi_bus = SPI.Bus(host=_HOST, mosi=_MOSI, miso=_MISO, sck=_SCK)
    dsp_bus = SPIBus(spi_bus=spi_bus, dc=_DC, cs=_CS, freq=_FREQ)
    
    import st7735
    import lvgl as lv
    display = st7735.ST7735(
        data_bus=dsp_bus,
        display_width=128,
        display_height=160,
        reset_pin=_RST,
        reset_state=st7735.STATE_LOW,
        color_space=lv.COLOR_FORMAT.RGB565,
        color_byte_order=st7735.BYTE_ORDER_RGB,
        rgb565_byte_swap=True)
    display.init(2)
    
    display.set_rotation(lv.DISPLAY_ROTATION._180)
    
    from task_handler import TaskHandler
    th = TaskHandler()
    
    del lv
    return display

display = config()