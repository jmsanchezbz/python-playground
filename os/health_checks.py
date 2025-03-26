#!/usr/bin/env python3
import shutil
import psutil
import socket
import emails
import os
import requests

def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75


# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything ok")
else:
    print("Network checks failed")

sender = "automation@mail.net"
receiver = "receiver@mail.com"
body = "Please check your system and resolve the issue as soon as possible."

def check_website_up(url):
   print("-------Check_website_up")
   global body
   subject = "Error - website " + url
   try:
      response = requests.get(url,verify=False)
      body += "/n url: " + url + " status_code: " + str(response.status_code)
      if (response.status_code==200):
         print("--Response url: " + url + " status_code " + str(response.status_code))
      else:
         print("--Error response url: " + url + " status_code " + str(response.status_code))
         message = emails.generate_email(sender,receiver,subject,body)
         emails.send_email(message)
   except Exception as e:
      print("ERROR " + str(e))
      body = "Error by checking if website is up"
      message = emails.generate_email(sender,receiver,subject,body)
      emails.send_email(message)

def check_cpu_pct_ok():
   """ Checks CPU usage and sends email if usage >80% """
   cpu_pct = psutil.cpu_percent(1)
   if cpu_pct > 80:
      subject = "Error - CPU usage is over 80%"
      print(subject)
      message = emails.generate_email(sender, receiver, subject, body)
      emails.send_email(message)

def check_disk_space_ok():
   """ Checks disk usage and sends email if available space < 20% """
   du = shutil.disk_usage("/")
   du_pct = du.free/du.total * 100
   if du_pct < 20:
      subject = "Error - Available disk space is less than 20%"
      print(subject)
      message = emails.generate_email(sender, receiver, subject, body)
      emails.send_email(message)

def check_virtual_memory_ok():
   """ Checks for available memory, if < 500mb sends an email """
   mem = psutil.virtual_memory()
   trs = 500 * 1024 * 1024  # 500MB
   if mem.available < trs:
      subject = "Error - Available memory is less than 500MB"
      print(subject)
      message = emails.generate_error_email(sender, receiver, subject, body)
      emails.send_email(message)

def check_resolve_hostname():
   """ Checks hostname and if cannot be resolved to "127.0.0.1" sends an email """
   hostname = socket.gethostbyname('localhost')
   if hostname != '127.0.0.1':
      subject = "Error - localhost cannot be resolved to 127.0.0.1"
      print(subject)
      message = emails.generate_error_email(sender, receiver, subject, body)
      emails.send_email(message)

