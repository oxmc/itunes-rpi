#!/usr/bin/env python3

import json,ast,os,tempfile,eyed3
cwd = os.getcwd()

#Function taken from pi-ware
def istherefile(file):
    try:
        file_tst = open(file)
        file_tst.close()
    except FileNotFoundError:
        return False
    else:
        return True

#Custom functions
def createjsonfile(data, name):
    if name == "":
        raise Exception("Provide a file name")
    if data == "":
        raise Exception("Provide data to save")
    if istherefile(f'{name}.json'):
        raise Exception("File already exists")
    else:
        with open(f'{name}.json', 'w') as json_file:
            json.dump(data, json_file)

def createtempfile(data, name):
    if name == "":
        raise Exception("Provide a file name")
    if data == "":
        raise Exception("Provide data to save")

def getmp3info(path):
    finfo = eyed3.load(path)
    try:
        artist = finfo.tag.artist
    except:
        artist = "Unkown"
    try:
        album = finfo.tag.album
    except:
        album = "Unkown"
    try:
        title = finfo.tag.title
    except:
        title = "Unkown"
    return {"artist": artist,
            "album": album,
            "title": title}

#function taken from github gists
def fixjson(string):
    if istherefile(f"{cwd}/json/jsontofix.json"):
        print("1")
        os.remove(f"{cwd}/json/jsontofix.json")
    if istherefile(f"{cwd}/json/fixedjson.json"):
        print("2")
        os.remove(f"{cwd}/json/fixedjson.json")
    createjsonfile(string, f"{cwd}/json/jsontofix")
    if istherefile(f"{cwd}/json/jsontofix.json"):
        fr=open(f"{cwd}/json/jsontofix.json")
        fw=open(f"{cwd}/json/fixedjson.json", "w")
        for line in fr:
            json_dat = json.dumps(ast.literal_eval(line))
            dict_dat = json.loads(json_dat)
            json.dump(dict_dat, fw)
            fw.write("\n")
        fw.close()
        fr.close()
        resp=open(f"{cwd}/json/fixedjson.json", "r")
        res=resp.read()
        os.remove(f"{cwd}/json/jsontofix.json")
        os.remove(f"{cwd}/json/fixedjson.json")
        return res
    else:
        raise Exception("No file exists at: '{cwd}/json/jsontofix.json'")
