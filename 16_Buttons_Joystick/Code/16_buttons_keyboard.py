# File name: 16_buttons_keyboard.py 
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
reload(sys)
sys.setdefaultencoding("ISO-8859-1")
		
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
        button_2(sleep_time)
    elif ch == '2':
        button_4(sleep_time)
    elif ch == '3':
        button_6(sleep_time)
    elif ch == '4':
        button_8(sleep_time)
    elif ch == '5':
        button_10(sleep_time)
    elif ch == '6':
        button_12(sleep_time)
    elif ch == '7':
        button_14(sleep_time)
    elif ch == '8':
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

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())
	
# Initialization 
def init():
    clean_up()

def button_1(tf):
    write_report('\x00\x00\x01\x00')
    time.sleep(tf)
    clean_up()	
	
def button_2(tf):
    write_report('\x00\x00\x02\x00')
    time.sleep(tf)
    clean_up()	
	
def button_3(tf):
    write_report('\x00\x00\x04\x00')
    time.sleep(tf)
    clean_up()	
	
def button_4(tf):
    write_report('\x00\x00\x08\x00')
    time.sleep(tf)
    clean_up()	
	
def button_5(tf):
    write_report('\x00\x00\x10\x00')
    time.sleep(tf)
    clean_up()	
	
def button_6(tf):
    write_report('\x00\x00\x20\x00')
    time.sleep(tf)
    clean_up()	
	
def button_7(tf):
    write_report('\x00\x00\x40\x00')
    time.sleep(tf)
    clean_up()	
	
def button_8(tf):
    write_report('\x00\x00\x80\x00')
    time.sleep(tf)
    clean_up()	

def button_9(tf):
    write_report('\x00\x00\x00\x01')
    time.sleep(tf)
    clean_up()	
	
def button_10(tf):
    write_report('\x00\x00\x00\x02')
    time.sleep(tf)
    clean_up()	
	
def button_11(tf):
    write_report('\x00\x00\x00\x04')
    time.sleep(tf)
    clean_up()	
	
def button_12(tf):
    write_report('\x00\x00\x00\x08')
    time.sleep(tf)
    clean_up()	
	
def button_13(tf):
    write_report('\x00\x00\x00\x10')
    time.sleep(tf)
    clean_up()	
	
def button_14(tf):
    write_report('\x00\x00\x00\x20')
    time.sleep(tf)
    clean_up()	
	
def button_15(tf):
    write_report('\x00\x00\x00\x40')
    time.sleep(tf)
    clean_up()	
	
def button_16(tf):
    write_report('\x00\x00\x00\x80')
    time.sleep(tf)
    clean_up()	
	
def button_right(tf):
    write_report('\x7F\x00\x00\x00')
    time.sleep(tf)
    clean_up()	
	
def button_up(tf):
    write_report('\x00\x7F\x00\x00')
    time.sleep(tf)
    clean_up()	
	
def button_left(tf):
    write_report('\x81\x00\x00\x00')
    time.sleep(tf)
    clean_up()	
	
def button_down(tf):
    write_report('\x00\x81\x00\x00')
    time.sleep(tf)
    clean_up()	
	
def clean_up():
    write_report('\x00\x00\x00\x00')


def main():
  
  while True:
        print("\nKey: '" + getch() + "'\n")




if __name__ == "__main__":
    main()

