#!/bin/bash


grep 'jane' ../data/list.txt
grep ' jane ' ../data/list.txt
grep " jane " ../data/list.txt | cut -d ' ' -f 1
grep " jane " ../data/list.txt | cut -d ' ' -f 2
grep " jane " ../data/list.txt | cut -d ' ' -f 3
grep " jane " ../data/list.txt | cut -d ' ' -f 1-3
grep " jane " ../data/list.txt | cut -d ' ' -f 1,3

if test -e ~/data/jane_profile_07272018.doc; then echo "File exists"; else echo "File doesn't exist"; fi

> test.txt
echo "I am appending text to this test file" >> test.txt
cat test.txt

for i in 1 2 3; do echo $i; done

