# Linux USB Gadget 8 Buttons Installation Instructions 
  
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
sudo touch /usr/bin/8_buttons_rpi_joystick_usb
sudo chmod +x /usr/bin/8_buttons_rpi_joystick_usb
```

4.	Add virtual joystick HID config script to startup scripts and run it automatically after OS boot

  4.1. Open /etc/rc.local
  
```
sudo nano /etc/rc.local
```
  4.2. Add following command on the line above "exit 0" and save it. ( Add it on the line before "exit 0" )
  
```
/usr/bin/8_buttons_rpi_joystick_usb # Raspberry Joystick 8 button libcomposite configuration
```

5.	Create the joystick HID gadget 

  5.1. Create a new gadget

```
sudo nano /usr/bin/8_buttons_rpi_joystick_usb
```

  5.2. Add the following code to the 8_buttons_rpi_joystick_usb gadget and save it.
  
```
# Created by https://github.com/milador/RaspberryPi-Joystick
#!/bin/bash

sleep 30

# Create 8_buttons_rpi_joystick gadget
cd /sys/kernel/config/usb_gadget/
mkdir -p 8_buttons_rpi_joystick
cd 8_buttons_rpi_joystick

sudo su

# Define USB specification
echo 0x1d6b > idVendor # Linux Foundation
echo 0x0104 > idProduct # Multifunction Composite Joystick Gadget
echo 0x0100 > bcdDevice # v1.0.0
echo 0x0200 > bcdUSB # USB2
echo 0xEF > bDeviceClass
echo 0x02 > bDeviceSubClass
echo 0x01 > bDeviceProtocol

# Perform localization
mkdir -p strings/0x409

echo "0123456789" > strings/0x409/serialnumber
echo "Raspberry Pi" > strings/0x409/manufacturer
echo "RaspberryPi Joystick" > strings/0x409/product


# Define the functions of the device
mkdir functions/hid.usb0
echo 0 > functions/hid.usb0/protocol
echo 0 > functions/hid.usb0/subclass
echo 3 > functions/hid.usb0/report_length

# Write report descriptor ( X and Y analog joysticks plus 8 buttons )
echo "05010904A1011581257F0901A10009300931750895028102C005091901290815002501750195088102C0" | xxd -r -ps > functions/hid.usb0/report_desc

# Create configuration file
mkdir configs/c.1
mkdir configs/c.1/strings/0x409

echo 0x80 > configs/c.1/bmAttributes
echo 200 > configs/c.1/MaxPower # 200 mA
echo "RaspberryPi Joystick configuration" > configs/c.1/strings/0x409/configuration

# Link the configuration file
ln -s functions/hid.usb0 configs/c.1

# Activate device 
ls /sys/class/udc > UDC

sleep 10

```

The report descriptor is created to define a dual axis joystick and 8 buttons joystick HID device. The report descriptor used in the 8_buttons_rpi_joystick_usb gadget definition is presented in hexadecimal values as follows:

```
05010904A1011581257F0901A10009300931750895028102C005091901290815002501750195088102C0
```

The actual USB Report Descriptor can be defined as following:

```
0x05, 0x01,        // Usage Page (Generic Desktop Ctrls)
0x09, 0x04,        // Usage (Joystick)
0xA1, 0x01,        // Collection (Application)
0x15, 0x81,        //   Logical Minimum (-127)
0x25, 0x7F,        //   Logical Maximum (127)
0x09, 0x01,        //   Usage (Pointer)
0xA1, 0x00,        //   Collection (Physical)
0x09, 0x30,        //     Usage (X)
0x09, 0x31,        //     Usage (Y)
0x75, 0x08,        //     Report Size (8)
0x95, 0x02,        //     Report Count (2)
0x81, 0x02,        //     Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
0xC0,              //   End Collection
0x05, 0x09,        //   Usage Page (Button)
0x19, 0x01,        //   Usage Minimum (0x01)
0x29, 0x08,        //   Usage Maximum (0x08)
0x15, 0x00,        //   Logical Minimum (0)
0x25, 0x01,        //   Logical Maximum (1)
0x75, 0x01,        //   Report Size (1)
0x95, 0x08,        //   Report Count (8)
0x81, 0x02,        //   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
0xC0,              // End Collection

// 42 bytes
```

6. Save and reboot the Rpi zero:
  
```
sudo reboot
```
  
7. Connect your Rpi zero to your computer and make sure it recognizes your Rpi zero as a USB HID joystick device named "RaspberryPi Joystick". Wait at least 30 seconds for Raspberry Pi to emulate as a HID Joystick device. Windows will initially say the USB Device is not recognized but detects it as a joystick in 30 seconds. 

  
8.  Startup your Rpi zero and enter following commands to test the configuration:
   
```
sudo /usr/bin/8_buttons_rpi_joystick_usb
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
<img align="center" src="https://raw.githubusercontent.com/milador/RaspberryPi-Joystick/master/Resources/rpi_joystick_8_buttons_properties.PNG" width="50%" height="50%" alt="raspberry pi 8 buttons joystick properties"/>
</p>

# Data packets

The data sent to the host device for the 8 buttons and dual axis joystick configuration of the joystick contains 3 bytes, 2 are for the XY and 1 are the buttons. The first two bytes are for dual axis joystick(X,Y) and the other byte of the data is for 8 buttons.

<p align="center">
<img align="center" src="https://raw.githubusercontent.com/milador/RaspberryPi-Joystick/master/Resources/rpi_joystick_8_buttons_packets.png" width="50%" height="50%" alt="raspberry pi joystick 8 buttons data packets"/>
</p>

# Usage

A sample code to convert keyboard actions to joystick actions using command line and a keyboard is available to test the functionality.

1.  Download the 8 buttons keyboard input interface code: [8_buttons_keyboard.py](https://github.com/milador/RaspberryPi-Joystick/blob/master/8_Buttons_Joystick/Code/8_buttons_keyboard.py)

  1.1. Create a new python file using following command:
  
```
sudo nano 8_buttons_keyboard.py
sudo chmod +x 8_buttons_keyboard.py
```   

Note : Make sure you are in /home/pi directory 

  1.2. Copy and paste the 8_buttons_keyboard.py code available under Code directory.

  1.3. Save 8_buttons_keyboard.py file and exit
  
  1.4. Test operating RaspberryPi-Joystick using 8_buttons_keyboard.py code with a physical keyboard or SSH
  
```
sudo python 8_buttons_keyboard.py
```   

  1.5. Use "q" key to exit.

2.	Add 8_buttons_keyboard.py code to startup scripts and run it automatically after OS boot

  2.1. Open /etc/rc.local
  
```
sudo nano /etc/rc.local
```
  2.2. Add following command on the line above "exit 0" and save it. ( Add it on the line before "exit 0" )
  
```
sudo python 8_buttons_keyboard.py
```

3. 8_buttons_keyboard.py usage:

* Key 1: Button 1
* Key 2: Button 2
* Key 3: Button 3
* Key 4: Button 4
* Key 5: Button 5
* Key 6: Button 6
* Key 7: Button 7
* Key 8: Button 8
* Key d: Analog Right
* Key w: Analog Up
* Key a: Analog Left
* Key s: Analog Down

  
  
