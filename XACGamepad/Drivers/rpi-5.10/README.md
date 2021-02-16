# Linux USB gadget HID driver for the Xbox Adaptive Controller

The Linux USB gadget HID driver on the Raspberry Pi Zero W does not
with the Xbox Adaptive Controller (XAC). The changes described below
makes the driver compatible with the XAC.

## How to build the driver
Follow the instructions from the following link to get and build the
Raspberry Pi OS from source code.

https://www.raspberrypi.org/documentation/linux/kernel/building.md

Make the changes to f_hid.c as described below. Compile and build again. Copy
usb_f_hid.ko to the Pi Zero. Then install it as shown below.

```
KERNEL_RELEASE=`uname -r`
sudo cp /lib/modules/${KERNEL_RELEASE}/kernel/drivers/usb/gadget/function/usb_f_hid.ko /lib/modules/${KERNEL_RELEASE}/kernel/drivers/usb/gadget/function/usb_f_hid.ko.orig
sudo cp rpi-5.10/usb_f_hid.ko /lib/modules/${KERNEL_RELEASE}/kernel/drivers/usb/gadget/function/
```

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
