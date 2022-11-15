#!/usr/bin/env python3
from multiprocessing import Pool
import os
import subprocess

# 1 - Set SRC
src = "{}/data/prod".format(os.getenv("HOME"))

# 4 - Pool RSYNC commands


def runprocess(folder):
    dest = "{}/data/prod_backup".format(os.getenv("HOME"))
    subprocess.call(["rsync", "-arq", folder, dest])


# 2 - Set folders array
folders = []
for root, _dir, files in os.walk(src):
   for name in _dir:
      folders.append(os.path.join(root, name))

# 3 Build and run the Pool
p = Pool(len(folders))
p.map(runprocess, folders)
