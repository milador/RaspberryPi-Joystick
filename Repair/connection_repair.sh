bluetoothctl paired-devices | cut -f2 -d' '|
while read -r uuid
do
    info=`bluetoothctl info $uuid`
    if echo "$info" | grep -q "Connected: no"; then
       echo "Connecting:"
       echo "$info" | grep "Name"
       bluetoothctl connect $uuid
    fi
done

if [ "$(sudo systemctl is-active 8_buttons_joystick.service)" = "active" ]; then
  sudo systemctl restart 8_buttons_joystick.service
  echo "Restarted 8_buttons_joystick.service"
elif [ "$(sudo systemctl is-active 16_buttons_joystick.service)" = "active" ]; then
  sudo systemctl restart 16_buttons_joystick.service
  echo "Restarted 16_buttons_joystick.service"
elif [ "$(sudo systemctl is-active 32_buttons_joystick.service)" = "active" ]; then
  sudo systemctl restart 32_buttons_joystick.service
  echo "Restarted 32_buttons_joystick.service"
elif [ "$(sudo systemctl is-active ns_gamepad.service)" = "active" ]; then
  sudo systemctl restart ns_gamepad.service
  echo "Restarted ns_gamepad.service"
elif [ "$(sudo systemctl is-active ps_gamepad.service)" = "active" ]; then
  sudo systemctl restart ps_gamepad.service
  echo "Restarted ps_gamepad.service"
elif [ "$(sudo systemctl is-active xac_gamepad.service)" = "active" ]; then
  sudo systemctl restart xac_gamepad.service
  echo "Restarted xac_gamepad.service"
fi
