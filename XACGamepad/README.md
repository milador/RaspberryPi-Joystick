# Linux USB XAC GamePad Gadget Installation Instructions 
  
# Software requirements  

  1. Install latest version of Raspbian OS on an SD card according to the official documents on [raspberrypi.org](https://www.raspberrypi.org/documentation/installation/installing-images/).
  
 # Software installation 
 
1.	Download Dependencies

  1.1. Startup the raspberrypi zero W
  
  1.2. Open the command line
  
  1.3. Install the required packages
```
sudo apt-get update
sudo apt full-upgrade
sudo apt-get install python3-evdev python3-gpiozero python-dev python-pip git
```

  1.4. Install the optional packages
```
sudo apt-get install vim ctags screen build-essential
```

2.	Reboot RaspberryPi
```
sudo reboot
```

3.	Verify the kernel version ( Tested : Linux btgadget 5.10.11+ #1399 Thu Jan 28 12:02:28 GMT 2021 armv6l GNU/Linux )
```
uname -a
```

4.	Set up USB gadget mode

  4.1. Download source code and necessary scripts
  
```
git clone https://github.com/milador/RaspberryPi-Joystick
cd RaspberryPi-Joystick/XACGamepad
```

  4.2. Enable libcomposite and other necessary modules and drivers

```
sudo echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
sudo echo "dwc2" | sudo tee -a /etc/modules
sudo echo "libcomposite" | sudo tee -a /etc/modules
```

  4.3. Make changes to Linux USB gadget HID driver module for the Xbox Adaptive Controller
```
KERNEL_RELEASE=`uname -r`
sudo cp /lib/modules/${KERNEL_RELEASE}/kernel/drivers/usb/gadget/function/usb_f_hid.ko /lib/modules/${KERNEL_RELEASE}/kernel/drivers/usb/gadget/function/usb_f_hid.ko.orig
sudo cp ./Drivers/rpi-5.10/usb_f_hid.ko /lib/modules/${KERNEL_RELEASE}/kernel/drivers/usb/gadget/function/
```

5.	Create the virtual joystick HID config script

```
sudo touch /usr/bin/xacgamepad_usb
sudo chmod +x /usr/bin/xacgamepad_usb
```

6.	Add virtual joystick HID config script to startup scripts and run it automatically after OS boot

  6.1. Open /etc/rc.local
  
```
sudo nano /etc/rc.local
```
  6.2. Add following command on the line above "exit 0" and save it. ( Add it on the line before "exit 0" )
  
```
/usr/bin/xacgamepad_usb # Raspberry XAC GamePad joystick libcomposite configuration
```

7.	Create the joystick HID gadget 

  7.1. Create a new gadget

```
sudo nano /usr/bin/xacgamepad_usb
```

  7.2. Add the following code to the xacgamepad_usb gadget and save it.
  
```
# Created by https://github.com/milador/RaspberryPi-Joystick
#!/bin/bash

sleep 30

# Create XAC Gamepad gadget
cd /sys/kernel/config/usb_gadget/
mkdir -p xacgamepad
cd xacgamepad

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
echo "RaspberryPi XAC Gamepad" > strings/0x409/product


# Define the functions of the device
mkdir functions/hid.usb0
echo 0 > functions/hid.usb0/protocol
echo 0 > functions/hid.usb0/subclass
echo 3 > functions/hid.usb0/report_length

# Write report descriptor ( X and Y analog joysticks plus 8 buttons for XAC)
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

The report descriptor is created to define a dual axis joystick and 8 buttons joystick HID device for XAC. The report descriptor used in the xacgamepad_usb gadget definition is presented in hexadecimal values as follows:

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

8. Save and reboot the Rpi zero:
  
```
sudo reboot
```
  
9. Connect your Rpi zero to your computer and make sure it recognizes your Rpi zero as a USB HID joystick device named "RaspberryPi Joystick". Wait at least 30 seconds for Raspberry Pi to emulate as a HID Joystick device. Windows will initially say the USB Device is not recognized but detects it as a joystick in 30 seconds. 

  
10.  Startup your Rpi zero and enter following commands to test the configuration:
   
```
sudo /usr/bin/xacgamepad_usb
ls -la /dev/hidg*
```   

You should get something similar to following which means it's working and ready to use.

```
crw------- 1 root root 243, 0 Dec 26 02:34 /dev/hidg0
```   

9.  Windows 10 detects Raspberry Pi joystick as a USB HID device and you can use find it under Control Panel\Hardware and Sound\Devices and Printers.

<p align="center">
<img align="center" src="https://raw.githubusercontent.com/milador/RaspberryPi-Joystick/master/Resources/rpi_xac_cpanel.png" width="50%" height="50%" alt="raspberry pi XAC joystick device in cpanel"/>
</p>

<p align="center">
<img align="center" src="https://raw.githubusercontent.com/milador/RaspberryPi-Joystick/master/Resources/rpi_xacgamepad_properties.PNG" width="50%" height="50%" alt="raspberry pi 8 buttons XAC joystick properties"/>
</p>

# Data packets

The data sent to the host device for the 8 buttons and dual axis joystick configuration of the joystick contains 3 bytes, 2 are for the XY and 1 are the buttons. The first two bytes are for dual axis joystick(X,Y) and the other byte of the data is for 8 buttons.

<p align="center">
<img align="center" src="https://raw.githubusercontent.com/milador/RaspberryPi-Joystick/master/Resources/rpi_xac_packets.png" width="50%" height="50%" alt="raspberry pi XAC joystick 8 buttons data packets"/>
</p>

# Testing

1.  gamepad_xac_keyboard.py: A sample code to convert keyboard actions to joystick actions using command line and a keyboard is available to test the functionality. This method has packets exposed which is not recommended for usage. 

  1.1. Change the path to Code sub-directory ( You can skip 1.2 to 1.6 )

```
cd RaspberryPi-Joystick/XACGamepad/Code
```  
  
  1.2. Download the 8 buttons XAC keyboard input interface code: [gamepad_xac_keyboard.py](https://github.com/milador/RaspberryPi-Joystick/blob/master/XACGamepad/Code/gamepad_xac_keyboard.py)

  1.3. Create a new python file using following command:
  
```
sudo nano gamepad_xac_keyboard.py
sudo chmod +x gamepad_xac_keyboard.py
```   

  1.4. Copy and paste the gamepad_xac_keyboard.py code available under Code directory.

  1.5. Save gamepad_xac_keyboard.py file and exit
  
  1.6. Test operating RaspberryPi-Joystick using xac_keyboard.py code with a physical keyboard or SSH
  
```
sudo python gamepad_xac_keyboard.py
```   

  1.7. Usage:


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
* Key q: Exit


2.  Gamepad_XAC.py: A class created to handle button actions and dual axis joystick actions.

3.  gamepad_xac_demo.py: A sample code that automatically press buttons and move joystick

  3.1. Change the path to Code sub-directory

  3.2. Start running the python script
  
```
sudo python gamepad_xac_demo.py
```   


# Usage

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

  1.4. Change the path to Code sub-directory 

```
cd RaspberryPi-Joystick/XACGamepad/Code
```  

  1.5. Test the gamepad_xac_inputevent python script
  
```
sudo python3 gamepad_xac_inputevent.py
```   
  1.6. Connect RaspberryPi to one of the USB ports on XAC. Make sure you use an external power source to power both XAC and RPi Zero. Wait 30 seconds for it to initialize.
  
  1.7. That's it! You should now be able to use your BT keyboard/mouse to operate your XAC.
  
  
 # Autostart
 
 We go over process to make the gamepad_xac_inputevent.py start automatically on boot 

1.  Create xacgamepad service
```
sudo nano /etc/systemd/system/xacgamepad.service
```   

2.  Add following script to xacgamepad.service and save it

```
[Unit]
Description=XAC Gamepad automatic start with systemd, respawn, after bluetooth
After=bluetooth.target
After=multi-user.target
Requires=bluetooth.target

[Service]
ExecStart=/usr/bin/python3 -u gamepad_xac_inputevent.py
WorkingDirectory=/home/pi/RaspberryPi-Joystick/XACGamepad/Code
Type=idle
Restart=always
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=xacgamepad
User=pi
Group=pi

[Install]
WantedBy=multi-user.target
```   

3.  Create a rule to give permission for execution of python code and accessing input devices 

```
sudo nano /etc/udev/rules.d/rpidevice.rules
```   

4.  Add rules to give permission for execution of python code and accessing input devices to rpidevice.rules and save it.

```
KERNEL=="hidg0", NAME="%k", GROUP="pi", MODE="0666"
KERNELS=="input*", MODE="0666" GROUP="plugdev"
```   

5.  Enable and start the xacgamepad.service

```
systemctl daemon-reload
systemctl enable xacgamepad.service
systemctl start xacgamepad.service
```   
Use following to check status of running service :

```
systemctl status xacgamepad.service
```   

6.  Perform reboot

```
sudo reboot
```   
