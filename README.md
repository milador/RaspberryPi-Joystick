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
sudo touch /usr/bin/xac_joystick_usb
sudo chmod +x /usr/bin/xac_joystick_usb
```

4.	Add virtual joystick HID config script to startup scripts and run it automatically after OS boot

  4.1. Open /etc/rc.local
  
```
sudo nano /etc/rc.local
```
  4.2. Add following command on the line above "exit 0" and save it. ( Add it on the line before "exit 0" )
  
```
/usr/bin/xac_joystick_usb # XAC libcomposite configuration
```

5.	Create the joystick HID gadget 

  5.1. Create a new gadget

```
sudo nano /usr/bin/xac_joystick_usb
```

  5.2. Add the following code to the xac_joystick_usb gadget and save it.
  
```
# Created by https://github.com/milador/XAC-Virtual-Joystick
#!/bin/bash

sleep 10

# Create xac_joystick gadget
cd /sys/kernel/config/usb_gadget/
mkdir -p xac_joystick
cd xac_joystick

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
echo "XAC Virtual Joystick" > strings/0x409/product


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
echo "XAC configuration" > configs/c.1/strings/0x409/configuration

# Link the configuration file
ln -s functions/hid.usb0 configs/c.1

# Activate device 
ls /sys/class/udc > UDC

sleep 10

```

6. Save and reboot the Rpi zero:
  
```
sudo reboot
```
  
7. Connect your Rpi zero to your computer and make sure it recognizes your Rpi zero as a USB HID joystick device named "XAC Virtual Joystick".

<p align="center">
<img align="center" src="https://raw.githubusercontent.com/milador/XAC-Virtual-Joystick/master/Resources/cpanel.PNG" width="50%" height="50%" alt="Joystick device in cpanel"/>
</p>
  
8.  Startup your Rpi zero and enter following commands to test the configuration:
   
```
sudo /usr/bin/xac_joystick_usb
ls -la /dev/hidg*
```   

You should get something similar to following which means it's working and ready to use.

```
crw------- 1 root root 243, 0 Dec 26 02:34 /dev/hidg0
```   

# Usage

This ia a simple program to operate the virtual joystick using command line and a keyboard.

1.  Download the keyboard input interface code

  1.1. Create a new python file using following command:
  
```
sudo nano input_keyboard.py
sudo chmod +x input_keyboard.py
```   

Note : Make sure you are in /home/pi directory 

  1.2. Copy and paste the input_keyboard.py code available under Scripts directory.

  1.3. Save input_keyboard.py file and exit
  
  1.4. Test operating XAC using input_keyboard.py code with a physical keyboard or SSH
  
```
sudo python input_keyboard.py
```   

  1.5. Use "q" key to exit.

2.	Add input_keyboard.py code to startup scripts and run it automatically after OS boot

  2.1. Open /etc/rc.local
  
```
sudo nano /etc/rc.local
```
  2.2. Add following command on the line above "exit 0" and save it. ( Add it on the line before "exit 0" )
  
```
sudo python input_keyboard.py
```

3. input_keyboard.py usage:

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

  
  
