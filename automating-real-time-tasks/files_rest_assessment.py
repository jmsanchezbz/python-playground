#!/usr/bin/env python3

import os
import requests

dir="tmp"
url="http://url/feedback"

def json_data(file):
    types = ["title", "name", "date", "feedback"]
    dict = {}
    with open(file,"r") as txtfile:
        lines = [line.replace('\n','') for line in txtfile]
        for index, type in enumerate(types):
            dict[type] = lines[index]
        #dict = { "title": lines[0], "name": lines[1], "date": lines[2], "feedback": lines[3]}
    return dict

def send_data(json):
    res = requests.post(url, data=json)

    if not res.status_code == 201:
        print(" ERROR :" + res.status_code + " " + res.reason)

    return res.ok


for file in os.listdir(dir):
    jsondata = json_data(dir + "/" + file)
    print(jsondata)
    res = send_data(jsondata)

print("ok end")
