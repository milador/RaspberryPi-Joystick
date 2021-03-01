"""
Test Joystick_16 class by pressing and releasing all buttons then moving
the joystick in all directions.
"""

import time
from Joystick_16 import *

def main():
    """ test Joystick_16 class """

    joystick = Joystick_16()
    joystick.begin('/dev/hidg0')

    while True:
        # Press and hold every button
        for button in range(0, 16):
            joystick.press(button)
            time.sleep(0.1)
        time.sleep(1)
        # Release all buttons
        joystick.releaseAll()
        time.sleep(1)
        # Press all buttons at the same time
        joystick.buttons(0xffff)
        time.sleep(1)
        # Release all buttons
        joystick.releaseAll()
        time.sleep(1)

        # Move the stick clockwise
        stick = [
            {"x":   0, "y":   0},
            {"x":   0, "y": -127},
            {"x": 127, "y": -127},
            {"x": 127, "y":   0},
            {"x": 127, "y": 127},
            {"x":   0, "y": 127},
            {"x":-127, "y": 127},
            {"x":-127, "y":   0},
            {"x":-127, "y":-127},
            {"x":   0, "y":   0},
        ]
        for direction in range(0, 10):
            joystick.xAxis(stick[direction]['x'])
            joystick.yAxis(stick[direction]['y'])
            time.sleep(0.5)

if __name__ == "__main__":
    main()
