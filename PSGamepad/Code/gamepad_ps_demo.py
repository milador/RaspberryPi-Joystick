"""
Demonstrate use of the PSGamepad class. psgamepad_usb must be run first to
create the USB gadget.


Must be run as root like this:
$ sudo ./ps_gamepad_usb
$ cd Code
$ sudo python3 gamepad_ps_demo.py
"""
import time
from MFGamepad import *

def main():
    """ test PSGamepad class """

    gamepad = MFGamepad()
    gamepad.begin('/dev/hidg0')

    while True:
        # Press and hold every button 0..13
        for button in range(0, 14):
            gamepad.press(button)
            time.sleep(0.1)
        time.sleep(1)
        # Release all buttons
        gamepad.releaseAll()
        time.sleep(1)
        # Press all 14 buttons at the same time
        gamepad.buttons(0x3fff)
        time.sleep(1)
        # Release all buttons
        gamepad.releaseAll()
        time.sleep(1)
        # Move directional pad in all directions
        # 0 = North, 1 = North-East, 2 = East, etc.
        for direction in range(0, 8):
            gamepad.dPad(direction)
            time.sleep(0.5)
        # Move directional pad to center
        gamepad.dPad(DPad.CENTERED)

        # Move the left stick then right stick
        stick = [
            {"x": 128, "y": 128},
            {"x": 128, "y": 0},
            {"x": 255, "y": 0},
            {"x": 255, "y": 128},
            {"x": 255, "y": 255},
            {"x": 128, "y": 255},
            {"x":   0, "y": 255},
            {"x":   0, "y": 128},
            {"x":   0, "y":   0},
            {"x": 128, "y": 128},
        ]
        for direction in range(0, 10):
            gamepad.leftXAxis(stick[direction]['x'])
            gamepad.leftYAxis(stick[direction]['y'])
            time.sleep(0.5)
        for direction in range(0, 10):
            gamepad.rightXAxis(stick[direction]['x'])
            gamepad.rightYAxis(stick[direction]['y'])
            time.sleep(0.5)

if __name__ == "__main__":
    main()
