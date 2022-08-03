#!/usr/bin/env bash

REPO_NAME='RaspberryPi-Joystick'
RULE_NAME='rpi_device.rules'
GADGET_NAME='XACGamepad'
USB_GADGET_NAME='xac_gamepad_usb'
SERVICE_NAME='xac_gamepad.service'

echo "Instaling $GADGET_NAME .."

#Step 1: Get current kernel version 
KERNEL_VERSION=$(uname -r | egrep -o '^[^-+]+')
echo "Step 1: Kernel version is currently set to ${KERNEL_VERSION}"


#Step 2: Install and update dependencies
sudo apt update
if [ $KERNEL_VERSION = "5.10.11" ] || [$GADGET_NAME != "XACGamepad"]; then
    echo "Step 2: Kernel version is already setup"
else
    sudo rpi-update 43998c82a7e88df284b7aa30221b2d0d21b2b86a -y
    echo "Step 2: Kernel version is successfully downgraded to 5.10.11"
fi
sudo apt install -y python3-pip python3-gpiozero python3-evdev git

#Step 3: Clone code from github
[ ! -d ${REPO_NAME} ] && git clone https://github.com/milador/RaspberryPi-Joystick
cd ${REPO_NAME}/${GADGET_NAME}
echo "Step 3: Repository was cloned"

#Step 4: Load the USB gadget drivers
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
echo "Step 4: Successfully loaded the USB gadget drivers."

#Step 5: Update Linux USB gadget HID driver module if necessary 
if [ $GADGET_NAME = "XACGamepad" ]; then
    cd Drivers
    sudo cp -R 5.* /lib/modules/
    echo "Step 5: Successfully updated Linux USB gadget HID driver module."
    cd ..
fi

#Step 6: Install USB gamepad gadget and load it on boot
chmod +x ${USB_GADGET_NAME}
sudo cp ${USB_GADGET_NAME} /usr/bin/
# Insert line in /etc/rc.local, if needed
grep --quiet "^/usr/bin/"${USB_GADGET_NAME}"$" /etc/rc.local
if [ $? -eq 1 ]
then
    sudo sed -i '/^exit 0/i \/usr/bin/'${USB_GADGET_NAME} /etc/rc.local
fi
echo "Step 6: Successfully installed USB gamepad gadget descriptor."

#Step 7: Install rpi_device rule to give permission and allow hidg0 access
sudo cp ${RULE_NAME} /etc/udev/rules.d/
echo "Step 7: Successfully added rpi_device rule."

#Step 8: Install xac_gamepad service and start it
IS_ACTIVE=$(sudo systemctl is-active $SERVICE_NAME)
if [ "$IS_ACTIVE" = "active" ]; then
    # restart the service
    echo "Service is running"
    echo "Restarting service"
    sudo systemctl restart $SERVICE_NAME
    echo "Step 8: Service successfully restarted"
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
    echo "Step 8: Service successfully started"
fi

#Step 9: Rebooting RaspberryPi
echo "Step 9: Rebooting RaspberryPi."
sleep 3

