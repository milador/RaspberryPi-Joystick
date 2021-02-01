"""
Demonstrate use of the NSGamepad class with GPIO pins. nsgamepad_usb must
be run first to create the USB gadget.

$ sudo apt update
$ sudo apt install gpiozero

Must be run as root like this:
$ sudo ./nsgamepad_usb
$ cd Code
$ sudo python3 gamepad_gpio.py
"""
import time
import threading
import signal
from gpiozero import Button
from NSGamepad import *

Gamepad = NSGamepad()

# Map the 4 direction buttons (up, right, down, left) to NS direction pad values
BUTTONS_MAP_DPAD = array.array('B', [
    # U = Up button, R = right button, etc
    #                   LDRU
    DPad.CENTERED,    # 0000
    DPad.UP,          # 0001
    DPad.RIGHT,       # 0010
    DPad.UP_RIGHT,    # 0011
    DPad.DOWN,        # 0100
    DPad.CENTERED,    # 0101
    DPad.DOWN_RIGHT,  # 0110
    DPad.CENTERED,    # 0111
    DPad.LEFT,        # 1000
    DPad.UP_LEFT,     # 1001
    DPad.CENTERED,    # 1010
    DPad.CENTERED,    # 1011
    DPad.DOWN_LEFT,   # 1100
    DPad.CENTERED,    # 1101
    DPad.CENTERED,    # 1110
    DPad.CENTERED     # 1111
])

class DpadBits(object):
    """ Convert 4 direction buttons to direction pad values """
    def __init__(self):
        self.dpad_bits = 0

    def set_bit(self, bit_num):
        """ Set bit in direction pad bit map. Update NSGadget direction pad. """
        self.dpad_bits |= (1 << bit_num)
        return BUTTONS_MAP_DPAD[self.dpad_bits]

    def clear_bit(self, bit_num):
        """ Clear bit in direction pad bit map. Update NSGadget direction pad. """
        self.dpad_bits &= ~(1 << bit_num)
        return BUTTONS_MAP_DPAD[self.dpad_bits]

def gpio_handler():
    """ Thread to handle buttons connected to GPIO pins. """
    all_buttons = {}
    dpad_bits = DpadBits()

    def gpio_pressed(button):
        """ Called when button connected to GPIO pin is pressed/closed """
        print('pressed', button.pin)
        if button.pin in all_buttons:
            ns_button = all_buttons[button.pin]
            if ns_button < 128:
                Gamepad.press(ns_button)
            else:
                Gamepad.dPad(dpad_bits.set_bit(255 - ns_button))
        else:
            print('Invalid button');

    def gpio_released(button):
        """ Called when button connected to GPIO pin is released/opened """
        print('released', button.pin)
        if button.pin in all_buttons:
            ns_button = all_buttons[button.pin]
            if ns_button < 128:
                Gamepad.release(ns_button)
            else:
                Gamepad.dPad(dpad_bits.clear_bit(255 - ns_button))
        else:
            print('Invalid button');

    gpio_ns_map = (
        # Left side (blue joy-con) buttons
        {'gpio_number': 4, 'ns_button': NSButton.LEFT_THROTTLE},
        {'gpio_number': 17, 'ns_button': NSButton.LEFT_TRIGGER},
        {'gpio_number': 27, 'ns_button': NSButton.MINUS},
        {'gpio_number': 22, 'ns_button': NSButton.CAPTURE},
        {'gpio_number': 5, 'ns_button': 255},
        {'gpio_number': 6, 'ns_button': 254},
        {'gpio_number': 13, 'ns_button': 253},
        {'gpio_number': 19, 'ns_button': 252},
        {'gpio_number': 26, 'ns_button': NSButton.LEFT_STICK},

        # Right side (red joy-con) buttons
        {'gpio_number': 23, 'ns_button': NSButton.RIGHT_THROTTLE},
        {'gpio_number': 24, 'ns_button': NSButton.RIGHT_TRIGGER},
        {'gpio_number': 25, 'ns_button': NSButton.PLUS},
        {'gpio_number': 8, 'ns_button': NSButton.HOME},
        {'gpio_number': 7, 'ns_button': NSButton.A},
        {'gpio_number': 12, 'ns_button': NSButton.B},
        {'gpio_number': 16, 'ns_button': NSButton.X},
        {'gpio_number': 20, 'ns_button': NSButton.Y},
        {'gpio_number': 21, 'ns_button': NSButton.RIGHT_STICK}
    )
    # For each GPIO to NS button entry, allocate gpiozero Button object
    # and update all_buttons dictionary. The when_pressed and when_released
    # callback functions use all_buttons to find the corresponding
    # NS button value.
    for element in gpio_ns_map:
        element['button'] = Button(element['gpio_number'])
        all_buttons[element['button'].pin] = element['ns_button']
        element['button'].when_pressed = gpio_pressed
        element['button'].when_released = gpio_released

    signal.pause()

def main():
    """ main program """
    threading.Thread(target=gpio_handler, args=(), daemon=True).start()

    Gamepad.begin('/dev/hidg0')

    while True:
        """ Read from keyboard and mouse input using evdev? """
        pass

if __name__ == "__main__":
    main()
