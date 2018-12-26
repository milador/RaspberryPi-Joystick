# XAC-Virtual-Joystick
The goal of this project is to create a virtual USB HID joystick using Raspberry Pi to operate XAC. 
XAC only accepts HID USB joystick devices and other sorts of USB HID devices can't be used to operate XAC.

However, we can use a raspberry pi to act as a HID converter device which makes it possible to use other devices such as USB Keyboard and mouse.

The new versions of raspberry pi ( Rpi 3 & Rpi zero w ) come with bluetooth chip which makes it possible to use Bluetooth HID devices as well as USB HID.

This project is in development process and it's only possible to operate XAC using a keyboard at the moment.

We now go over the hardware and software requirements.

# Hardware requirements  

  1. [Raspberry Pi zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) x 1
  2. Micro SD card x 1
  3. [Pi Zero USB Stem](https://www.sparkfun.com/products/14526) x 1
  4. mice and keyboard to setup (optional)
  
Note : You can also use an OTG adapter cable and a power supply through micro USB ports instead of Pi Zero USB Stem. A 3rd generation Raspberry pi 3 and Raspberry pi zero can be used as well.

# Hardware Assembly Instructions   

The main part of the assembly process is to solder the Pi Zero USB Stem to the Raspberry pi zero W. You can find the assembly instructions of Pi Zero USB Stem on [zerostem.io website](https://zerostem.io/installation/). 

Note: You can skip this step if you using an OTG adapter 
