from microbit import *

# identify the pins
Crashensor_pin = pin1
moisturesensor_pin = pin3
servo_pin = pin8
LEDgreen_pin = pin12
LEDred_pin = pin13

#other variables
healthwarning = False 

#if else statements
while True: 
    if moisturesensor_pin.read_analog() >50 and moisturesensor_pin.read_analog() <75:
        print("Your plant is good. Moisture level is %d" % moisturesensor_pin.read_analog)
        LEDgreen_pin.write_digital(12)
        crashsensor_pin.read_analog(0)

    elif crashsensor_pin.read_digital()== 1:
        servo.right_angle(180)
        
    else:
        print("Your plant needs water. Moisture level is %d" % moisturesensor_pin.read_analog)
        LEDred_pin.write_digital(13)
                


