#!/usr/bin/env python3

#Change files with jane name and replace to jdoe

import sys
import subprocess

try:
  with open(sys.argv[1], 'r') as file:
    lines = file.readlines()
    for line in lines:
      dst = line.replace('jane', 'jdoe')
      subprocess.run("mv "+line.strip()+" " +
                     dst.strip(), shell=True, check=True)
    file.close()
except IndexError:
  print("File not passed as argument")
