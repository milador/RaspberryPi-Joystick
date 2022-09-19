# Linux USB gadget HID driver for the Xbox Adaptive Controller

The Linux USB gadget HID driver on the Raspberry Pi Zero W does not work
with the Xbox Adaptive Controller (XAC). The changes described below
makes the driver compatible with the XAC.

## How to build the driver
Follow the instructions from the following link to get and build the
Raspberry Pi OS from source code.

https://www.raspberrypi.org/documentation/linux/kernel/building.md

Be sure to install the dependencies and toolchains. Choose whether
cross-compiling or compiling on a Raspberry Pi.

```
sudo apt install git bc bison flex libssl-dev make libc6-dev libncurses5-dev
sudo apt install crossbuild-essential-armhf
```

```bash
git clone --depth=1 --branch rpi-5.10.y https://github.com/raspberrypi/linux
cd linux
git checkout raspberrypi-kernel_1.20210201-1
```

Make the changes to f_hid.c as described below.

Build the kernel three times for the different CPU types currently in use.
Copy the driver usb_f_hid.ko to the RaspberryPi-Joystick directory.

```bash
DEST=${HOME}/RaspberryPi-Joystick/XACGamepad/Drivers
TAIL=kernel/drivers/usb/gadget/function
NUMCPU=8    # change for your system. 4 if using Raspberry Pi 3 or 4.

## For Pi 1, Pi Zero, Pi Zero W, or Compute Module:
KERNEL=kernel
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- bcmrpi_defconfig
make -j ${NUMCPU} ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- zImage modules dtbs
DESTDIR="${DEST}/5.10.11+/${TAIL}"
if [ ! -d ${DESTDIR} ]
then
    mkdir -p ${DESTDIR}
fi
find . -name usb_f_hid.ko -print0 |xargs -0 -I{} cp {} "${DESTDIR}"

## For Pi 2, Pi 3, Pi 3+, or Compute Module 3:
KERNEL=kernel7
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- bcm2709_defconfig
make -j ${NUMCPU} ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- zImage modules dtbs
DESTDIR="${DEST}/5.10.11-v7+/${TAIL}"
if [ ! -d ${DESTDIR} ]
then
    mkdir -p ${DESTDIR}
fi
find . -name usb_f_hid.ko -print0 |xargs -0 -I{} cp {} "${DESTDIR}"

## For Raspberry Pi 4 and 400:

KERNEL=kernel7l
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- bcm2711_defconfig
make -j ${NUMCPU} ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- zImage modules dtbs
DESTDIR="${DEST}/5.10.11-v7l+/${TAIL}"
if [ ! -d ${DESTDIR} ]
then
    mkdir -p ${DESTDIR}
fi
find . -name usb_f_hid.ko -print0 |xargs -0 -I{} cp {} "${DESTDIR}"
```

At this point update the github repo with the latest drivers.

To install them on a Raspberry Pi do the following.

```
cd ${HOME}
git clone https://github.com/RaspberryPi-Joystick.git
cd RaspberryPi-Joystick/XACGamepad/Drivers
sudo cp -R 5.* /lib/modules/
```

Kernel Release|Description
------------|-------------------------------------------------
5.10.11+    |For Pi 1, Pi Zero, Pi Zero W, or Compute Module
5.10.11-v7+ |For Pi 2, Pi 3, Pi 3+, or Compute Module 3
5.10.11-v7l+|For Raspberry Pi 4 or Pi 400


## Driver Changes

The XAC does not like bInterval=10 so bInterval is set to 1 for both endpoints.
This matches bInterval on a Logitech Extreme 3D joystick which works with the
XAC. The other change is to acknowledge the HID SET_IDLE request. The XAC
sends this command but without this change the gadget driver responds with USB
STALL which the XAC does not like. The change does not implement the SET_IDLE
request but it responds with sucess anyway. This is enough to make the XAC
happy. None of these changes can be made using USB gadget configfs.

Changes to f_hid.c which compiles to usb_f_hid.ko.

```
diff --git a/drivers/usb/gadget/function/f_hid.c b/drivers/usb/gadget/function/f_hid.c
index 8315fca29cff..54f7b3bbf7c5 100644
--- a/drivers/usb/gadget/function/f_hid.c
+++ b/drivers/usb/gadget/function/f_hid.c
@@ -191,7 +191,7 @@ static struct usb_endpoint_descriptor hidg_fs_in_ep_desc = {
        .bEndpointAddress       = USB_DIR_IN,
        .bmAttributes           = USB_ENDPOINT_XFER_INT,
        /*.wMaxPacketSize       = DYNAMIC */
-       .bInterval              = 10, /* FIXME: Add this field in the
+       .bInterval              =  1, /* FIXME: Add this field in the
                                       * HID gadget configuration?
                                       * (struct hidg_func_descriptor)
                                       */
@@ -203,7 +203,7 @@ static struct usb_endpoint_descriptor hidg_fs_out_ep_desc = {
        .bEndpointAddress       = USB_DIR_OUT,
        .bmAttributes           = USB_ENDPOINT_XFER_INT,
        /*.wMaxPacketSize       = DYNAMIC */
-       .bInterval              = 10, /* FIXME: Add this field in the
+       .bInterval              =  1, /* FIXME: Add this field in the
                                       * HID gadget configuration?
                                       * (struct hidg_func_descriptor)
                                       */
@@ -560,6 +560,12 @@ static int hidg_setup(struct usb_function *f,
                goto stall;
                break;

+       case ((USB_DIR_OUT | USB_TYPE_CLASS | USB_RECIP_INTERFACE) << 8
+                 | HID_REQ_SET_IDLE):
+               VDBG(cdev, "set_idle\n");
+               goto respond;
+               break;
+
        case ((USB_DIR_IN | USB_TYPE_STANDARD | USB_RECIP_INTERFACE) << 8
                  | USB_REQ_GET_DESCRIPTOR):
                switch (value >> 8) {
```
