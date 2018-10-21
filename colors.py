#!/usr/bin/env python3

from roberta.ev3 import Hal
from roberta.BlocklyMethods import BlocklyMethods
from ev3dev import ev3 as ev3dev
import math
import traceback

_brickConfiguration = {
    'wheel-diameter': 5.6,
    'track-width': 18.0,
    'actors': {
        'RIGHT':Hal.makeLargeMotor(ev3dev.OUTPUT_A, 'on', 'foreward', 'right'),
        'LEFT':Hal.makeLargeMotor(ev3dev.OUTPUT_D, 'on', 'foreward', 'left'),
    },
    'sensors': {
        'color': Hal.makeColorSensor(ev3dev.INPUT_2),
#       'distance': Hal.makeUltrasonicSensor(ev3dev.INPUT_2),
        'touchLeft': Hal.makeTouchSensor(ev3dev.INPUT_4),
        'touchRight': Hal.makeTouchSensor(ev3dev.INPUT_1),
    },
}
hal = Hal(_brickConfiguration)

def rotate(direction):
    hal.rotateDirectionAngle('LEFT', 'RIGHT', False, direction, 20, 80)


angle = 5
right = False

def followTheTape():
    while True:
        if hal.getColorSensorColour('3') == 'white':
            hal.driveDistance('C', 'B', False, 'foreward', default_angle, 2)
            angle = 5
        else:
            if right:
                hal.rotateDirectionAngle('C', 'B', False, 'left', default_angle, angle)
            else:
                hal.rotateDirectionAngle('C', 'B', False, 'right', default_angle, angle)
        right = not right
        angle = angle + 5


def checkObstacles():
    if hal.isPressed('touchLeft') and hal.isPressed('touchRight'):
        print('both left and right pressed')
        hal.driveDistance('LEFT', 'RIGHT', False, 'backward', 30, 5)
        rotate('left')
    elif hal.isPressed('touchLeft'):
        print('left pressed')
        #hal.sayText('Ooops, going right')
        rotate('right')
    elif hal.isPressed('touchRight'):
        print('right pressed')
        #hal.sayText('Ooops, going left')
        rotate('left')

def checkTape():
    default_angle = 20
    steps = int(360 / default_angle)
    for i in range(steps):
        hal.rotateDirectionAngle('C', 'B', False, 'left', 15, default_angle * i)

        if hal.getColorSensorColour('3') == 'white':
            return True

    return False        

def checkBridge():
    if hal.getColorSensorColour('3') != 'black' or hal.getColorSensorColour('3') != 'white':
       searchForTape()

def run():
    # going among walls
    find_type_after_steps = 15
    loopNumber = 0
    while True:
        checkObstacles()
       
        hal.driveDistance('LEFT', 'RIGHT', False, 'forward', 30, 5)
        # TODO: check if we are ready to follow white tape

        if loopNumber % find_type_after_steps == 0 and checkTape():
            followTheTape() 
       
        ++loopNumber

def main():
    try:
        run()
    except Exception:
        traceback.print_exc()

if __name__ == "__main__":
    main()