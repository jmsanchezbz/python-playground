#!/usr/bin/env python3

import sys

logfile = sys.argv[1]
with open(logfile) as f:
    for line in f:
        print(line.striI())