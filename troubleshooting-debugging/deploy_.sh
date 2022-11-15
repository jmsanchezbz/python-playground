#!/bin/bash

# The videos need to be in the mp4 format in order to serve them
# in the website.
#
# This script runs ffmpeg in parallel to convert all of the webm files to mp4.
echo "Starting video conversion..."
for video in static/*.webm; do
    mp4_video="$(echo "$video"  | sed 's/\.webm$/.mp4/')"
    daemonize -c $PWD /usr/bin/ffmpeg -nostats -nostdin -i "$video" "$mp4_video"
done
