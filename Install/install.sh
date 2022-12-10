#!/usr/bin/env bash

REPO_NAME='RaspberryPi-Joystick'
RULE_NAME='rpi_device.rules'

echo "Instaling RaspberryPi-Joystick Software..."

GADGET_TYPE=$1

if [ -z $GADGET_TYPE ]; then
    GADGET_NAME='XACGamepad'
    USB_GADGET_NAME='xac_gamepad_usb'
    SERVICE_NAME='xac_gamepad.service'
elif [ $GADGET_TYPE = "8b" ]; then
    GADGET_NAME='8_Buttons_Joystick'
    USB_GADGET_NAME='8_buttons_joystick_usb'
    SERVICE_NAME='8_buttons_joystick.service'
elif [ $GADGET_TYPE = "16b" ]; then
    GADGET_NAME='16_Buttons_Joystick'
    USB_GADGET_NAME='16_buttons_joystick_usb'
    SERVICE_NAME='16_buttons_joystick.service'
elif [ $GADGET_TYPE = "32b" ]; then
    GADGET_NAME='32_Buttons_Joystick'
    USB_GADGET_NAME='32_buttons_joystick_usb'
    SERVICE_NAME='32_buttons_joystick.service'
elif [ $GADGET_TYPE = "ns" ]; then
    GADGET_NAME='NSGamepad'
    USB_GADGET_NAME='ns_gamepad_usb'
    SERVICE_NAME='ns_gamepad.service'
elif [ $GADGET_TYPE = "ps" ]; then
    GADGET_NAME='PSGamepad'
    USB_GADGET_NAME='ps_gamepad_usb'
    SERVICE_NAME='ps_gamepad.service'
elif [ $GADGET_TYPE = "xac" ]; then
    GADGET_NAME='XACGamepad'
    USB_GADGET_NAME='xac_gamepad_usb'
    SERVICE_NAME='xac_gamepad.service'
else
    GADGET_NAME='XACGamepad'
    USB_GADGET_NAME='xac_gamepad_usb'
    SERVICE_NAME='xac_gamepad.service'
fi
echo "Instaling $GADGET_NAME ..."

#Step 1: Get current kernel version
KERNEL_VERSION=$(uname -r | egrep -o '^[^-+]+')
echo "Step 1: Kernel version is currently set to ${KERNEL_VERSION}"

#Step 2: Install and update dependencies
sudo apt update
#sudo apt install -y python3-pip python3-gpiozero python3-evdev git
sudo apt install -y python3-pip python3-gpiozero git
pip install evdev -U
pip install fastapi uvicorn[standard]
echo "Step 2: Dependencies successfully installed"

#Step 3: Clone code from github
[ ! -d ${REPO_NAME} ] && git clone https://github.com/milador/RaspberryPi-Joystick
cd ${REPO_NAME}/${GADGET_NAME}
git checkout api
echo "Step 3: Repository was cloned"

#Step 4: Load the USB gadget drivers
grep --quiet "^dtoverlay=dwc2$" /boot/config.txt
if [ $? -eq 1 ]; then
    echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
fi
grep --quiet "^dwc2$" /etc/modules
if [ $? -eq 1 ]; then
    echo "dwc2" | sudo tee -a /etc/modules
fi
grep --quiet "^libcomposite$" /etc/modules
if [ $? -eq 1 ]; then
    echo "libcomposite" | sudo tee -a /etc/modules
fi
echo "Step 4: Successfully loaded the USB gadget drivers."

#Step 5: Install USB gamepad gadget and load it on boot
chmod +x ${USB_GADGET_NAME}
sudo cp ${USB_GADGET_NAME} /usr/bin/
# Insert line in /etc/rc.local, if needed
sudo sed -i '/\/usr\/bin\//d' /etc/rc.local
sudo sed -i '/^exit 0/i \/usr/bin/'${USB_GADGET_NAME} /etc/rc.local
#grep --quiet "^/usr/bin/"${USB_GADGET_NAME}"$" /etc/rc.local
#if [ $? -eq 1 ]
#then
#    sudo sed -i '/^exit 0/i \/usr/bin/'${USB_GADGET_NAME} /etc/rc.local
#fi
echo "Step 5: Successfully installed USB gamepad gadget descriptor."

#Step 6: Install rpi_device rule to give permission and allow hidg0 access
sudo cp ${RULE_NAME} /etc/udev/rules.d/
echo "Step 6: Successfully added rpi_device rule."

#Step 7: Install xac_gamepad service and start it
IS_ACTIVE=$(sudo systemctl is-active $SERVICE_NAME)
if [ $GADGET_NAME = "8_Buttons_Joystick" ]; then
    sudo systemctl stop '16_buttons_joystick.service' '32_buttons_joystick.service' 'ns_gamepad.service' 'ps_gamepad.service' 'xac_gamepad.service'
    sudo systemctl disable '16_buttons_joystick.service' '32_buttons_joystick.service' 'ns_gamepad.service' 'ps_gamepad.service' 'xac_gamepad.service'
elif [ $GADGET_NAME = "16_Buttons_Joystick" ]; then
    sudo systemctl stop '8_buttons_joystick.service' '32_buttons_joystick.service' 'ns_gamepad.service' 'ps_gamepad.service' 'xac_gamepad.service'
    sudo systemctl disable '8_buttons_joystick.service' '32_buttons_joystick.service' 'ns_gamepad.service' 'ps_gamepad.service' 'xac_gamepad.service'
elif [ $GADGET_NAME = "32_Buttons_Joystick" ]; then
    sudo systemctl stop '8_buttons_joystick.service' '16_buttons_joystick.service' 'ns_gamepad.service' 'ps_gamepad.service' 'xac_gamepad.service'
    sudo systemctl disable '8_buttons_joystick.service' '16_buttons_joystick.service' 'ns_gamepad.service' 'ps_gamepad.service' 'xac_gamepad.service'
elif [ $GADGET_NAME = "NSGamepad" ]; then
    sudo systemctl stop '8_buttons_joystick.service' '16_buttons_joystick.service' '32_buttons_joystick.service' 'xac_gamepad.service' 'ps_gamepad.service'
    sudo systemctl disable '8_buttons_joystick.service' '16_buttons_joystick.service' '32_buttons_joystick.service' 'xac_gamepad.service' 'ps_gamepad.service'
elif [ $GADGET_NAME = "PSGamepad" ]; then
    sudo systemctl stop '8_buttons_joystick.service' '16_buttons_joystick.service' '32_buttons_joystick.service' 'xac_gamepad.service' 'ns_gamepad.service'
    sudo systemctl disable '8_buttons_joystick.service' '16_buttons_joystick.service' '32_buttons_joystick.service' 'xac_gamepad.service' 'ns_gamepad.service'
elif [ $GADGET_NAME = "XACGamepad" ]; then
    sudo systemctl stop '8_buttons_joystick.service' '16_buttons_joystick.service' '32_buttons_joystick.service' 'ns_gamepad.service' 'ps_gamepad.service'
    sudo systemctl disable '8_buttons_joystick.service' '16_buttons_joystick.service' '32_buttons_joystick.service' 'ns_gamepad.service' 'ps_gamepad.service'
else
    sudo systemctl stop '8_buttons_joystick.service' '16_buttons_joystick.service' '32_buttons_joystick.service' 'ns_gamepad.service' 'ps_gamepad.service'
    sudo systemctl disable '8_buttons_joystick.service' '16_buttons_joystick.service' '32_buttons_joystick.service' 'ns_gamepad.service' 'ps_gamepad.service'
fi
sudo systemctl daemon-reload
sudo systemctl reset-failed
if [ "$IS_ACTIVE" = "active" ]; then
    # restart the service
    echo "Service is running"
    echo "Restarting service"
    sudo systemctl restart $SERVICE_NAME
    echo "Step 7: Service successfully restarted"
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
    echo "Step 7: Service successfully started"
fi

#Step 8: Rebooting RaspberryPi
echo "Step 8: Rebooting RaspberryPi."
echo "RaspberryPi-Joystick software successfully installed..."
sleep 3
sudo reboot
