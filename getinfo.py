#!/usr/bin/env python3

import time,json,os,getpass,sys,re,base64
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
if istherefile(f"{cwd}/media.json"):
    os.remove(f"{cwd}/media.json")

media_list, media_list2, media_list3, music_info, minfo = {}, {}, [], {}, {}
#devicejson = json.loads(sys.argv[1])
#print(devicejson)
#Main
#Wait for lsblk
time.sleep(2)
#Windows Testing:
drive_name = "ALEKS"
#Normal:
#drive_name = os.popen(f"lsblk {devicejson['DEVPATH']} | tail -n +2 | awk '{print $NF}' | cut -d/ -f4 | tr '\n' ' ' | awk '{print $NF}'").read().strip()
print("Checking for mp3's")
#Windows Testing:
directory = f"D:\\iPod_Control\\Music\\"
#Normal:
#directory = f"/media/{username}/{drive_name}/iPod_Control/Music/"
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a dir
    if os.path.isdir(f):
        print(f"Dir: {f}")
        for file in os.listdir(f):
            if file.endswith(".mp3"):
                floc = f"{f}/{file}"
                fn = Path(floc).stem
                #print(floc)
                mi = getmp3info(floc)
                minfo['floc'] = floc
                minfo['artist'] = mi['artist']
                minfo['album'] = mi['album']
                minfo['title'] = mi['title']
                minfo['b64'] = "error"
                with open(f"{floc}", "rb") as audio_file:
                    b64_string = base64.b64encode(audio_file.read())
                    minfo['b64'] = b64_string
                music_info1 = {minfo}
                print(music_info1)
                media_list3.append(music_info1)
                #deviceinfo = os.popen(f'cat /media/{username}/{drive_name}/iPod_Control/iTunes/DeviceInfo').read().strip()
    else:
        print(f"Not mp3: {f}")

print(media_list3)
media_list["media"] = media_list3
print(media_list)
createjsonfile(media_list, "media")
