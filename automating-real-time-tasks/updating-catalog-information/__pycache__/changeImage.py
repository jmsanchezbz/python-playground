#!/usr/bin/env python3
from PIL import Image
import os

WIDTH=400
HEIGHT=400

path = os.path.expanduser('~')+"/supplier-data/images"

for f in os.listdir(path):
    if f.endswith(".tiff"):
        split_f = f.split(".")
        name = split_f[0] + ".jpeg"
        img = Image.open(path + f).convert("RGB").resize((WIDTH, HEIGHT))
        img.save(path+"/" + name, "JPEG")
