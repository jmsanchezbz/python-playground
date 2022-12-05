#!/usr/bin/env python3
import os
import datetime
import reports
import emails

dt = datetime.date.today().strftime("%B  %d, %Y")
date = "Processed Update on " + dt
names = []
weights = []
path = os.path.expanduser('~')+"/supplier-data/descriptions"

for file in os.listdir(path):
    with open(path + "/" + file) as f:
        for i,ln in enumerate(f):
            line = ln.strip()
            if i==0:
                fruit_name = "name: " + line
                print(fruit_name)
                names.append(fruit_name)
            elif i==1:
                fruit_weight = "weight: " + line
                print(fruit_weight)
                weights.append(fruit_weight)

summary = ""
for name, weight in zip(names, weights):
    summary += name + '<br />' 
    summary += weight + '<br />' + '<br />'

if __name__ == "__main__":
    reports.generate_report("/tmp/processed.pdf", date, summary)
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)
