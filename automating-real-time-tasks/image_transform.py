#!/usr/bin/env python3

from PIL import Image
import os

# Rotate the image 90° clockwise
# Resize the image from 192x192 to 128x128
# Save the image to a new folder in .jpeg format

dest_path='tmp'

# the output width of all images
WIDTH = 128
HEIGHT = 128
ROTATION = -90
FORMAT = 'JPEG'

def process_image(dest_path, filename, width, height, rotation, format='JPEG'):
    img = Image.open(filename)

    if rotation:
        img = img.rotate(rotation)

    if width and height:
        img = img.resize((width, height))

    img = img.convert('RGB')

    try:
        img.save(os.path.join(dest_path,image), format, optimize=True)
    except OSError as e:
        print("ERROR: Image process image ", filename, str(e))

