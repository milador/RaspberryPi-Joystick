# Interface Setup Installation Instructions 

# Hardware requirements 

We use [Adafruit 128x64 OLED Bonnet for Raspberry Pi](https://www.adafruit.com/product/3192) for this interface which offers an OLED display and buttons for navigation.  The OLED Bonnet comes pre-soldered so you need to stack header pins over RaspberryPi Zero header pins.
  
# Software requirements  

  1. Follow the official installation instruction of [Bonnet for Raspberry Pi](https://learn.adafruit.com/adafruit-128x64-oled-bonnet-for-raspberry-pi/usage) on Adafruit website.
  
 # Software installation 
 
1. Install the circuitpython-ssd1306 package
```
sudo pip3 install adafruit-circuitpython-ssd1306
```

2.	Install PIL to allow using text with custom fonts
```
sudo apt-get install python3-pil
```

3.	Enable I2C 

  3.1. Enter RaspberryPi software configuration tool
```
sudo raspi-config
```
  3.2. Select "Interfacing Options" and press enter
  
  3.3. Select "I2C" and press enter
  
  3.4. Select "Yes" and press enter to enable "I2C"

4.	Reboot RaspberryPi

```
sudo reboot
```


5.	Shutdown RaspberryPi after you enabled I2C.

```
sudo shutdown -h now
```

6.	Once the Pi has halted, plug in the [Adafruit 128x64 OLED Bonnet for Raspberry Pi](https://www.adafruit.com/product/3192). Now you can power the RaspberryPi again.

7.	Type the following command to check if OLED Bonnet is connected which confirms I2C is configured.

```
sudo i2cdetect -y 1
```

8.	Verify I2C Device

  8.1. Create a new python script file

```
sudo nano ~pi/bonnet_buttons.py
```

  8.2. Copy and paste [ssd1306_bonnet_buttons](https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_SSD1306/master/examples/ssd1306_bonnet_buttons.py) example into bonnet_buttons.py

  8.3. Save bonnet_buttons.py file

  8.4. Run the demo bonnet_buttons.py code

```
sudo python3 bonnet_buttons.py
```

  8.5. Press buttons to interact with the demo code and check everything is working.



9.	Run script on Boot

  9.1. Open /etc/rc.local file

```
sudo nano /etc/rc.local
```

  9.2. Add following command on the line above "exit 0" and save it. ( Add it on the line before "exit 0" )
  
```
sudo python /home/pi/bonnet_buttons.py  &
```



