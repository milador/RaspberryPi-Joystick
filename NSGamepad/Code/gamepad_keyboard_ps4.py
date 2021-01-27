"""
Use a keyboard to control a PS4.

Remember to hit the PS4 LOGO button (keyboard key '0' ) to activate. The PS4
does not activate a controller until it sees the LOGO button press.
"""

import os
import sys
import termios
import time
from NSGamepad import *

Gamepad = NSGamepad()
Gamepad.begin('/dev/hidg0')

def getch():
    init()
    sleep_time = 0.050
    old_settings = termios.tcgetattr(0)
    new_settings = old_settings[:]
    new_settings[3] &= ~termios.ICANON

    try:
        termios.tcsetattr(0, termios.TCSANOW, new_settings)
        ch = sys.stdin.read(1)
        if ch == 'd':
            left_stick_right(sleep_time)
        elif ch == 'w':
            left_stick_up(sleep_time)
        elif ch == 'a':
            left_stick_left(sleep_time)
        elif ch == 's':
            left_stick_down(sleep_time)
        elif ch == '\'':
            right_stick_right(sleep_time)
        elif ch == 'p':
            right_stick_up(sleep_time)
        elif ch == 'l':
            right_stick_left(sleep_time)
        elif ch == ':':
            right_stick_down(sleep_time)
        elif ch == '1':
            button(DS4Button.CIRCLE, sleep_time)
        elif ch == '2':
            button(DS4Button.SQUARE, sleep_time)
        elif ch == '3':
            button(DS4Button.TRIANGLE, sleep_time)
        elif ch == '4':
            button(DS4Button.CROSS, sleep_time)
        elif ch == '5':
            button(DS4Button.L1, sleep_time)
        elif ch == '6':
            button(DS4Button.R1, sleep_time)
        elif ch == '7':
            button(DS4Button.L2, sleep_time)
        elif ch == '8':
            button(DS4Button.R2, sleep_time)
        elif ch == '9':
            button(DS4Button.OPTIONS, sleep_time)
        elif ch == '0':
            button(DS4Button.LOGO, sleep_time)
        elif ch == 'q':
            clean_up()
            sys.exit()
        else:
            clean_up()
        init()

    finally:
        termios.tcsetattr(0, termios.TCSANOW, old_settings)
    return ch

# Initialization
def init():
    clean_up()

def button(button, tf):
    Gamepad.press(button)
    time.sleep(tf)
    Gamepad.release(button)

def left_stick_right(tf):
    Gamepad.leftXAxis(255)
    time.sleep(tf)
    Gamepad.leftXAxis(128)

def left_stick_up(tf):
    Gamepad.leftYAxis(0)
    time.sleep(tf)
    Gamepad.leftYAxis(128)

def left_stick_left(tf):
    Gamepad.leftXAxis(0)
    time.sleep(tf)
    Gamepad.leftXAxis(128)

def left_stick_down(tf):
    Gamepad.leftYAxis(255)
    time.sleep(tf)
    Gamepad.leftYAxis(128)

def right_stick_right(tf):
    Gamepad.rightXAxis(255)
    time.sleep(tf)
    Gamepad.rightXAxis(128)

def right_stick_up(tf):
    Gamepad.rightYAxis(0)
    time.sleep(tf)
    Gamepad.rightYAxis(128)

def right_stick_left(tf):
    Gamepad.rightXAxis(0)
    time.sleep(tf)
    Gamepad.rightXAxis(128)

def right_stick_down(tf):
    Gamepad.rightYAxis(255)
    time.sleep(tf)
    Gamepad.rightYAxis(128)

def clean_up():
    Gamepad.releaseAll()
    Gamepad.leftXAxis(128)
    Gamepad.leftYAxis(128)
    Gamepad.rightXAxis(128)
    Gamepad.rightYAxis(128)
    Gamepad.dPad(DPad.CENTERED)

def main():
    Gamepad.begin('/dev/hidg0')

    while True:
        print("\nKey: '" + getch() + "'\n")

if __name__ == "__main__":
    main()

