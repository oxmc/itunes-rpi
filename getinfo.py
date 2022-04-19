#!/usr/bin/env python3

import time,json,os,getpass,sys,re
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
#drive_name = os.popen(f"lsblk {devicejson['DEVPATH']} | tail -n +2 | cut -d/ -f4").read().strip()
print("Checking for mp3's")
#Windows Testing:
directory = f"D:\\iPod_Control\\Music\\"
#Normal:
#directory = f"/media/{username}/{drive_name}/iPod_Control/Music/"
#print(directory)
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
                #music_info = (minfo)
                print(file)
                music_info1 = {f'{file}':[minfo]}
                print(music_info1)
                music_info2 =re.sub(r'.', '', str(music_info1), count = 1)
                print(music_info2)
                music_info = music_info2[:-1]
                #minfo = {file:{**music_info[file], **d}}
                #music_info = f'{file}":"{music_info}'
                print(music_info)
                media_list3.append(music_info)
                #media_list2[file] = music_info
                #deviceinfo = os.popen(f'cat /media/{username}/{drive_name}/iPod_Control/iTunes/DeviceInfo').read().strip()
            #else:
            #    print("False")
    else:
        print(f"Not mp3: {f}")

#print(media_list2)
#media_list3.append(media_list2)
print(media_list3)
media_list["media"] = media_list3
print(media_list)
createjsonfile(media_list, "media")
