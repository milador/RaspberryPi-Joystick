# USB Gadget 32 Buttons Installation Instructions 

# Hardware requirements  

## RaspberryPi Zero

  1. [Raspberry Pi zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) x 1
  2. Micro SD card x 1
  3. [Pi Zero USB Stem](https://www.sparkfun.com/products/14526) x 1
  4. OTG Micro USB B to USB A Female adapter (For USB mice/keyboard usage) x 1
  5. Micro USB B Male to USB A Male cable x 1
  6. Mice and keyboard to setup (optional)
  7. BT mice/keyboard or USB mice/keyboard as input 
  8. Power Supply
    
## RaspberryPi 4

  1. [Raspberry Pi 4B](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/) x 1
  2. Micro SD card x 1
  3. [USB C Male to USB C Female Data and Power Splitter](https://www.amazon.com/Splitter-Headphone-Charger-Pixel2XL-Note20Ultra/dp/B09BBFLD22/) x 1
  4. USB C Male to USB A Male cable x 1
  5. Mice and keyboard to setup (optional)
  6. BT mice/keyboard or USB mice/keyboard as input 
  7. Power Supply
  
## RaspberryPi 400

  1. [Raspberry Pi 400](https://www.raspberrypi.org/products/raspberry-pi-400/) x 1
  2. Micro SD card x 1
  3. [USB C Male to USB C Female Data and Power Splitter](https://www.amazon.com/Splitter-Headphone-Charger-Pixel2XL-Note20Ultra/dp/B09BBFLD22/) x 1
  4. USB C Male to USB A Male cable x 1
  5. Mice and keyboard to setup (optional)
  6. BT mice/keyboard or USB mice/keyboard as input 
  7. Power Supply

# Hardware Assembly Instructions   

## RaspberryPi Zero W

<p align="center">
<img align="center" src="../Resources/Images/PiZW_Setup_Diagram.png" width="50%" height="50%" alt="raspberry pi 0 W setup assembly"/>
</p>

### Option1 : 

  1. Solder the Pi Zero USB Stem . The main part of the assembly process is to solder the Pi Zero USB Stem to the Raspberry pi zero W. You can find the assembly instructions of Pi Zero USB Stem on [zerostem.io website](https://zerostem.io/installation/). 

  2. Insert the flashed micro SD card with the latest version of Raspbian OS into micro SD card slot.
  
  3. Connect an (OTG Micro USB B to USB A Female) adapter to the RaspberryPi Zero W through (Micro USB B) data port.
  
  4. Connect a mice and keyboard via (OTG Micro USB B to USB A Female) adapter. This step is required to install the necessary code and make Rpi act as a virtual joystick device. You can also use SSH and skip this step. 
  
  5. Connect your raspberry pi to a monitor through HDMI cable. You can also use SSH and skip this step. 

  6. Connect power supply through (Micro USB B) power port and power RaspberryPi Zero W.
  
  7. Connect RaspberryPi Zero W to your host device via Pi Zero USB Stem (USB A Male) port.
  
  
### Option2 : 
  
  1. Connect an (OTG Micro USB B to USB A Female) adapter to the RaspberryPi Zero W through (Micro USB B) data port.

  2. Insert the flashed micro SD card with the latest version of Raspbian OS into micro SD card slot.
  
  3. Connect a mice and keyboard via (OTG Micro USB B to USB A Female) adapter. This step is required to install the necessary code and make Rpi act as a virtual joystick device. You can also use SSH and skip this step. 
  
  4. Connect your raspberry pi to a monitor through HDMI cable. You can also use SSH and skip this step. 

  5. Connect power supply through (Micro USB B) port and power RaspberryPi Zero W.
  
  6. Perform the software setup and disconnect (OTG Micro USB B to USB A Female) adapter.
  
  7. Connect the (Micro USB B Male to USB A Male) cable to (Micro USB B) data port on RaspberryPi Zero W.
  
  8. Connect RaspberryPi Zero W to your host device via (Micro USB B Male to USB A Male) cable.
  
  
Note: Make sure the USB cable is connected to host device before running the codes or you may get 108 error.

  
## RaspberryPi 4 B

<p align="center">
<img align="center" src="../Resources/Images/Pi4_Setup_Diagram.png" width="50%" height="50%" alt="raspberry pi 4 B XAC setup assembly"/>
</p>
 
  1. Connect the (USB C Male to USB C Female Data and Power Splitter) cable to the (USB C Female) port of RaspberryPi 4 B.
  
  2. Connect the (USB C Male to USB A Male) cable to the (USB C Female) data port of (USB C Male to USB C Female Data and Power Splitter) cable.

  3. Insert the flashed micro SD card with the latest version of Raspbian OS into micro SD card slot.
  
  4. Connect a mice and keyboard via (USB A Female) ports on RaspberryPi 4 B. This step is required to install the necessary code and make Rpi act as a virtual joystick device. You can also use SSH and skip this step. 
  
  5. Connect your raspberry pi to a monitor through HDMI cable. You can also use SSH and skip this step. 

  6. Connect power supply to the (USB C Female) power port of (USB C Data and Power Splitter) cable.
  
  7. Perform the software setup.
  
  8. Connect the other end of (USB C Male to USB A Male) cable to the (USB A Female) port of your host device ( Example: Computer).
  
  
Note: Make sure the USB cable is connected to the host before running the codes or you may get 108 error.

## RaspberryPi 400

<p align="center">
<img align="center" src="../Resources/Images/Pi400_Setup_Diagram.png" width="50%" height="50%" alt="raspberry pi 400 XAC setup assembly"/>
</p>
 
  1. Connect the (USB C Male to USB C Female Data and Power Splitter) cable to the (USB C Female) port of RaspberryPi 400.
  
  2. Connect the (USB C Male to USB A Male) cable to the (USB C Female) data port of (USB C Male to USB C Female Data and Power Splitter) cable.
  
  3. Insert the flashed micro SD card with the latest version of Raspbian OS into micro SD card slot.
  
  4. Connect a mice and keyboard via (USB A Female) ports on RaspberryPi 400. This step is required to install the necessary code and make Rpi act as a virtual joystick device. You can also use SSH and skip this step. 
  
  5. Connect your raspberry pi to a monitor through HDMI cable. You can also use SSH and skip this step. 

  6. Connect power supply to the (USB C Female) power port of (USB C Data and Power Splitter) cable.
  
  7. Perform the software setup.
  
  8. Connect the other end of (USB C Male to USB A Male) cable to the (USB A Female) port of your host device ( Example: Computer).
  
Note: Make sure the USB cable is connected to the host before running the codes or you may get 108 error.
  
  
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
  1.4. Install the optional packages
```
sudo apt-get install vim ctags screen build-essential
```

2.	Set up USB gadget mode

  2.1. Download source code and necessary scripts
  
```
git clone https://github.com/milador/RaspberryPi-Joystick
cd RaspberryPi-Joystick/32_Buttons_Joystick
```

  3.2. Enable libcomposite and other necessary modules and drivers

```
sudo echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
sudo echo "dwc2" | sudo tee -a /etc/modules
sudo echo "libcomposite" | sudo tee -a /etc/modules
```

3.	Create the virtual joystick HID config script

```
sudo touch /usr/bin/32_buttons_rpi_joystick_usb
sudo chmod +x /usr/bin/32_buttons_rpi_joystick_usb
```

4.	Add virtual joystick HID config script to startup scripts and run it automatically after OS boot

  4.1. Open /etc/rc.local
  
```
sudo nano /etc/rc.local
```
  4.2. Add following command on the line above "exit 0" and save it. ( Add it on the line before "exit 0" )
  
```
/usr/bin/32_buttons_rpi_joystick_usb # Raspberry Joystick 32 button libcomposite configuration
```

5.	Create the joystick HID gadget 


```
sudo chmod +x 32_buttons_rpi_joystick_usb
sudo cp 32_buttons_rpi_joystick_usb /usr/bin/
```

The report descriptor is created to define a dual axis joystick and 32 buttons joystick HID device. The report descriptor used in the 32_buttons_rpi_joystick_usb gadget definition is presented in hexadecimal values as follows:

```
05010904A1011581257F0901A10009300931750895028102C0A10005091901292015002501750195208102C0C0
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
0xA1, 0x00,        //   Collection (Physical)
0x05, 0x09,        //     Usage Page (Button)
0x19, 0x01,        //     Usage Minimum (0x01)
0x29, 0x20,        //     Usage Maximum (0x20)
0x15, 0x00,        //     Logical Minimum (0)
0x25, 0x01,        //     Logical Maximum (1)
0x75, 0x01,        //     Report Size (1)
0x95, 0x20,        //     Report Count (32)
0x81, 0x02,        //     Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
0xC0,              //   End Collection
0xC0,              // End Collection

// 45 bytes
```

6. Save and reboot the Rpi zero:
  
```
sudo reboot
```
  
7. Connect your Rpi zero to your computer and make sure it recognizes your Rpi zero as a USB HID joystick device named "RaspberryPi Joystick". Wait at least 30 seconds for Raspberry Pi to emulate as a HID Joystick device. Windows will initially say the USB Device is not recognized but detects it as a joystick in 30 seconds. 

  
8.  Startup your Rpi zero and enter following commands to test the configuration:
   
```
sudo /usr/bin/32_buttons_rpi_joystick_usb
ls -la /dev/hidg*
```   

You should get something similar to following which means it's working and ready to use.

```
crw------- 1 root root 243, 0 Dec 26 02:34 /dev/hidg0
```   

9.  Windows 10 detects Raspberry Pi joystick as a USB HID device and you can use find it under Control Panel\Hardware and Sound\Devices and Printers.

<p align="center">
<img align="center" src="../Resources/Images/32Buttons_Cpanel.png" width="50%" height="50%" alt="raspberry pi joystick device in cpanel"/>
</p>

<p align="center">
<img align="center" src="../Resources/Images/32Buttons_Properties.png" width="50%" height="50%" alt="raspberry pi 32 buttons joystick properties"/>
</p>

# Data packets

The data sent to the host device for the 32 buttons and dual axis joystick configuration of the joystick contains 6 bytes, 2 are for the XY and 4 are the buttons. The first two bytes are for dual axis joystick(X,Y) and the other bytes of the data is for 32 buttons.

<p align="center">
<img align="center" src="../Resources/Images/32Buttons_Packets.png" width="50%" height="50%" alt="raspberry pi joystick 32 buttons data packets"/>
</p>

# Testing

1.  32_buttons_keyboard.py: A sample code to convert keyboard actions to joystick actions using command line and a keyboard is available to test the functionality. This method has packets exposed which is not recommended for usage. 

  1.1. Change the path to Code sub-directory ( You can skip 1.2 to 1.6 )

```
cd RaspberryPi-Joystick/32_Buttons_Joystick/Code
```  
  
  1.2. Download the 32 buttons keyboard input interface code: [joystick_32_buttons_keyboard.py](https://github.com/milador/RaspberryPi-Joystick/blob/master/32_Buttons_Joystick/Code/joystick_32_buttons_keyboard.py)

  1.3. Create a new python file using following command:
  
```
sudo nano joystick_32_buttons_keyboard.py
sudo chmod +x joystick_32_buttons_keyboard.py
```   

  1.4. Copy and paste the joystick_32_buttons_keyboard.py code available under Code directory.

  1.5. Save joystick_32_buttons_keyboard.py file and exit
  
  1.6. Test operating RaspberryPi-Joystick using joystick_32_buttons_keyboard.py code with a physical keyboard or SSH
  
```
sudo python joystick_32_buttons_keyboard.py
```   

  1.7. Usage:


* Key 1: Button 4
* Key 2: Button 8
* Key 3: Button 12
* Key 4: Button 16
* Key 5: Button 20
* Key 6: Button 24
* Key 7: Button 28
* Key 8: Button 32
* Key d: Analog Right
* Key w: Analog Up
* Key a: Analog Left
* Key s: Analog Down
* Key q: Exit


2.  Joystick_32.py: A class created to handle button actions and dual axis joystick actions.

3.  joystick_32_buttons_demo.py: A sample code that automatically press buttons and move joystick

  3.1. Change the path to Code sub-directory

  3.2. Start running the python script
  
```
sudo python joystick_32_buttons_demo.py
```   

# Usage Setup

Connect RaspberryPi to one of the USB ports on your host device. Make sure you use an external power source to power RPi Zero. Wait 30 seconds for it to initialize.


## Bluetooth

1.  Pair BT keyboard/mouse using RaspberryPi GUI taskbar.

  1.1. Click on Bluetooth button icon on top right of RaspberryPi GUI taskbar.
<p align="center">
<img align="center" src="../Resources/Images/BT_Pair_Open.PNG" width="50%" height="50%" alt="RaspberryPi GUI taskbar bluetooth menu"/>
</p>

  1.2. Click on Add Device
  
  1.3. Select your BT keyboard/mouse and Click on Pair button
<p align="center">
<img align="center" src="../Resources/Images/BT_Pair_Add.PNG" width="50%" height="50%" alt="BT keyboard/mouse scanning menu"/>
</p>

# Usage


1. Change the path to Code sub-directory 

```
cd RaspberryPi-Joystick/32_Buttons_Joystick/Code
```  

2. Test the joystick_32_buttons_inputevent python script
  
```
sudo python3 joystick_32_buttons_inputevent.py
```   
3. Connect RaspberryPi to one of the USB ports on your host device. Make sure you use an external power source to power RPi Zero. Wait 30 seconds for it to initialize.
  
4. That's it! You should now be able to use your BT keyboard/mouse to operate as 32 buttons joystick.
  
  
 # Autostart
 
 We go over process to make the joystick_32_buttons_inputevent.py start automatically on boot 

1.  Create 32_buttons_joystick service
```
sudo nano /etc/systemd/system/32_buttons_joystick.service
```   

2.  Add following script to 32_buttons_joystick.service and save it

```
[Unit]
Description=32 Button joystick automatic start with systemd, respawn, after bluetooth
After=bluetooth.target
After=multi-user.target
Requires=bluetooth.target

[Service]
ExecStart=/usr/bin/python3 -u joystick_32_buttons_inputevent.py
WorkingDirectory=/home/pi/RaspberryPi-Joystick/32_Buttons_Joystick/Code
Type=idle
Restart=always
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=32_buttons_joystick
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

5.  Enable and start the 32_buttons_joystick.service

```
systemctl daemon-reload
systemctl enable 32_buttons_joystick.service
systemctl start 32_buttons_joystick.service
```   
Use following to check status of running service :

```
systemctl status 32_buttons_joystick.service
```   

6.  Perform reboot

```
sudo reboot
```   
