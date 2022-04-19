#!/usr/bin/env python3

import usbdev
import time,json,os,getpass
from pathlib import Path
from functions import fixjson,createjsonfile,istherefile,getmp3info
#Set global var username
global username
username = getpass.getuser()
#Set global var cwd
global cwd
cwd = os.getcwd()
#Global od
global od
od = None
#Setup
if istherefile(f"{cwd}/json/jsontofix.json"):
    os.remove(f"{cwd}/json/jsontofix.json")
if istherefile(f"{cwd}/json/fixedjson.json"):
    os.remove(f"{cwd}/json/fixedjson.json")
#start listening for usb device change events
#you may have to unplug the flashdrive and replug
observer = usbdev.startListener()
while 1:
    time.sleep(2)
    #get the status of the connected usb device
    status = usbdev.isDeviceConnected()
    #get device identification data 
    device = usbdev.getDevData()
    if device != None:
        devicejson = json.loads(fixjson(device))
    else:
        print("No new USB device connected")
        print("---------------------------------")
    #Show info
    #print(f"Connected: {status}")
    if device != None:
        if od != None:
            if od == device:
                print("Same device")
                print("---------------------------------")
            else:
                od = device
        #print(device)
        #print(f"Vendor: {devicejson['VENDOR']}")
        if devicejson['VENDOR'] == "Apple":
            print("Possible Ipod!")
            if devicejson['MODEL'] == "iPod":
                print("IPOD FOUND")
                isipod = True
                exec(os.popen(f"python3 getinfo.py '{devicejson}'"))
                device = None
            else:
                print("Not an ipod, is apple device")
                isipod = False
                device = None
        else:
            print("Not an apple device, returning to listening for new usb connections")
            device = None
usbdev.stopListener(observer)