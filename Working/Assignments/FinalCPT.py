from microbit import *

led_pin = pin0

while True:
    lightLevel = display.read_light_level()
    display.scroll(lightLevel)
    sleep(2000)
    if lightLevel > 100 and lightLevel < 2037:
        led_pin.write_digital(1)
    else:
        led_pin.write_digital(0)

