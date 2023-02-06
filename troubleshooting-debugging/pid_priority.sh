#!/bin/bash

#reassign priority of all ffmpeg processes
for pid in $(pidof ffmpeg; do renice 19 $pid; don)