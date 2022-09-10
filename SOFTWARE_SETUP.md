# Software requirements and setup

## Software requirements  

Install latest version of Raspbian OS on an SD card according to the official documents on [raspberrypi.org](https://www.raspberrypi.org/documentation/installation/installing-images/).

  1. Download and install [Raspberry Pi Imager](https://www.raspberrypi.com/software/) in your computer.
  2. Insert the MicroSD Card into SD Card reader slot of your computer. ( You can use SD Card USB Adapter as well )
  3. Run Raspberry Pi Imager software 
  4. Click on the "CHOOSE STORAGE" button and select your SD Card drive.
  5. Click on the "CHOOSE OS" button and select "Raspberry Pi OS".
  6. Click on the settings button with a gear icon.
  7. Click on the checkbox next to "Enable SSH" to enable SSH.
  8. Click on the checkbox next to "Configure Wireless LAN", and enter your Wi-fi network username and password.
  9. Click on the "SAVE" button
  10. Click on the "WRITE" button and wait for it to write the image to the SD Card.
  11. You will get a dialog box titled "Write Successful" Once the verification process is complete. Click on the "CONTINUE" button.
  12. Remove MicroSD Card and insert it in the SD Card reader slot of your Raspberry Pi.
  
 ## Software installation 
 
 ### Option 1
 
1.	Login to your Raspberry Pi
2.	Open a web browser 
3.	Download [install.sh](https://github.com/milador/RaspberryPi-Joystick/blob/master/Install/install.sh) to your main /home/pi/ directory ( Make sure you save it as .sh or shell script )
4.	Run the shell script to install the software. You can pass an argument to define your desired configuration.

Note: The configuration for XAC Compatible Gamepad will be selected if no argument is passed.
  
```
sh install.sh
```

- 8 Button Gamepad
```
sh install.sh 8b
```

- 16 Button Gamepad
```
sh install.sh 16b
```

- 32 Button Gamepad
```
sh install.sh 32b
```

- NS Compatible Gamepad
```
sh install.sh ns
```

- PS Compatible Gamepad
```
sh install.sh ps
```

- XAC Compatible Gamepad
```
sh install.sh xac
```
5.	Raspberry Pi will reboot once the installation process is complete.
6.	Startup your Rpi and enter following command to test the configuration ( Optional ):
   
```
ls -la /dev/hidg*
```   

You should get something similar to following which means it's working and ready to use.

```
crw------- 1 root root 243, 0 Dec 26 02:34 /dev/hidg0
```   

7.	Windows 10 detects Raspberry Pi joystick as a USB HID device and you can use find it under Control Panel\Hardware and Sound\Devices and Printers.

<p align="center">
<img align="center" src="./Resources/Images/Cpanel.png" width="50%" height="50%" alt="raspberry pi joystick device in cpanel"/>
</p>

 ### Option 2
 
1.	Download/Clone project repository in your computer 
2.	Enter the "Insall" directory 
3.	Open install_windows.bat file with a text editor 
4.	Change the ip address and set your raspberry pi local ip address 
5.	Set the raspberry pi password if it is no longer set to "raspberry"
6.	Save the file
7.	Run the install_windows.bat file to install the software.

Note: The configuration for XAC Compatible Gamepad will be installed by default. Change the last line of setup.sh for other gamepad configurations.
  
- 8 Button Gamepad
```
sh ./install.sh 8b
```

- 16 Button Gamepad
```
sh ./install.sh 16b
```

- 32 Button Gamepad
```
sh ./install.sh 32b
```

- NS Compatible Gamepad
```
sh ./install.sh ns
```

- PS Compatible Gamepad
```
sh install.sh ps
```


- XAC Compatible Gamepad
```
sh ./install.sh xac
```
8.	Raspberry Pi will reboot once the installation process is complete.

9.	Startup your Rpi and enter following command to test the configuration ( Optional ):
   
```
ls -la /dev/hidg*
```   

You should get something similar to following which means it's working and ready to use.

```
crw------- 1 root root 243, 0 Dec 26 02:34 /dev/hidg0
```   

10.	Windows 10 detects Raspberry Pi joystick as a USB HID device and you can use find it under Control Panel\Hardware and Sound\Devices and Printers.

<p align="center">
<img align="center" src="./Resources/Images/Cpanel.png" width="50%" height="50%" alt="raspberry pi joystick device in cpanel"/>
</p>

### Option 3
 
1.	Download/Clone project repository in your computer 
2.	Enter the "Insall" directory 
3.	Open Command line or terminal 
4.	Enter following command:

#### Windows

```
plink -ssh -v -pw raspberry pi@10.0.0.0 -m setup.sh
```

#### Mac

```
ssh pi@10.0.0.0 'bash -s' < setup.sh
```

  1.1.	Change the ip address and set your raspberry pi local ip address 
  
  1.2.	Set the raspberry pi password if it is no longer set to "raspberry"
  
5.	Press enter to execute the command to install the software.

Note: The configuration for XAC Compatible Gamepad will be installed by default. Change the last line of setup.sh for other gamepad configurations.
  
- 8 Button Gamepad
```
sh install.sh 8b
```

- 16 Button Gamepad
```
sh install.sh 16b
```

- 32 Button Gamepad
```
sh install.sh 32b
```

- NS Compatible Gamepad
```
sh install.sh ns
```

- PS Compatible Gamepad
```
sh install.sh ps
```


- XAC Compatible Gamepad
```
sh install.sh xac
```
6.	Raspberry Pi will reboot once the installation process is complete.

7.	Startup your Rpi and enter following command to test the configuration ( Optional ):
   
```
ls -la /dev/hidg*
```   

You should get something similar to following which means it's working and ready to use.

```
crw------- 1 root root 243, 0 Dec 26 02:34 /dev/hidg0
```   

8.	Windows 10 detects Raspberry Pi joystick as a USB HID device and you can use find it under Control Panel\Hardware and Sound\Devices and Printers.

<p align="center">
<img align="center" src="./Resources/Images/Cpanel.png" width="50%" height="50%" alt="raspberry pi joystick device in cpanel"/>
</p>

## Usage Setup

1.	Connect RaspberryPi to one of the USB ports on your host device. Make sure you use an external power source to power RPi Zero. 
2.	Make sure all the USB and Bluetooth input devices are connected.
3.	Wait 30 seconds for it to initialize.
4.	Move your input mice or press the keys on the input keyboard to initiate the connection if they are already paired.


### Bluetooth Connection 

1.  Pair BT keyboard/mouse using RaspberryPi GUI taskbar.

  1.1. Click on Bluetooth button icon on top right of RaspberryPi GUI taskbar.
<p align="center">
<img align="center" src="https://github.com/milador/RaspberryPi-Joystick/blob/master/Resources/Images/BT_Pair_Open.PNG" width="50%" height="50%" alt="RaspberryPi GUI taskbar bluetooth menu"/>
</p>

  1.2. Click on Add Device
  
  1.3. Select your BT keyboard/mouse and Click on Pair button
<p align="center">
<img align="center" src="https://raw.githubusercontent.com/milador/RaspberryPi-Joystick/master/Resources/Images/BT_Pair_Add.PNG" width="50%" height="50%" alt="BT keyboard/mouse scanning menu"/>
</p>

