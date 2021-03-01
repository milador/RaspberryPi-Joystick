# USB Gadget NSGamepad Installation Instructions 

# Hardware requirements  

## RaspberryPi Zero

  1. [Raspberry Pi zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) x 1
  2. Micro SD card x 1
  3. [Pi Zero USB Stem](https://www.sparkfun.com/products/14526) x 1
  4. [Mayflash Magic NS](https://www.amazon.com/Mayflash-Magic-NS-Wireless-Controller-Nintendo/dp/B079B5KHWQ) x 1
  5. USB B OTG adapter cable (For USB mice/keyboard usage) x 1
  6. [USB Female to Dual USB Male Extra Power Data Y Extension Cable](https://www.amazon.com/Black-Female-Extension-Mobile-CableCC/dp/B00ZUE6PVE/) (For USB mice/keyboard usage. Not needed with USB Stem) x 1
  7. mice and keyboard to setup (optional)
  8. [Mini Color PiTFT Ad Blocking Pi-Hole Kit](https://www.adafruit.com/product/4475) or [OLED Bonnet Pack for Raspberry Pi Zero](https://www.adafruit.com/product/3192) x 1 (optional)
  9. BT mice/keyboard or USB mice/keyboard as input 
    
## RaspberryPi 4

  1. [Raspberry Pi 4B](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/) x 1
  2. Micro SD card x 1
  3. [Mayflash Magic NS](https://www.amazon.com/Mayflash-Magic-NS-Wireless-Controller-Nintendo/dp/B079B5KHWQ) x 1
  4. USB C OTG adapter cable x 1
  5. [USB Female to Dual USB Male Extra Power Data Y Extension Cable](https://www.amazon.com/Black-Female-Extension-Mobile-CableCC/dp/B00ZUE6PVE/) x1
  6. mice and keyboard to setup (optional)
  7. [Adafruit Mini PiTFT 1.3" - 240x240 TFT Add-on for Raspberry Pi](https://www.adafruit.com/product/4484) x 1  (optional)
  8. BT mice/keyboard or USB mice/keyboard as input 


# Hardware Assembly Instructions   

  1. Connect USB cable/connection based on your hardware
  
  1.1. Rpi zero & zero w : Solder the Pi Zero USB Stem or use a USB B OTG adapter cable and Dual USB Male Extra Power Data Y Extension Cable (if you are using USB Keyboard/mice)
  
The main part of the assembly process is to solder the Pi Zero USB Stem to the Raspberry pi zero W. You can find the assembly instructions of Pi Zero USB Stem on [zerostem.io website](https://zerostem.io/installation/). 

Note: You can skip this step if you using an OTG adapter 

  1.2. Rpi 4 : USB C OTG adapter cable ( Use Dual USB Male Extra Power Data Y Extension Cable if you are using USB Keyboard/mice)

  2. Insert the flashed micro SD card with the latest version of Raspbian OS into micro SD card slot.
  
  3. Connect your raspberry pi to a monitor through HDMI cable and a mice and keyboard. This step is required to install the necessary code and make Rpi act as a virtual joystick device. You can also use SSH and skip this step. 
  
Note: Make sure the USB cable is connected to host before running the codes or you may get 108 error.
  
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

2.	Set up USB gadget mode

  2.1. Download source code and necessary scripts
  
```
git clone https://github.com/milador/RaspberryPi-Joystick
cd RaspberryPi-Joystick/NSGamepad
```

  3.2. Enable libcomposite and other necessary modules and drivers

```
sudo echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
sudo echo "dwc2" | sudo tee -a /etc/modules
sudo echo "libcomposite" | sudo tee -a /etc/modules
```

3.	Create the virtual joystick HID config script

```
sudo touch /usr/bin/ns_gamepad_usb
sudo chmod +x /usr/bin/ns_gamepad_usb
```

4.	Add virtual joystick HID config script to startup scripts and run it automatically after OS boot

  4.1. Open /etc/rc.local
  
```
sudo nano /etc/rc.local
```
  4.2. Add following command on the line above "exit 0" and save it. ( Add it on the line before "exit 0" )
  
```
/usr/bin/ns_gamepad_usb # Raspberry NSGamepad joystick libcomposite configuration
```

5.	Create the NS Gamepad HID gadget 

  5.1. Create a new gadget

```
sudo nano /usr/bin/ns_gamepad_usb
```

  5.2. Add the following code to the ns_gamepad_usb gadget and save it.
  
```
# Created by https://github.com/milador/RaspberryPi-Joystick
#!/bin/bash
# This must run as root!
# This creates a generic gamepad with 2 sticks, 1 dpad, and 14 buttons.

sleep 30

# Create ns_gamepad gadget
cd /sys/kernel/config/usb_gadget/
mkdir -p ns_gamepad
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

The report descriptor is created to define a generic gamepad with 2 sticks, 1 dpad, and 14 buttons HID device. The report descriptor used in the ns_gamepad_usb gadget definition is presented in hexadecimal values as follows:

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
sudo /usr/bin/ns_gamepad_usb
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

# Data packets

The data sent to the host device for the 14 buttons , 1 dpad, and dual axis joystick configuration of the joystick contains 6 bytes, 2 are for the XY and 4 are the buttons. 

<p align="center">
<img align="center" src="https://raw.githubusercontent.com/milador/RaspberryPi-Joystick/master/Resources/rpi_joystick_ns_packets.png" width="50%" height="50%" alt="raspberry pi NS Gamepad data packets"/>
</p>

# Testing

1.  gamepad_ns_keyboard.py: A sample code to convert keyboard actions to joystick actions using command line and a keyboard is available to test the functionality. This method has packets exposed which is not recommended for usage. 

  1.1. Change the path to Code sub-directory ( You can skip 1.2 to 1.6 )

```
cd RaspberryPi-Joystick/NSGamepad/Code
```  
  
  1.2. Download the NSGamepad keyboard input interface code: [gamepad_ns_keyboard.py](https://github.com/milador/RaspberryPi-Joystick/blob/master/NSGamepad/Code/gamepad_ns_keyboard.py)

  1.3. Create a new python file using following command:
  
```
sudo nano gamepad_ns_keyboard.py
sudo chmod +x gamepad_ns_keyboard.py
```   

  1.4. Copy and paste the gamepad_ns_keyboard.py code available under Code directory.

  1.5. Save gamepad_ns_keyboard.py file and exit
  
  1.6. Test operating RaspberryPi-Joystick using gamepad_ns_keyboard.py code with a physical keyboard or SSH
  
```
sudo python gamepad_ns_keyboard.py
```   


2.  NSGamepad.py: A class created to handle button actions,dpad and dual axis joystick actions.

3.  gamepad_ns_demo.py: A sample code that automatically press buttons and move joystick

  3.1. Change the path to Code sub-directory

  3.2. Start running the python script
  
```
sudo python gamepad_ns_demo.py
```   


# Usage Setup

Connect RaspberryPi to one of the USB ports on your host device. Make sure you use an external power source to power RPi Zero. Wait 30 seconds for it to initialize.


## Bluetooth

1.  Pair BT keyboard/mouse using RaspberryPi GUI taskbar.

  1.1. Click on Bluetooth button icon on top right of RaspberryPi GUI taskbar.
<p align="center">
<img align="center" src="https://raw.githubusercontent.com/milador/RaspberryPi-Joystick/master/Resources/rpi_bt_pair_open.PNG" width="50%" height="50%" alt="RaspberryPi GUI taskbar bluetooth menu"/>
</p>

  1.2. Click on Add Device
  
  1.3. Select your BT keyboard/mouse and Click on Pair button
<p align="center">
<img align="center" src="https://raw.githubusercontent.com/milador/RaspberryPi-Joystick/master/Resources/rpi_bt_pair_add.PNG" width="50%" height="50%" alt="BT keyboard/mouse scanning menu"/>
</p>



# Usage

The file ns_gamepad_usb, based on 8_buttons_joystick_usb, configures the USB OTG
port as a gamepad with 2 analog sticks, 1 dpad, and 14 buttons. Be sure to run
it as root using sudo. Or set it up to auto run from /etc/rc.local. See the
docs for 8_joystick.

```
$ cd NSGamepad
$ sudo ./ns_gamepad_usb
```

The class and test program are in Code/NSGamepad.py.

The class can be imported into another Python3 program like this.

```
from NSGamepad import *
```

To run the gamepad demo program do the following. The program presses and
releases all buttons then rotates the joysticks and dpad.

```
$ cd RaspberryPi-Joystick/NSGamepad/Code
$ sudo python3 gamepad_ns_demo.py
```

To test the gamepad_ns_inputevent python script run following command:
  
```
sudo python3 gamepad_ns_inputevent.py
```   

That's it! You should now be able to use your BT keyboard/mouse to operate as NSGamepad.
  


## Nintendo Switch
To run the gamepad keyboard program for a Nintendo Switch do the following.

```
$ cd Code
$ sudo python3 gamepad_ns_keyboard.py
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
$ sudo python3 gamepad_ns_keyboard_ps4.py
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
  
  
 # Autostart
 
 We go over process to make the gamepad_ns_inputevent.py start automatically on boot 

1.  Create ns_gamepad service
```
sudo nano /etc/systemd/system/ns_gamepad.service
```   

2.  Add following script to ns_gamepad.service and save it

```
[Unit]
Description=NS Gamepad automatic start with systemd, respawn, after bluetooth
After=bluetooth.target
After=multi-user.target
Requires=bluetooth.target

[Service]
ExecStart=/usr/bin/python3 -u gamepad_ns_inputevent.py
WorkingDirectory=/home/pi/RaspberryPi-Joystick/NSGamepad/Code
Type=idle
Restart=always
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=ns_gamepad
User=pi
Group=pi

[Install]
WantedBy=multi-user.target
```   

3.  Create a rule to give permission for execution of python code and accessing input devices 

```
sudo nano /etc/udev/rules.d/rpi_device.rules
```   

4.  Add rules to give permission for execution of python code and accessing input devices to rpi_device.rules and save it.

```
KERNEL=="hidg0", NAME="%k", GROUP="pi", MODE="0666"
KERNELS=="input*", MODE="0666" GROUP="plugdev"
```   

5.  Enable and start the ns_gamepad.service

```
systemctl daemon-reload
systemctl enable ns_gamepad.service
systemctl start ns_gamepad.service
```   
Use following to check status of running service :

```
systemctl status ns_gamepad.service
```   

6.  Perform reboot

```
sudo reboot
```   
