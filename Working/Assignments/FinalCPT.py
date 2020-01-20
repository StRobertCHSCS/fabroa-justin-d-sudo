from microbit import *

led_ping = pin0
led_pinr = pin1
ADKeypad_pin = pin2
i = 1

while True:
    #button C
    if ADKeypad_pin.read_analog() > 90 and ADKeypad_pin.read_analog() < 100:
        i = 1
    #button B
    if ADKeypad_pin.read_analog() > 45 and ADKeypad_pin.read_analog() < 55:
        led_ping.write_digital(0)
        i = 3
    #button A
    if ADKeypad_pin.read_analog() > 0 and ADKeypad_pin.read_analog() < 10:
        led_ping.write_digital(1)
        i = 2
    while i == 2:
        lightLevel = display.read_light_level()
        if lightLevel > 10 and lightLevel < 2037:
            led_pinr.write_digital(0)
        else:
            led_pinr.write_digital(1)
        if ADKeypad_pin.read_analog() > 45 and ADKeypad_pin.read_analog() < 55:
            i=3
            led_ping.write_digital(0)
        if ADKeypad_pin.read_analog() > 90 and ADKeypad_pin.read_analog() < 100:
            led_pinr.write_digital(0)
            i=1
    while i == 1:
        lightLevel = display.read_light_level()
    # display.scroll(lightLevel)
        if lightLevel > 10 and lightLevel < 2037:
            led_ping.write_digital(1)
        else:
            led_ping.write_digital(0)
        # buttonA
        if ADKeypad_pin.read_analog() > 0 and ADKeypad_pin.read_analog() < 10:
            led_ping.write_digital(1)
            i = 0
        break
        # buttonB
        if ADKeypad_pin.read_analog() > 45 and ADKeypad_pin.read_analog() < 55:
            led_ping.write_digital(0)
            i = 0
        break
    while i == 3:
        lightLevel = display.read_light_level()
        if lightLevel > 10 and lightLevel < 2037:
            led_pinr.write_digital(1)
            led_ping.write_digital(0)
        else:
            led_pinr.write_digital(0)
        if ADKeypad_pin.read_analog() > 0 and ADKeypad_pin.read_analog() < 10:
            i=2
            led_pinr.write_digital(0)
        if ADKeypad_pin.read_analog() > 90 and ADKeypad_pin.read_analog() < 100:
            led_pinr.write_digital(0)
            i=1


