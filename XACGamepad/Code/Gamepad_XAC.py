#!/usr/bin/python3
"""
Interface to Linux USB Gadget Gamepad Gadget

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
import threading

class Gamepad_XAC():
    """Joystick 8 buttons Linux USB Gadget Interface"""
    def __init__(self):
        self.thread_lock = threading.Lock()
        with self.thread_lock:
            self.devhandle = 0
            self.x_axis = 0
            self.y_axis = 0
            self.my_buttons = 0
        return

    def begin(self, devname):
        """Start Joystick_8"""
        with self.thread_lock:
            self.devhandle = open(devname, 'wb+')
            self.x_axis = 0
            self.y_axis = 0
            self.my_buttons = 0
            self.write()
        return

    def end(self):
        """End Joystick_8"""
        with self.thread_lock:
            self.devhandle.close()
            self.x_axis = 0
            self.y_axis = 0
            self.my_buttons = 0
            self.write()
        return

    def write(self):
        """Send Joystick_8 state"""
        self.devhandle.write(pack('<bbB',
            self.x_axis, self.y_axis, self.my_buttons))
        self.devhandle.flush()
        return

    def press(self, button_number):
        """Press button 0..7"""
        with self.thread_lock:
            self.my_buttons |= (1<<button_number)
            self.write()
        return

    def release(self, button_number):
        """Release button 0..7"""
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
        """Set all buttons 0..8"""
        with self.thread_lock:
            self.my_buttons = buttons
            self.write()
        return

    def xAxis(self, position):
        """Move left stick X axis -127..0..127"""
        with self.thread_lock:
            self.x_axis = position
            self.write()
        return

    def yAxis(self, position):
        """Move left stick Y axis -127..0..127"""
        with self.thread_lock:
            self.y_axis = position
            self.write()
        return

def main():
    """ test Gamepad_XAC class """
    import time

    joystick = Gamepad_XAC()
    joystick.begin('/dev/hidg0')

    while True:
        # Press and hold every button
        for button in range(0, 8):
            joystick.press(button)
            time.sleep(0.1)
        time.sleep(1)
        # Release all buttons
        joystick.releaseAll()
        time.sleep(1)
        # Press all buttons at the same time
        joystick.buttons(0xff)
        time.sleep(1)
        # Release all buttons
        joystick.releaseAll()
        time.sleep(1)

        # Move the stick
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
