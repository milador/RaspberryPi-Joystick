# RaspberryPi-Joystick

The goal of this project is to create a virtual USB HID joystick using Raspberry Pi. 

The new versions of raspberry pi zero W come with USB OTG and bluetooth chip which makes it possible to use Bluetooth HID devices as well as USB HID.

A RaspberryPi 4B can also be used instead of a Raspberry pi zero W.

This project is in development process at the moment.

We now go over the hardware and software requirements.

# Hardware requirements  

## RaspberryPi Zero

  1. [Raspberry Pi zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) x 1
  2. Micro SD card x 1
  3. [Pi Zero USB Stem](https://www.sparkfun.com/products/14526) x 1
  4. mice and keyboard to setup (optional)
  5. [Mini Color PiTFT Ad Blocking Pi-Hole Kit](https://www.adafruit.com/product/4475) or [OLED Bonnet Pack for Raspberry Pi Zero](https://www.adafruit.com/product/3192)  (optional)
  6. BT mice or keyboard for XAC 
  
Note : You can also use an OTG adapter cable and a power supply through micro USB ports instead of Pi Zero USB Stem.
  
## RaspberryPi 4

  1. [Raspberry Pi 4B](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/) x 1
  2. Micro SD card x 1
  3. USB C OTG adapter cable
  4. [USB Female to Dual USB Male Extra Power Data Y Extension Cable](https://www.amazon.com/Black-Female-Extension-Mobile-CableCC/dp/B00ZUE6PVE/)
  5. mice and keyboard to setup (optional)
  6. [Adafruit Mini PiTFT 1.3" - 240x240 TFT Add-on for Raspberry Pi](https://www.adafruit.com/product/4484)  (optional)
  7. BT mice or keyboard for XAC   


# Hardware Assembly Instructions   

  1. Solder the Pi Zero USB Stem
  
The main part of the assembly process is to solder the Pi Zero USB Stem to the Raspberry pi zero W. You can find the assembly instructions of Pi Zero USB Stem on [zerostem.io website](https://zerostem.io/installation/). 

Note: You can skip this step if you using an OTG adapter 

  2. Insert the flashed micro SD card with the latest version of Raspbian OS into micro SD card slot.
  
  3. Connect your raspberry pi zero to a monitor through HDMI cable and a mice and keyboard. This step is required to install the necessary code and make Rpi act as a virtual joystick device. You can also use SSH and skip this step. 
  
# Software installation instructions   

The software for this project is offered in three flavors and you can select the version that matches your needs.

  1. [8_Buttons](https://github.com/milador/RaspberryPi-Joystick/blob/master/8_Buttons_Joystick/) ( 8 Buttons and a dual axis joystick )
  2. [16_Buttons](https://github.com/milador/RaspberryPi-Joystick/blob/master/16_Buttons_Joystick/) ( 16 Buttons and a dual axis joystick )
  3. [32_Buttons](https://github.com/milador/RaspberryPi-Joystick/blob/master/32_Buttons_Joystick/) ( 32 Buttons and a dual axis joystick )
  4. [NSGamepad](https://github.com/milador/RaspberryPi-Joystick/blob/master/NSGamepad/) ( Nintendo Switch & PS4 )
  5. [XACGamepad](https://github.com/milador/RaspberryPi-Joystick/blob/master/XACGamepad/) ( Xbox Adaptive Controller )
  
Please select the option based on your need and follow the instructions.

# Collaborators

Thanks to all the developers and testers helping to create this project. Special thanks to [gdsports](https://github.com/gdsports) for finding/fixing bugs and developing new features. 


# License

## Creative Commons Attribution-NonCommercial-ShareAlike (CC-BY-NC-SA)

Copyright (c) 2019 Milador

A creative commons license that bans commercial use and requires you to release any modified works under this license.

<p align="center">
<img align="center" src="https://raw.githubusercontent.com/milador/milador/master/Assets/IMG/Cc-by-nc-sa_license_icon.png" width="50%" height="50%" alt="CC-BY-NC-SA"/>
</p>

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License</a>.


  
  
