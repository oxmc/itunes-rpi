#!/usr/bin/env python3

import os,glob,getpass,json
from screeninfo import get_monitors
from datetime import date

#Import custom functions
from functions import istherefile

#Set global var username
global username
username = getpass.getuser()

#Get usbs
drive_list = os.listdir(f'/media/{username}/')
#print(drive_list)

#Loop through usbs
for i, drive_name in enumerate(drive_list):
    #print(i)
    #print(drive_name)
    print(f'/media/{username}/{drive_name}')
    #print(f'/media/{username}/{drive_name}/iPod_Control/iTunes/DeviceInfo')
    print("Checking for device info file")
    if istherefile(f'/media/{username}/{drive_name}/iPod_Control/iTunes/DeviceInfo'):
        print("True")
        isipod = True
        deviceinfo = os.popen(f'cat /media/{username}/{drive_name}/iPod_Control/iTunes/DeviceInfo').read()
    else:
        print("False")
        isipod = False
    print(deviceinfo)
    #for j, image_path_name in enumerate(glob.glob('/media/'+drive_name+'/*.jpg')):
        #print(image_path_name)
