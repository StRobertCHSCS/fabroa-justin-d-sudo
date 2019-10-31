#identify the pins
Crashensor_pin = pin1
moisturesensor_pin = pin3
servo_pin = pin8
LEDgreen_pin = pin12
LEDgreen_pin = pin13

#other variables
healthwarning = false

#if else statements
while True: 
    if moisturesensor_pin.read_analog (moisture > 50) and (moisture < 100):
        print("Your plant is good. Moisture level is %d" % moisturesensor_pin.read_analog)
        LEDgreen_pin.write_digital(12)
        display.show(Image.HAPPY)
        
    else:
        print("Your plant needs water. Moisture level is %d" % moisturesensor_pin.read_analog)
        LEDred_pin.write_digital(13)
        while True:
            if Crashsensor_pin.read_digital()== 0:
                servo.right_angle(180)
                Crashsensor_pin.read_analog(1)
                display.show(Imaage.SAD)


