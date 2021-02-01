# Linux USB Gadget NSGamepad Installation Instructions 

# Software requirements  

  1. Install latest version of Raspbian OS on an SD card according to the official documents on [raspberrypi.org](https://www.raspberrypi.org/documentation/installation/installing-images/).
  
 # Software installation 
 
1.	Download Dependencies

  1.1. Startup the raspberrypi zero W
  
  1.2. Open the command line
  
  1.3. Install the necessary packages
```
sudo apt-get update
sudo apt-get install build-essential python-dev python-pip git
```

2.	Enable libcomposite and other necessary modules and drivers

```
sudo echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
sudo echo "dwc2" | sudo tee -a /etc/modules
sudo echo "libcomposite" | sudo tee -a /etc/modules
```

3.	Create the virtual joystick HID config script

```
sudo touch /usr/bin/nsgamepad_usb
sudo chmod +x /usr/bin/nsgamepad_usb
```

4.	Add virtual joystick HID config script to startup scripts and run it automatically after OS boot

  4.1. Open /etc/rc.local
  
```
sudo nano /etc/rc.local
```
  4.2. Add following command on the line above "exit 0" and save it. ( Add it on the line before "exit 0" )
  
```
/usr/bin/nsgamepad_usb # Raspberry NS Gamepad libcomposite configuration
```

5.	Create the NS Gamepad HID gadget 

  5.1. Create a new gadget

```
sudo nano /usr/bin/nsgamepad_usb
```

  5.2. Add the following code to the nsgamepad_usb gadget and save it.
  
```
# Created by https://github.com/milador/RaspberryPi-Joystick
#!/bin/bash
# This must run as root!
# This creates a generic gamepad with 2 sticks, 1 dpad, and 14 buttons.

sleep 30

# Create nsgamepad gadget
cd /sys/kernel/config/usb_gadget/
mkdir -p nsgamepad
cd nsgamepad

# Define USB specification
echo 0x1d6b > idVendor # Linux Foundation
echo 0x0104 > idProduct # Gamepad
echo 0x0100 > bcdDevice # v1.0.0
echo 0x0101 > bcdUSB # USB2
echo 0x00 > bDeviceClass
echo 0x00 > bDeviceSubClass
echo 0x00 > bDeviceProtocol

# Perform localization
mkdir -p strings/0x409

echo "Raspberry Pi" > strings/0x409/manufacturer
echo "NSGamepad" > strings/0x409/product

# Define the functions of the device
mkdir functions/hid.usb0
echo 0 > functions/hid.usb0/protocol
echo 0 > functions/hid.usb0/subclass
echo 8 > functions/hid.usb0/report_length

# Write report descriptor ( 2 analog sticks, 1 dpad, 14 buttons )
echo "05010905a10115002501350045017501950e05091901290e81029502810105012507463b017504950165140939814265009501810126ff0046ff000930093109320935750895048102750895018101c0" | xxd -r -ps > functions/hid.usb0/report_desc

# Create configuration file
mkdir configs/c.1
mkdir configs/c.1/strings/0x409

echo 0x80 > configs/c.1/bmAttributes
echo 100 > configs/c.1/MaxPower # 100 mA

# Link the configuration file
ln -s functions/hid.usb0 configs/c.1

# Activate device
ls /sys/class/udc > UDC

sleep 30
```

The report descriptor is created to define a generic gamepad with 2 sticks, 1 dpad, and 14 buttons HID device. The report descriptor used in the nsgamepad_usb gadget definition is presented in hexadecimal values as follows:

```
05010905a10115002501350045017501950e05091901290e81029502810105012507463b017504950165140939814265009501810126ff0046ff000930093109320935750895048102750895018101c0
```

The actual USB Report Descriptor can be defined as following:

```
0x05, 0x01,        // Usage Page (Generic Desktop Ctrls)
0x09, 0x05,        // Usage (Game Pad)
0xA1, 0x01,        // Collection (Application)
0x15, 0x00,        //   Logical Minimum (0)
0x25, 0x01,        //   Logical Maximum (1)
0x35, 0x00,        //   Physical Minimum (0)
0x45, 0x01,        //   Physical Maximum (1)
0x75, 0x01,        //   Report Size (1)
0x95, 0x0E,        //   Report Count (14)
0x05, 0x09,        //   Usage Page (Button)
0x19, 0x01,        //   Usage Minimum (0x01)
0x29, 0x0E,        //   Usage Maximum (0x0E)
0x81, 0x02,        //   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
0x95, 0x02,        //   Report Count (2)
0x81, 0x01,        //   Input (Const,Array,Abs,No Wrap,Linear,Preferred State,No Null Position)
0x05, 0x01,        //   Usage Page (Generic Desktop Ctrls)
0x25, 0x07,        //   Logical Maximum (7)
0x46, 0x3B, 0x01,  //   Physical Maximum (315)
0x75, 0x04,        //   Report Size (4)
0x95, 0x01,        //   Report Count (1)
0x65, 0x14,        //   Unit (System: English Rotation, Length: Centimeter)
0x09, 0x39,        //   Usage (Hat switch)
0x81, 0x42,        //   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,Null State)
0x65, 0x00,        //   Unit (None)
0x95, 0x01,        //   Report Count (1)
0x81, 0x01,        //   Input (Const,Array,Abs,No Wrap,Linear,Preferred State,No Null Position)
0x26, 0xFF, 0x00,  //   Logical Maximum (255)
0x46, 0xFF, 0x00,  //   Physical Maximum (255)
0x09, 0x30,        //   Usage (X)
0x09, 0x31,        //   Usage (Y)
0x09, 0x32,        //   Usage (Z)
0x09, 0x35,        //   Usage (Rz)
0x75, 0x08,        //   Report Size (8)
0x95, 0x04,        //   Report Count (4)
0x81, 0x02,        //   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
0x75, 0x08,        //   Report Size (8)
0x95, 0x01,        //   Report Count (1)
0x81, 0x01,        //   Input (Const,Array,Abs,No Wrap,Linear,Preferred State,No Null Position)
0xC0,              // End Collection

// 80 bytes

```

6. Save and reboot the Rpi zero:
  
```
sudo reboot
```
  
7. Connect your Rpi zero to your computer and make sure it recognizes your Rpi zero as a USB HID joystick device named "RaspberryPi Joystick". Wait at least 30 seconds for Raspberry Pi to emulate as a HID Joystick device. Windows will initially say the USB Device is not recognized but detects it as a joystick in 30 seconds. 

  
8.  Startup your Rpi zero and enter following commands to test the configuration:
   
```
sudo /usr/bin/nsgamepad_usb
ls -la /dev/hidg*
```   

You should get something similar to following which means it's working and ready to use.

```
crw------- 1 root root 243, 0 Dec 26 02:34 /dev/hidg0
```   

9.  Windows 10 detects Raspberry Pi joystick as a USB HID device and you can use find it under Control Panel\Hardware and Sound\Devices and Printers.

<p align="center">
<img align="center" src="https://raw.githubusercontent.com/milador/RaspberryPi-Joystick/master/Resources/rpi_joystick_cpanel.PNG" width="50%" height="50%" alt="raspberry pi joystick device in cpanel"/>
</p>

<p align="center">
<img align="center" src="https://raw.githubusercontent.com/milador/RaspberryPi-Joystick/master/Resources/rpi_nsgamepad_properties.PNG" width="50%" height="50%" alt="raspberry pi nsgamepad properties"/>
</p>

# Usage

The file nsgamepad_usb, based on 8_buttons_joystick_usb, configures the USB OTG
port as a gamepad with 2 analog sticks, 1 dpad, and 14 buttons. Be sure to run
it as root using sudo. Or set it up to auto run from /etc/rc.local. See the
docs for 8_joystick.

```
$ cd NSGamepad
$ sudo ./nsgamepad_usb
```

The class and test program are in Code/NSGamepad.py.

The class can be imported into another Python3 program like this.

```
from NSGamepad import *
```

To run the gamepad demo program do the following. The program presses and
releases all buttons then rotates the joysticks and dpad.

```
$ cd Code
$ sudo python3 gamepad_demo.py
```

## Nintendo Switch
To run the gamepad keyboard program for a Nintendo Switch do the following.

```
$ cd Code
$ sudo python3 gamepad_keyboard.py
```

The active keys for a Nintendo Switch are listed below

Key |Gamepad button
----|--------------
1   |A
2   |B
3   |X
4   |Y
5   |L
6   |R
7   |ZL
8   |ZR
9   |+
0   |-
W   |left stick up
A   |left stick left
S   |left stick down
D   |left stick right
P   |right stick up
L   |right stick left
;   |right stick down
'   |right stick right
Q   |quit program

To control a Nintendo Switch, use a Mayflash Magic NS adapter. Plug the
Zero into the Mayflash adapter then plug the Mayflash adapter into the Switch
dock. I suggest using the dock because the adapter and Zero may draw too much
current from the Switch battery if it is plugged directly into the Switch.
Configure the adapter to "Switch Pro" mode. The LED should be purple.

IMPORTANT: The Switch uses wireless communications even when a controller is
plugged in via USB. To change this start from the Home screen. Select
System Settings | Controllers and Sensors | Pro Controller Wired Communication.
Change it to ON.

## Playstation 4

To run the gamepad keyboard program for a Playstation 4 do the following.

```
$ cd Code
$ sudo python3 gamepad_keyboard_ps4.py
```

The active keys for a Playstation 4 are listed below

Key |Gamepad button
----|--------------
1   |CIRCLE
2   |SQUARE
3   |TRIANGLE
4   |CROSS
5   |L1
6   |R1
7   |L2
8   |R2
9   |OPTIONS
0   |LOGO
W   |left stick up
A   |left stick left
S   |left stick down
D   |left stick right
P   |right stick up
L   |right stick left
;   |right stick down
'   |right stick right
Q   |quit program

To control a Playstation 4, use a Mayflash Magic S Pro adapter. This adapter
supports PS4 and Nintendo Switch. Plug the Zero into the Mayflash adapter then
plug the Mayflash adapter into the PS4. Configure the adapter to "PS4" mode.
The LED should be blue.
