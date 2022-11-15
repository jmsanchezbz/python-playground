#!/usr/bin/env python3

import re
import operator
import csv

error = {}
per_user = {}

with open('syslog.log', 'r') as file:
  line = file.readline()
  while line:
    #error = re.search(r"ticky: ERROR ([\w ]*) \(([\w]+)\)", line)
    #info = re.search(r"ticky: INFO ([\w ]*) \[#\b\d{4}\b\] \(([\w]+)\)", line)
    match = re.search(
        r"ticky: ([\w+]*) ([\w' ]*)[\[#\d{4}]*\]? \((.*)\)$", line)
    code, msg, user = match.group(1), match.group(2), match.group(3)

    if match != None:
      if code == 'ERROR':
        if msg not in error:
          error[msg] = 0
        error[msg] += 1

      if user not in per_user:
        per_user[user] = {}
        #only to codes 'INFO' and 'ERROR'
        per_user[user]['INFO'] = 0
        per_user[user]['ERROR'] = 0

      per_user[user][code] += 1
    line = file.readline()

  file.close()

sorted_errors = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
sorted_users = sorted(per_user.items())

print(sorted_errors)
print(sorted_users)

with open('error_message.csv', 'w', newline='') as csvfile:
  fieldnames = ['Error', 'Count']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  for error, count in sorted_errors:
    writer.writerow({'Error': error, 'Count': count})
  csvfile.close()

with open('user_statistics.csv', 'w', newline='') as csvfile:
  fieldnames = ['Username', 'INFO', 'ERROR']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  for user, msgs in sorted_users:
    writer.writerow(
        {'Username': user, 'INFO': msgs['INFO'], 'ERROR': msgs['ERROR']})
  csvfile.close()
