#!/usb/bin/python3
"""

Read keyboard and mouse input events then trigger gamepad buttons and sticks.
Input from tty devices such as UARTs and ssh sessions do not count as keyboard
events. This works for USB and Bluetooth HID keyboards and mice.

To BT pair with keyboard or mouse, run the Raspbery Pi OS GUI and use the
Bluetooth tray applet to Add Device.

# Install input event module
sudo apt install python3-evdev

cd NSGamepad
# Create USB gamepad gadget
sudo ./nsgamepad_usb
cd Code
# Read keyboard and mouse events then press/release gamepad buttons.
sudo python3 gamepad_inputevent.py

"""

import sys
import asyncio
import evdev
from NSGamepad import *

Gamepad = NSGamepad()
Gamepad.begin('/dev/hidg0')

# Map keyboard keys or mouse buttons to gamepad buttons.
EVENT2BUTTON = {
    str(evdev.ecodes.KEY_A): NSButton.A,
    str(evdev.ecodes.KEY_B): NSButton.B,
    str(evdev.ecodes.KEY_X): NSButton.X,
    str(evdev.ecodes.KEY_Y): NSButton.Y,
    str(evdev.ecodes.BTN_LEFT): NSButton.A,
    str(evdev.ecodes.BTN_RIGHT): NSButton.B,
    str(evdev.ecodes.BTN_MIDDLE): NSButton.X,
    str(evdev.ecodes.BTN_SIDE): NSButton.Y,
    str(evdev.ecodes.BTN_EXTRA): NSButton.HOME,
}

async def handle_events(device):
    # Grab exclusive access means the shell and/or GUI no longer receives the input events
    with device.grab_context():
        async for event in device.async_read_loop():
            if event.code == evdev.ecodes.KEY_PAUSE:
                sys.exit(0)
            if str(event.code) in EVENT2BUTTON:
                gamepad_button = EVENT2BUTTON[str(event.code)]
                if event.value == 1:
                    print('Key or button down', 'gamepad down', gamepad_button)
                    Gamepad.press(gamepad_button)
                elif event.value == 0:
                    print('Key or button up', 'gamepad up', gamepad_button)
                    Gamepad.release(gamepad_button)
            else:
                """ Map mouse motion to thumbstick motion """
                if event.code == evdev.ecodes.REL_X:
                    print('REL_X', event.value)
                    #Gamepad.leftXAxis(?)
                elif event.code == evdev.ecodes.REL_Y:
                    print('REL_Y', event.value)
                    #Gamepad.leftYAxis(?)
                elif event.code == evdev.ecodes.REL_WHEEL:
                    print('REL_WHEEL', event.value)
                    #Gamepad.rightYAxis(?)
                elif event.code == evdev.ecodes.REL_HWHEEL:
                    print('REL_HWHEEL', event.value)
                    #Gamepad.rightXAxis(?)
                elif event.code == evdev.ecodes.ABS_X:
                    print('ABS_X', event.value)
                    #Gamepad.leftXAxis(?)
                elif event.code == evdev.ecodes.ABS_Y:
                    #Gamepad.leftYAxis(?)
                    print('ABS_Y', event.value)

# Examine all input devices and find keyboards and mice.
# Process all keyboard and mouse input events.
for devpath in evdev.list_devices():
    device = evdev.InputDevice(devpath)
    print(device)
    print(device.path, device.name, device.phys)
    print(device.capabilities(verbose=True))
    if evdev.ecodes.EV_KEY in device.capabilities():
        print('Has EV_KEY')
        print(device.capabilities()[evdev.ecodes.EV_KEY])
        if evdev.ecodes.KEY_A in device.capabilities()[evdev.ecodes.EV_KEY]:
            print('Keyboard', device)
            asyncio.ensure_future(handle_events(device))
        elif evdev.ecodes.BTN_MOUSE in device.capabilities()[evdev.ecodes.EV_KEY]:
            print('Mouse', device)
            asyncio.ensure_future(handle_events(device))

loop = asyncio.get_event_loop()
loop.run_forever()
