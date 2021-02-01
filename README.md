# RaspberryPi-Joystick
The goal of this project is to create a virtual USB HID joystick using Raspberry Pi. 

The new versions of raspberry pi zero W come with bluetooth chip which makes it possible to use Bluetooth HID devices as well as USB HID.

This project is in development process at the moment.

We now go over the hardware and software requirements.

# Hardware requirements  

  1. [Raspberry Pi zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) x 1
  2. Micro SD card x 1
  3. [Pi Zero USB Stem](https://www.sparkfun.com/products/14526) x 1
  4. mice and keyboard to setup (optional)
  
Note : You can also use an OTG adapter cable and a power supply through micro USB ports instead of Pi Zero USB Stem.

# Hardware Assembly Instructions   

  1. Solder the Pi Zero USB Stem
  
The main part of the assembly process is to solder the Pi Zero USB Stem to the Raspberry pi zero W. You can find the assembly instructions of Pi Zero USB Stem on [zerostem.io website](https://zerostem.io/installation/). 

Note: You can skip this step if you using an OTG adapter 

  2. Insert the flashed micro SD card with the latest version of Raspbian OS into micro SD card slot.
  
  3. Connect your raspberry pi zero to a monitor through HDMI cable and a mice and keyboard. This step is required to install the necessary code and make Rpi act as a virtual joystick device. You can also use SSH and skip this step. 
  
# Software installation instructions   

The software for this project is offered in three flavors and you can select the version that matches your needs.

  1. [8_Buttons README.md](https://github.com/milador/RaspberryPi-Joystick/blob/master/8_Buttons_Joystick/README.md) ( 8 Buttons and a dual axis joystick )
  2. [16_Buttons README.md](https://github.com/milador/RaspberryPi-Joystick/blob/master/16_Buttons_Joystick/README.md) ( 16 Buttons and a dual axis joystick )
  3. [32_Buttons README.md](https://github.com/milador/RaspberryPi-Joystick/blob/master/32_Buttons_Joystick/README.md) ( 32 Buttons and a dual axis joystick )
  4. [Nintendo_Switch README.md](https://github.com/milador/RaspberryPi-Joystick/blob/master/NSGamepad/README.md) ( Nintendo Switch & PS4 )
  
Please select the opention based on your need and follow the instructions.

# Usage

You can find sample python codes for each version of joysticks which can be used to test functionality of RaspberryPi Joystick. The sample codes can be modified and used in your own projects.

  
  
