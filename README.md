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
echo 8 > functions/hid.usb0/report_length

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

  5.3. Save and reboot the Rpi zero:
  
```
sudo reboot
```
  
