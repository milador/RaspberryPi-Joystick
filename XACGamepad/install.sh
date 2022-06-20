#!/usr/bin/env bash
sudo apt update
sudo apt install -y python3-pip python3-gpiozero python3-evdev git

cd
git clone https://github.com/milador/RaspberryPi-Joystick
cd RaspberryPi-Joystick/NSGamepad

# Update system files to load the USB gadget drivers, if needed.
grep --quiet "^dtoverlay=dwc2$" /boot/config.txt
if [ $? -eq 1 ]
then
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

# Install USB NS gadget on boot
chmod +x ns_gamepad_usb
sudo cp ns_gamepad_usb /usr/bin/
# Insert line in /etc/rc.local, if needed
grep --quiet "^/usr/bin/ns_gamepad_usb$" /etc/rc.local
if [ $? -eq 1 ]
then
    sudo sed -i '/^exit 0/i \
/usr/bin/ns_gamepad_usb' /etc/rc.local
fi

# TBD Update usb_f_hid.ko files. This required for XAC but not NS.

# TBD Install service?

# TBD Expire pi account password?

# TBD Remove SSH keys?

# Remove my SSID/PSK
sudo rm /etc/wpa_supplicant/wpa_supplicant.conf

#sudo raspi-config overlay-file-system turn on???
echo "Powering off so an IMG can be created from this microSD card."
sleep 1
sudo poweroff