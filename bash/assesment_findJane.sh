#!/bin/bash

#Find files in directory data that own jane and write in oldFiles.txt file

> oldFiles.txt
path=/home/student-00-d70e66156eee
files=$(grep '\bjane\b' $path/data/list.txt | cut -d ' ' -f 3)
for file in $files; do
  if test -e $path$file
  then echo $path$file>>oldFiles.txt
  fi
done