#!/usr/bin/python3
"""
Interface to Linux USB NSGamepad Gadget

MIT License

Copyright (c) 2021 gdsports625@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from struct import pack
import array
import threading
from enum import IntEnum

# Direction pad names
class DPad(IntEnum):
    """DPad direction names"""
    CENTERED = 0xF
    UP = 0
    UP_RIGHT = 1
    RIGHT = 2
    DOWN_RIGHT = 3
    DOWN = 4
    DOWN_LEFT = 5
    LEFT = 6
    UP_LEFT = 7

# Button names
class NSButton(IntEnum):
    """NSButton names based on Nintendo Switch buttons"""
    Y = 0
    B = 1
    A = 2
    X = 3
    LEFT_TRIGGER = 4
    RIGHT_TRIGGER = 5
    LEFT_THROTTLE = 6
    RIGHT_THROTTLE = 7
    MINUS = 8
    PLUS = 9
    LEFT_STICK = 10
    RIGHT_STICK = 11
    HOME = 12
    CAPTURE = 13

class DS4Button(IntEnum):
    """Button names based on Dual Shock 4 PS4 buttons"""
    SQUARE = 0
    CROSS = 1
    CIRCLE = 2
    TRIANGLE = 3
    L1 = 4
    R1 = 5
    L2 = 6
    R2 = 7
    SHARE = 8
    OPTIONS = 9
    L3 = 10
    R3 = 11
    LOGO = 12
    TPAD = 13

class NSGamepad():
    """NSGamepad Linux USB Gadget Interface"""
    # pylint: disable=too-many-instance-attributes
    compass_dir_x = array.array('B', \
            [0, 0, 128, 255, 255, 255, 128, 0, \
            128, 128, 128, 128, 128, 128, 128, 128, 128])
    compass_dir_y = array.array('B', \
            [128, 255, 255, 255, 128, 0, 0, 0,\
            128, 128, 128, 128, 128, 128, 128, 128, 128])

    def __init__(self):
        self.thread_lock = threading.Lock()
        self.left_x_axis = 128
        self.left_y_axis = 128
        self.right_x_axis = 128
        self.right_y_axis = 128
        self.my_buttons = 0
        self.d_pad = DPad.CENTERED
        self.dpad_x_axis = 128
        self.dpad_y_axis = 128

    def begin(self, devname):
        """Start NSGamepad"""
        with self.thread_lock:
            self.devhandle = open(devname, 'wb+')
            self.left_x_axis = 128
            self.left_y_axis = 128
            self.right_x_axis = 128
            self.right_y_axis = 128
            self.my_buttons = 0
            self.d_pad = DPad.CENTERED
            self.dpad_x_axis = 128
            self.dpad_y_axis = 128
            self.write()
        return

    def end(self):
        """End NSGamepad"""
        self.devhandle.close()
        return

    def write(self):
        """Send NSGamepad state"""
        self.devhandle.write(pack('<HBBBBBB',
            self.my_buttons, self.d_pad,
            self.left_x_axis, self.left_y_axis, \
            self.right_x_axis, self.right_y_axis, 0))
        self.devhandle.flush()
        return

    def press(self, button_number):
        """Press button 0..13"""
        with self.thread_lock:
            self.my_buttons |= (1<<button_number)
            self.write()
        return

    def release(self, button_number):
        """Release button 0..13"""
        with self.thread_lock:
            self.my_buttons &= ~(1<<button_number)
            self.write()
        return

    def releaseAll(self):
        """Release all buttons"""
        with self.thread_lock:
            self.my_buttons = 0
            self.write()
        return

    def buttons(self, buttons):
        """Set all buttons 0..13"""
        with self.thread_lock:
            self.my_buttons = buttons
            self.write()
        return

    def leftXAxis(self, position):
        """Move left stick X axis 0..128..255"""
        with self.thread_lock:
            self.left_x_axis = position
            self.write()
        return

    def leftYAxis(self, position):
        """Move left stick Y axis 0..128..255"""
        with self.thread_lock:
            self.left_y_axis = position
            self.write()
        return

    def rightXAxis(self, position):
        """Move right stick X axis 0..128..255"""
        with self.thread_lock:
            self.right_x_axis = position
            self.write()
        return

    def rightYAxis(self, position):
        """Move right stick Y axis 0..128..255"""
        with self.thread_lock:
            self.right_y_axis = position
            self.write()
        return

    def map_dpad_xy(self, x, y):
        """Return direction pad number given axes x,y"""
        if x == 128:
            if y == 128:
                return DPad.CENTERED   # Center
            elif y < 128:
                return 0    # North
            return 4        # South
        elif x < 128:
            if y == 128:
                return 6    # West
            elif y < 128:
                return 7    # North West
            return 5        # South West
        else:
            if y == 128:
                return 2    # East
            elif y < 128:
                return 1    # North East
            return 3        # South East

    def dPadXAxis(self, position):
        """Move right stick X axis 0..128..255"""
        if (position < 0 or position > 255):
            position = 128
        with self.thread_lock:
            self.dpad_x_axis = position
            self.d_pad = self.map_dpad_xy(self.dpad_x_axis, self.dpad_y_axis)
            self.write()
        return

    def dPadYAxis(self, position):
        """Move right stick Y axis 0..128..255"""
        if (position < 0 or position > 255):
            position = 128
        with self.thread_lock:
            self.dpad_y_axis = position
            self.d_pad = self.map_dpad_xy(self.dpad_x_axis, self.dpad_y_axis)
            self.write()
        return

    def dPad(self, position):
        """Move directional pad (0..7, 15)"""
        if position < 0 or position > 7:
            position = DPad.CENTERED
        with self.thread_lock:
            self.d_pad = position
            self.dpad_x_axis = self.compass_dir_x[position]
            self.dpad_y_axis = self.compass_dir_y[position]
            self.write()
        return

def main():
    """ test NSGamepad class """
    import time

    gamepad = NSGamepad()
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
