#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveSteering
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

# TODO: Add code here
# sound = Sound()
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   sound.speak(x)

# m = LargeMotor(OUTPUT_A)
# m.on_for_rotations(SpeedPercent(75), 5)

robot = MoveSteering(OUTPUT_A, OUTPUT_D)
rotateLeft = True

while True:
    if rotateLeft:
        robot.on_for_rotations(-10, SpeedPercent(25), 0.1)
    else:
        robot.on_for_rotations(10, SpeedPercent(25), 0.1)

    rotateLeft = not rotateLeft

# ts = TouchSensor(INPUT_1)
# leds = Leds()

# print("Press the touch sensor to change the LED color!")

# while True:
#     if ts.is_pressed:
#         sound.speak("Alexei")
#         leds.set_color("LEFT", "GREEN")
#         leds.set_color("RIGHT", "GREEN")
#     else:
#         sound.speak("Khaled")
#         leds.set_color("LEFT", "RED")
#         leds.set_color("RIGHT", "RED")