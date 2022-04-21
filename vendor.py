#!/usr/bin/env python3

import pyudev
context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
# For USB devices
monitor.filter_by('usb')
# OR specifically for most USB serial devices
#monitor.filter_by(susbystem='tty')
for action, device in monitor:
    vendor_id = device.get('ID_VENDOR_ID')
    print(vendor_id)
    # I know the devices I am looking for have a vendor ID of '22fa'
    if vendor_id in ['o5ac']:
        print(f'Detected {action} for device with vendor ID {vendor_id}')

#import pyudev
#context = pyudev.Context()
#for device in context.list_devices(subsystem='block', DEVTYPE='partition'):
#    print(device.get('ID_FS_LABEL', 'unlabeled partition'))