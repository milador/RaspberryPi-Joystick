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
sudo ./ns_gamepad_usb
cd Code
# Read keyboard and mouse events then press/release gamepad buttons.
sudo python3 gamepad_ns_inputevent.py

"""

import sys
import asyncio
import time  
import evdev
from enum import IntEnum
from NSGamepad import *

Gamepad = NSGamepad()
Gamepad.begin('/dev/hidg0')

DEBUG_MODE = False

mice_x_in = 0
mice_y_in = 0

gamepad_x_out = 0
gamepad_y_out = 0

reaction_time = 0.0

class GAMEPAD_XY(IntEnum):
    MinInputValue = -16
    MaxInputValue = 16
    MinOutputValue = 0
    MaxOutputValue = 255
    DeadZoneValue = 1
    OperationMode = 0  # 0: Don't Keep position after each mice move, 1: Keep position after each mice move
    ReactionTimeValue =  10  #10 ms

# Map keyboard keys or mouse buttons to gamepad buttons.
EVENT2ACTION = {
    'BUTTONS': {
        str(evdev.ecodes.BTN_LEFT): NSButton.A,
        str(evdev.ecodes.BTN_RIGHT): NSButton.B,
        str(evdev.ecodes.BTN_MIDDLE): NSButton.X,
        str(evdev.ecodes.BTN_SIDE): NSButton.Y,
        str(evdev.ecodes.BTN_EXTRA): NSButton.HOME,
        str(evdev.ecodes.KEY_A): NSButton.A,
        str(evdev.ecodes.KEY_B): NSButton.B,
        str(evdev.ecodes.KEY_X): NSButton.X,
        str(evdev.ecodes.KEY_Y): NSButton.Y,
    }, 
    'DIRECTIONS': {
        str(evdev.ecodes.KEY_UP): {"x":   128, "y": 0},
        str(evdev.ecodes.KEY_RIGHT): {"x":   255, "y": 128},
        str(evdev.ecodes.KEY_DOWN): {"x":   128, "y": 255},
        str(evdev.ecodes.KEY_LEFT): {"x":   0, "y": 128}
    },
    'OTHERS': {
        str(evdev.ecodes.REL_WHEEL): NSButton.HOME    
    }
}

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
    global mice_x_in
    global mice_y_in
    global gamepad_x_out
    global gamepad_y_out
    # Grab exclusive access means the shell and/or GUI no longer receives the input events
    with device.grab_context():
        async for event in device.async_read_loop():
            if event.code == evdev.ecodes.KEY_PAUSE:
                sys.exit(0)
            if str(event.code) in EVENT2ACTION.get('BUTTONS'):
                gamepad_button = EVENT2ACTION.get('BUTTONS')[str(event.code)]
                if event.value == 1:
                    if DEBUG_MODE: 
                        print('Key or button press', 'gamepad button press', gamepad_button)
                    Gamepad.press(gamepad_button)
                    time.sleep(0.05)
                elif event.value == 0:
                    if DEBUG_MODE: 
                        print('Key or button release', 'gamepad button release', gamepad_button)
                    Gamepad.release(gamepad_button)
            elif str(event.code) in EVENT2ACTION.get('DIRECTIONS'):
                gamepad_move = EVENT2ACTION.get('DIRECTIONS')[str(event.code)]
                if event.value == 1:
                    if DEBUG_MODE: 
                        print('Direction Key press', 'gamepad left axis move', gamepad_move)
                    Gamepad.leftXAxis(gamepad_move['x'])
                    Gamepad.leftYAxis(gamepad_move['y'])
                    time.sleep(0.05)
                elif event.value == 0:
                    if DEBUG_MODE: 
                        print('Direction Key release', 'gamepad left axis release', gamepad_move)
                    Gamepad.leftXAxis(128)
                    Gamepad.leftYAxis(128)
            else:
                """ Map mouse motion to thumbstick motion """
                if event.code == evdev.ecodes.REL_X and int(GAMEPAD_XY.OperationMode)== 0 and event.value != 0:
                    mice_x_in = event.value
                    gamepad_x_out = map_joystick(mice_x_in,int(GAMEPAD_XY.DeadZoneValue),int(GAMEPAD_XY.MinInputValue),int(GAMEPAD_XY.MaxInputValue),int(GAMEPAD_XY.MinOutputValue),int(GAMEPAD_XY.MaxOutputValue))
                    if DEBUG_MODE: 
                        print('REL_X', event.value , 'gamepad left x axis out', gamepad_x_out)
                    Gamepad.leftXAxis(gamepad_x_out)
                if event.code == evdev.ecodes.REL_X and int(GAMEPAD_XY.OperationMode) == 1:
                    mice_x_in = event.value + mice_x_in
                    gamepad_x_out = map_joystick(mice_x_in,int(GAMEPAD_XY.DeadZoneValue),int(GAMEPAD_XY.MinInputValue),int(GAMEPAD_XY.MaxInputValue),int(GAMEPAD_XY.MinOutputValue),int(GAMEPAD_XY.MaxOutputValue))
                    if DEBUG_MODE: 
                        print('REL_X', event.value , 'gamepad left x axis out', gamepad_x_out)
                    Gamepad.leftXAxis(gamepad_x_out)
                elif event.code == evdev.ecodes.REL_Y and int(GAMEPAD_XY.OperationMode)== 0 and event.value != 0:
                    mice_y_in = event.value
                    gamepad_y_out = map_joystick(mice_y_in,int(GAMEPAD_XY.DeadZoneValue),int(GAMEPAD_XY.MinInputValue),int(GAMEPAD_XY.MaxInputValue),int(GAMEPAD_XY.MinOutputValue),int(GAMEPAD_XY.MaxOutputValue))
                    if DEBUG_MODE: 
                        print('REL_Y', event.value , 'gamepad left y axis out', gamepad_y_out)
                    Gamepad.leftYAxis(gamepad_y_out)
                elif event.code == evdev.ecodes.REL_Y and int(GAMEPAD_XY.OperationMode)== 1:
                    mice_y_in = event.value + mice_y_in
                    gamepad_y_out = map_joystick(mice_y_in,int(GAMEPAD_XY.DeadZoneValue),int(GAMEPAD_XY.MinInputValue),int(GAMEPAD_XY.MaxInputValue),int(GAMEPAD_XY.MinOutputValue),int(GAMEPAD_XY.MaxOutputValue))
                    if DEBUG_MODE: 
                        print('REL_Y', event.value , 'gamepad left y axis out', gamepad_y_out)
                    Gamepad.leftYAxis(gamepad_y_out)
                elif event.code == evdev.ecodes.REL_WHEEL:
                    gamepad_button = EVENT2ACTION.get('OTHERS')[str(event.code)]
                    if event.value == 1:
                        Gamepad.press(gamepad_button)
                    elif event.value == -1:
                        Gamepad.release(gamepad_button)
                    if DEBUG_MODE: 
                        print('REL_WHEEL', event.value)
                elif event.code == evdev.ecodes.REL_HWHEEL:
                    if DEBUG_MODE: 
                        print('REL_HWHEEL', event.value)
                elif event.code == evdev.ecodes.ABS_X and event.value != 0:
                    if DEBUG_MODE: 
                        print('ABS_X', event.value)
                elif event.code == evdev.ecodes.ABS_Y and event.value != 0:
                    if DEBUG_MODE: 
                        print('ABS_Y', event.value)
                else:
                    time.sleep(reaction_time)
                    info = device.read_one()
                    if(info == None):
                        if gamepad_x_out != 128:
                           Gamepad.leftXAxis(128)
                        if gamepad_y_out != 128:
                           Gamepad.leftYAxis(128)
                    else:
                        device.write_event(info)
                    if DEBUG_MODE: 
                        print('Gamepad centering')



def map_joystick(value, deadzone_value, input_value_min, input_value_max, output_value_min, output_value_max):
    # Figure out the range 
    input_span = input_value_max - input_value_min
    output_span = output_value_max - output_value_min

    # Convert the input range into a 0 to 1 range (float value)   
    if (value>=-deadzone_value and value<=deadzone_value):
        value_scaled = 0.5
    elif (value<input_value_min):
        value_scaled = 0.0
    elif (value>input_value_max):
        value_scaled = 1.0
    else:
        value_scaled = float(value - input_value_min) / float(input_span)
    
    # Convert the 0-1 range into a value in the output range
    if value_scaled<=0:
        return output_value_min
    elif value_scaled>=1:
        return output_value_max
    else:
        return int(output_value_min + (value_scaled * output_span))


# Examine all input devices and find keyboards and mice.
# Process all keyboard and mouse input events.
def main():
    global reaction_time
    reaction_time = float(GAMEPAD_XY.ReactionTimeValue/1000)
    """ Trigger NS gamepad with USB or BT mouse and keyboard  """
    # Examine all input devices and find keyboards and mice.
    while len(evdev.list_devices()) == 0:
        if DEBUG_MODE: 
            print("Waiting for keyboard or mice")
        time.sleep(1)
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

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        Gamepad.end()
        time.sleep(0.1)
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)