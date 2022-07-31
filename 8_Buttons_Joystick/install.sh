#!/usr/bin/env bash

#Step 1: Install and update dependencies
sudo apt update
sudo apt install -y python3-pip python3-gpiozero python3-evdev git

#Step 2: Clone code from github
git clone https://github.com/milador/RaspberryPi-Joystick
cd RaspberryPi-Joystick/8_Buttons_Joystick

#Step 3: Load the USB gadget drivers
grep --quiet "^dtoverlay=dwc2$" /boot/config.txt
if [ $? -eq 1 ]; then
    echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
fi
grep --quiet "^dwc2$" /etc/modules
if [ $? -eq 1 ]
then
    echo "dwc2" | sudo tee -a /etc/modules
fi
grep --quiet "^libcomposite$" /etc/modules
if [ $? -eq 1 ]
then
    echo "libcomposite" | sudo tee -a /etc/modules
fi


#Step 4: Install 8 button USB gamepad gadget and load it on boot
chmod +x 8_buttons_rpi_joystick_usb
sudo cp 8_buttons_rpi_joystick_usb /usr/bin/
# Insert line in /etc/rc.local, if needed
grep --quiet "^/usr/bin/8_buttons_rpi_joystick_usb$" /etc/rc.local
if [ $? -eq 1 ]
then
    sudo sed -i '/^exit 0/i \
/usr/bin/8_buttons_rpi_joystick_usb' /etc/rc.local
fi

#Step 5: Install rpi_device rule to give permission and allow hidg0 access
RULE_NAME='rpi_device.rules'
sudo cp ${RULE_NAME} /etc/udev/rules.d/
echo "Rule added"

#Step 6: Install 8_Buttons_Joystick service and start it
cd /home/pi/RaspberryPi-Joystick/8_Buttons_Joystick/
SERVICE_NAME='8_buttons_joystick.service'
IS_ACTIVE=$(sudo systemctl is-active $SERVICE_NAME)
if [ "$IS_ACTIVE" = "active" ]; then
    # restart the service
    echo "Service is running"
    echo "Restarting service"
    sudo systemctl restart $SERVICE_NAME
    echo "Service restarted"
else
    # create service file
    echo "Creating service file"
    sudo chmod +x ${SERVICE_NAME}
	sudo cp ${SERVICE_NAME} /etc/systemd/system/
    #Restart daemon, enable and start service
    echo "Reloading daemon and enabling service"
    sudo systemctl daemon-reload 
    sudo systemctl enable ${SERVICE_NAME} # remove the extension
    sudo systemctl start ${SERVICE_NAME}
    echo "Service Started"
fi

#Step 7: Rebooting RaspberryPi
echo "Rebooting RaspberryPi."
sleep 3
sudo reboot
