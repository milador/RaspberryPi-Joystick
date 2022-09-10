# File name: joystick_16_buttons_keyboard.py 
# Created by https://github.com/milador/RaspberryPi-Joystick
# Author: Milad Hajihassan
# Date created: 14/2/2021
# Python Version: 1.0

import os
import sys
import fcntl  
import termios
import time
import random
from Joystick_16 import *
from importlib import reload
reload(sys)

joystick = Joystick_16()
joystick.begin('/dev/hidg0')
		
def getch():
  import sys, tty, termios
  init()
  sleep_time = 0.050
  old_settings = termios.tcgetattr(0)
  new_settings = old_settings[:]
  new_settings[3] &= ~termios.ICANON

  try:
    termios.tcsetattr(0, termios.TCSANOW, new_settings)
    ch = sys.stdin.read(1)
    if (ch == 'd'):
        button_right(sleep_time)
    elif ch == 'w':
        button_up(sleep_time)
    elif ch == 'a':
        button_left(sleep_time)
    elif ch == 's':
        button_down(sleep_time)
    elif ch == '1':
        button_1(sleep_time)
    elif ch == '2':
        button_2(sleep_time)
    elif ch == '3':
        button_3(sleep_time)
    elif ch == '4':
        button_4(sleep_time)
    elif ch == '5':
        button_5(sleep_time)
    elif ch == '6':
        button_6(sleep_time)
    elif ch == '7':
        button_7(sleep_time)
    elif ch == '8':
        button_8(sleep_time)
    elif ch == '9':
        button_9(sleep_time)
    elif ch == 'r':
        button_10(sleep_time)
    elif ch == 't':
        button_11(sleep_time)
    elif ch == 'y':
        button_12(sleep_time)
    elif ch == 'u':
        button_13(sleep_time)
    elif ch == 'i':
        button_14(sleep_time)
    elif ch == 'o':
        button_15(sleep_time)
    elif ch == 'p':
        button_16(sleep_time)
    elif ch == 'q':
        clean_up() 
        sys.exit()
    else:
        clean_up()
    pass
    init()
      
  finally:
    termios.tcsetattr(0, termios.TCSANOW, old_settings)
  return ch
	
# Initialization 
def init():
    clean_up()

def button_1(tf):
    joystick.press(0)
    time.sleep(tf)
    clean_up()	
	
def button_2(tf):
    joystick.press(1)
    time.sleep(tf)
    clean_up()	
	
def button_3(tf):
    joystick.press(2)
    time.sleep(tf)
    clean_up()	
	
def button_4(tf):
    joystick.press(3)
    time.sleep(tf)
    clean_up()	
	
def button_5(tf):
    joystick.press(4)
    time.sleep(tf)
    clean_up()	
	
def button_6(tf):
    joystick.press(5)
    time.sleep(tf)
    clean_up()	
	
def button_7(tf):
    joystick.press(6)
    time.sleep(tf)
    clean_up()	
	
def button_8(tf):
    joystick.press(7)
    time.sleep(tf)
    clean_up()	

def button_9(tf):
    joystick.press(8)
    time.sleep(tf)
    clean_up()	
	
def button_10(tf):
    joystick.press(9)
    time.sleep(tf)
    clean_up()	
	
def button_11(tf):
    joystick.press(10)
    time.sleep(tf)
    clean_up()	
	
def button_12(tf):
    joystick.press(11)
    time.sleep(tf)
    clean_up()	
	
def button_13(tf):
    joystick.press(12)
    time.sleep(tf)
    clean_up()	
	
def button_14(tf):
    joystick.press(13)
    time.sleep(tf)
    clean_up()	
	
def button_15(tf):
    joystick.press(14)
    time.sleep(tf)
    clean_up()	
	
def button_16(tf):
    joystick.press(15)
    time.sleep(tf)
    clean_up()	
	
def button_right(tf):
    joystick.xAxis(127)
    joystick.yAxis(0)
    time.sleep(tf)
    clean_up()	
	
def button_up(tf):
    joystick.xAxis(0)
    joystick.yAxis(-127)
    time.sleep(tf)
    clean_up()	
	
def button_left(tf):
    joystick.xAxis(-127)
    joystick.yAxis(0)
    time.sleep(tf)
    clean_up()	
	
def button_down(tf):
    joystick.xAxis(0)
    joystick.yAxis(127)
    time.sleep(tf)
    clean_up()	
	
def clean_up():
    joystick.releaseAll()
    joystick.xAxis(0)
    joystick.yAxis(0)


def main():
    
    while True:
        print("\nKey: '" + getch() + "'\n")




if __name__ == "__main__":
    main()

