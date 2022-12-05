#! /usr/bin/env python3
import os
import requests

fruits = {}
keys = ["name", "weight", "description", "image_name"]
url = "http://ipaddress/fruits/"
path = os.path.expanduser('~')+"/supplier-data"
desc_path = path+"/descriptions"
img_path = path+"/images"

for file in os.listdir(desc_path):
    with open(path + file) as f:
        for i,ln in enumerate(f):
            line = ln.strip()
            if i==0:
                fruits[keys[i]] = line
            elif i==1:    #"lbs" in line:
                fruits[keys[i]] = int(line.split()[0])
            elif i==2:
                fruits[keys[i]] = line

        name = file.split(".")[0] + ".jpeg"
        fruits["image_name"] = name
        """for img in os.listdir(img_path):
            if img == name:
                fruits["image_name"] = name"""
        response = requests.post(url, json=fruits)
        fruits.clear()
