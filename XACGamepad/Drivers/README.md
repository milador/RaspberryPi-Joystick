# Linux USB gadget HID driver for the Xbox Adaptive Controller

The Linux USB gadget HID driver on the Raspberry Pi does not work
with the Xbox Adaptive Controller (XAC). The changes described below
makes the driver compatible with the XAC.

## How to build the driver
Follow the instructions from the following link to get and build the
Raspberry Pi OS from source code.

https://www.raspberrypi.org/documentation/linux/kernel/building.md

Be sure to install the dependencies and toolchains. Choose whether
cross-compiling or compiling on a Raspberry Pi. We choose cross-compiling for purpose of this document to go over the process 

  1. Install the dependencies and toolchains

```
sudo apt install git bc bison flex libssl-dev make libc6-dev libncurses5-dev
sudo apt install crossbuild-essential-armhf                     #32-bit Toolchain for a 32-bit Kernel
sudo apt install crossbuild-essential-arm64                     #64-bit Toolchain for a 64-bit Kernel
```

  2. Get the Kernel Sources

```bash
git clone --branch rpi-5.15.y https://github.com/raspberrypi/linux
cd linux
git checkout 1.20220830
```

Note: You can find the branch name and use tag or hash code for the release number to checkout. 

  3. Make the changes to HID function module source code or f_hid.c file. Please follow instructions under **Driver Changes** section.

  4. Build the kernel for the different CPU types currently in use and copy the driver usb_f_hid.ko.xz to the RaspberryPi-Joystick directory.

```bash
DEST=${HOME}/RaspberryPi-Joystick/XACGamepad/Drivers
TAIL=kernel/drivers/usb/gadget/function
NUMCPU=8    # change for your system. 4 if using Raspberry Pi 3 or 4.
KERNEL_RELEASE=$(uname -r | egrep -o '^[^-+]+')   # release number 

## For Pi 1, Pi Zero, Pi Zero W, or Compute Module:
KERNEL=kernel
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- bcmrpi_defconfig
make -j ${NUMCPU} ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- zImage modules dtbs
DESTDIR="${DEST}/${KERNEL_RELEASE}+/${TAIL}"
if [ ! -d ${DESTDIR} ]
then
    mkdir -p ${DESTDIR}
fi
find . -name usb_f_hid.ko -print0 |xargs -0 -I{} cp {} "${DESTDIR}"
xz "${DESTDIR}"/usb_f_hid.ko

## For Pi 2, Pi 3, Pi 3+, or Compute Module 3:
KERNEL=kernel7
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- bcm2709_defconfig
make -j ${NUMCPU} ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- zImage modules dtbs
DESTDIR="${DEST}/${KERNEL_RELEASE}-v7+/${TAIL}"
if [ ! -d ${DESTDIR} ]
then
    mkdir -p ${DESTDIR}
fi
find . -name usb_f_hid.ko -print0 |xargs -0 -I{} cp {} "${DESTDIR}"
xz "${DESTDIR}"/usb_f_hid.ko

## For Raspberry Pi 4 and 400:

KERNEL=kernel7l
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- bcm2711_defconfig
make -j ${NUMCPU} ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- zImage modules dtbs
DESTDIR="${DEST}/${KERNEL_RELEASE}-v7l+/${TAIL}"
if [ ! -d ${DESTDIR} ]
then
    mkdir -p ${DESTDIR}
fi
find . -name usb_f_hid.ko -print0 |xargs -0 -I{} cp {} "${DESTDIR}"
xz "${DESTDIR}"/usb_f_hid.ko

KERNEL=kernel8
make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- bcm2711_defconfig
make -j ${NUMCPU} ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- Image modules dtbs
DESTDIR="${DEST}/${KERNEL_RELEASE}-v8+/${TAIL}"
if [ ! -d ${DESTDIR} ]
then
    mkdir -p ${DESTDIR}
fi
find . -name usb_f_hid.ko -print0 |xargs -0 -I{} cp {} "${DESTDIR}"
xz "${DESTDIR}"/usb_f_hid.ko

```

  5. Install all drivers on a Raspberry Pi do the following.

```
cd ${HOME}
git clone https://github.com/RaspberryPi-Joystick.git
cd RaspberryPi-Joystick/XACGamepad/Drivers
sudo cp -R 5.* /lib/modules/
```

Kernel Release|Description
------------|-------------------------------------------------
5.15.61+    |For Pi 1, Pi Zero, Pi Zero W, or Compute Module
5.15.61-v7+ |For Pi 2, Pi 3, Pi 3+, or Compute Module 3
5.15.61-v7l+|For Raspberry Pi 4 or Pi 400 (32 Bit)
5.15.61-v8+ |For Raspberry Pi 4 or Pi 400 (64 Bit)


## Driver Changes

The XAC does not like bInterval=10 so bInterval is set to 1 for both endpoints.
This matches bInterval on a Logitech Extreme 3D joystick which works with the
XAC. The other change is to acknowledge the HID SET_IDLE request. The XAC
sends this command but without this change the gadget driver responds with USB
STALL which the XAC does not like. The change does not implement the SET_IDLE
request but it responds with sucess anyway. This is enough to make the XAC
happy. None of these changes can be made using USB gadget configfs.

  1. Open f_hid.c ( To be compiled as usb_f_hid.ko )

```
sudo nano /home/pi/linux/drivers/usb/gadget/function/f_hid.c
```

  2. Make required changes to f_hid.c file ( Last change can be skipped in more recent kernel releases )
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
