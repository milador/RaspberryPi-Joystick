# Linux USB Gadget NSGamepad

The file nsgamepad_usb, based on xac_gamepad_usb, configures the USB OTG
port as a gamepad with 2 analog sticks, 1 dpad, and 14 buttons. Be sure to run
it as root using sudo. Or set it up to auto run from /etc/rc.local. See the
docs for 8_joystick.

```
$ cd NSGamepad
$ sudo ./nsgamepad_usb
```

The class and test program are in Scripts/NSGamepad.py.

The class can be imported into another Python3 program like this.

```
from NSGamepad import *
```

To run the gamepad demo program do the following. The program presses and
releases all buttons then rotates the joysticks and dpad.

```
$ cd Code
$ sudo python3 gamepad_demo.py
```

## Nintendo Switch
To run the gamepad keyboard program for a Nintendo Switch do the following.

```
$ cd Code
$ sudo python3 gamepad_keyboard.py
```

The active keys for a Nintendo Switch are listed below

Key |Gamepad button
----|--------------
1   |A
2   |B
3   |X
4   |Y
5   |L
6   |R
7   |ZL
8   |ZR
9   |+
0   |-
W   |left stick up
A   |left stick left
S   |left stick down
D   |left stick right
P   |right stick up
L   |right stick left
;   |right stick down
'   |right stick right
Q   |quit program

To control a Nintendo Switch, use a Mayflash Magic NS adapter. Plug the
Zero into the Mayflash adapter then plug the Mayflash adapter into the Switch
dock. I suggest using the dock because the adapter and Zero may draw too much
current from the Switch battery if it is plugged directly into the Switch.
Configure the adapter to "Switch Pro" mode. The LED should be purple.

IMPORTANT: The Switch uses wireless communications even when a controller is
plugged in via USB. To change this start from the Home screen. Select
System Settings | Controllers and Sensors | Pro Controller Wired Communication.
Change it to ON.

## Playstation 4

To run the gamepad keyboard program for a Playstation 4 do the following.

```
$ cd Code
$ sudo python3 gamepad_keyboard_ps4.py
```

The active keys for a Playstation 4 are listed below

Key |Gamepad button
----|--------------
1   |CIRCLE
2   |SQUARE
3   |TRIANGLE
4   |CROSS
5   |L1
6   |R1
7   |L2
8   |R2
9   |OPTIONS
0   |LOGO
W   |left stick up
A   |left stick left
S   |left stick down
D   |left stick right
P   |right stick up
L   |right stick left
;   |right stick down
'   |right stick right
Q   |quit program

To control a Playstation 4, use a Mayflash Magic S Pro adapter. This adapter
supports PS4 and Nintendo Switch. Plug the Zero into the Mayflash adapter then
plug the Mayflash adapter into the PS4. Configure the adapter to "PS4" mode.
The LED should be blue.
