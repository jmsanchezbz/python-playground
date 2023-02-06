
#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

path = os.path.expanduser('~')+"/supplier-data/images"

url = "http://localhost/upload/"
for f in os.listdir(path):
    if f.endswith(".jpeg"):
        with open(path + '/' + f, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
