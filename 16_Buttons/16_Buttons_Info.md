# 16 Buttons Software Installation Instructions 
  
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
sudo touch /usr/bin/16_buttons_rpi_joystick_usb
sudo chmod +x /usr/bin/16_buttons_rpi_joystick_usb
```

4.	Add virtual joystick HID config script to startup scripts and run it automatically after OS boot

  4.1. Open /etc/rc.local
  
```
sudo nano /etc/rc.local
```
  4.2. Add following command on the line above "exit 0" and save it. ( Add it on the line before "exit 0" )
  
```
/usr/bin/16_buttons_rpi_joystick_usb # Raspberry Joystick 8 button libcomposite configuration
```

5.	Create the joystick HID gadget 

  5.1. Create a new gadget

```
sudo nano /usr/bin/16_buttons_rpi_joystick_usb
```

  5.2. Add the following code to the 16_buttons_rpi_joystick_usb gadget and save it.
  
```
TBD

```

The report descriptor is created to define a dual axis joystick and 16 buttons joystick HID device. The report descriptor used in the 16_buttons_rpi_joystick_usb gadget definition is presented in hexadecimal values as follows:

```
TBD
```

The actual USB Report Descriptor can be defined as following:

```
TBD
```

6. Save and reboot the Rpi zero:
  
```
sudo reboot
```
  
7. Connect your Rpi zero to your computer and make sure it recognizes your Rpi zero as a USB HID joystick device named "RaspberryPi Joystick".

<p align="center">
<img align="center" src="https://raw.githubusercontent.com/milador/RaspberryPi-Joystick/master/Resources/rpi_joystick_cpanel.PNG" width="50%" height="50%" alt="raspberry pi joystick device in cpanel"/>
</p>
  
8.  Startup your Rpi zero and enter following commands to test the configuration:
   
```
sudo /usr/bin/16_buttons_rpi_joystick_usb
ls -la /dev/hidg*
```   

You should get something similar to following which means it's working and ready to use.

```
crw------- 1 root root 243, 0 Dec 26 02:34 /dev/hidg0
```   

# Usage

A sample code to convert keyboard actions to joystick actions using command line and a keyboard is available to test the functionality.

1.  Download the 16 buttons keyboard input interface code

  1.1. Create a new python file using following command:
  
```
sudo nano 16_buttons_keyboard.py
sudo chmod +x 16_buttons_keyboard.py
```   

Note : Make sure you are in /home/pi directory 

  1.2. Copy and paste the 16_buttons_keyboard.py code available under Code directory.[16_buttons_keyboard.py](https://github.com/milador/RaspberryPi-Joystick/blob/master/16_Buttons/Code/16_buttons_keyboard.py)

  1.3. Save 16_buttons_keyboard.py file and exit
  
  1.4. Test operating RaspberryPi-Joystick using 16_buttons_keyboard.py code with a physical keyboard or SSH
  
```
sudo python 16_buttons_keyboard.py
```   

  1.5. Use "q" key to exit.

2.	Add 16_buttons_keyboard.py code to startup scripts and run it automatically after OS boot

  2.1. Open /etc/rc.local
  
```
sudo nano /etc/rc.local
```
  2.2. Add following command on the line above "exit 0" and save it. ( Add it on the line before "exit 0" )
  
```
sudo python 16_buttons_keyboard.py
```

3. 16_buttons_keyboard.py usage:

TBD

  
  
