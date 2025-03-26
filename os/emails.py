#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib


def generate_email_attachment(sender, recipient, subject, body, attachment_path):
    """Creates an email with an attachement."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # Process the attachment and add it to the email
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=attachment_filename)

    return message


def generate_email(sender, recipient, subject, body):
    """Creates an email without an attachement."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    return message


def send_email(message):
    """Sends the message to the configured SMTP server."""
    sender_email = "noreply@mail.com"
    receiver_email = "account@mail.com"
    password = "your_email_password"
    smtp_server = "smtp.mail.com"
    smtp_port = 25

    # Use the login() method to authenticate with the server
    #server.login(sender_email, password)

    mail_server = smtplib.SMTP(smtp_server)
    mail_server.send_message(message)
    mail_server.quit()
