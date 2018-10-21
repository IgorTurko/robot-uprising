#!/usr/bin/env python3

from __future__ import absolute_import
from roberta.ev3 import Hal
from roberta.BlocklyMethods import BlocklyMethods
from ev3dev import ev3 as ev3dev
import math
import traceback

class BreakOutOfALoop(Exception): pass
class ContinueLoop(Exception): pass

_brickConfiguration = {
    'wheel-diameter': 5.6,
    'track-width': 18.0,
    'actors': {
        'B':Hal.makeLargeMotor(ev3dev.OUTPUT_A, 'on', 'foreward', 'right'),
        'C':Hal.makeLargeMotor(ev3dev.OUTPUT_D, 'on', 'foreward', 'left'),
    },
    'sensors': {
        '3':Hal.makeColorSensor(ev3dev.INPUT_1),
        '4':Hal.makeUltrasonicSensor(ev3dev.INPUT_4),
    },
}
hal = Hal(_brickConfiguration)

right = True
angle = 5
def run():
    global angle, right
    while True:
        while (hal.getUltraSonicSensorDistance('4') <= 6):
            hal.rotateDirectionAngle('C', 'B', False, 'left', 10, 5)
        print(hal.getUltraSonicSensorDistance('4'))
        # later we need to add hal.getColorSensorColour('3') == 'red'
        if hal.getColorSensorColour('3') == 'white':
            hal.driveDistance('C', 'B', False, 'foreward', 15, 2)
            angle = 5
        else:
            if right:
                hal.rotateDirectionAngle('C', 'B', False, 'left', 15, angle)
            else:
                hal.rotateDirectionAngle('C', 'B', False, 'right', 15, angle)
            right = not right
            angle = angle + 5

def main():
    try:
        run()
    except Exception:
        traceback.print_exc()

if __name__ == "__main__":
    main()