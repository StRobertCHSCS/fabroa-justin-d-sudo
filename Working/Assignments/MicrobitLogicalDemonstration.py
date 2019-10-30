from microbit import *

#identify the pins
crashsensor_pin = pin1
soilmoisturesensor_pin = pin3
miniservo_pin = pin8
greenLED_pin = pin12
redLED_pin = pin13

#other variables
healthwarning = false

#if else statements
while True: 
    if soilmoisturesensor_pin.read_analog (moisture > 50) and (moisture < 100):
        print("Your plant is good. Moisture level is %d" % soilmoisturesensor_pin.read_analog)
        greenLED_pin.write_digital(12)
        display.show(Image.HAPPY)
        
    else:
        print("Your plant needs water. Moisture level is %d" % soilmoisturesensor_pin.read_analog)
        redLED_pin.write_digital(13)
        while True:
            if crashsensor_pin.read_digital()== 0:
                servo.right_angle(180)
                crashsensor_pin.read_analog(1)
                display.show(Imaage.SAD)


