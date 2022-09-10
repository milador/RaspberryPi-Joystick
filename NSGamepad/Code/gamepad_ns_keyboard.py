import os
import sys
import termios
import time
from MFGamepad import *

Gamepad = MFGamepad()
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
            button(NSButton.A, sleep_time)
        elif ch == '2':
            button(NSButton.B, sleep_time)
        elif ch == '3':
            button(NSButton.X, sleep_time)
        elif ch == '4':
            button(NSButton.Y, sleep_time)
        elif ch == '5':
            button(NSButton.LEFT_TRIGGER, sleep_time)
        elif ch == '6':
            button(NSButton.RIGHT_TRIGGER, sleep_time)
        elif ch == '7':
            button(NSButton.LEFT_THROTTLE, sleep_time)
        elif ch == '8':
            button(NSButton.RIGHT_THROTTLE, sleep_time)
        elif ch == '9':
            button(NSButton.MINUS, sleep_time)
        elif ch == '0':
            button(NSButton.PLUS, sleep_time)
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

    while True:
        print("\nKey: '" + getch() + "'\n")

if __name__ == "__main__":
    main()

