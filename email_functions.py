#Followed this tutorial: https://realpython.com/python-send-email/
import smtplib, ssl
import csv_functions
from random import randrange

EMAIL_PASSWORD_FILE = 'email_info.txt'
EMAIL_SENDING_LOG = 'emailing_log.csv'

RECEIVING_EMAILS = ['beauhoover1@gmail.com', 'uninathan@gmail.com', 'jancvanbruggen@gmail.com']
PORT = 465  # For SSL
SMTP_SERVER = "smtp.gmail.com"
SENDER_EMAIL = "greenbeandev1@gmail.com"


def get_password():
    file = open(EMAIL_PASSWORD_FILE, 'r')
    return file.read()


def compose_message(names, article_url):
    interesting_words = ['Interesting', 'Exciting', 'Shocking', 'Insane', 'Sweet', 'Mysterious']
    interesting_word = interesting_words[randrange(len(interesting_words))]
    message = """\
    Subject: New Disc Golf Sponsorship Agreement

    X news! namesLIST were all sponsored!! Check article_url for more info"""
    return message


def send_email(names, article_url):
    for email_address in RECEIVING_EMAILS:
        # Send Emails
    csv_functions.log_timestamp(EMAIL_SENDING_LOG)


receiver_email = "beauhoover1@gmail.com "  # Enter receiver address
# password = input("Type your password and press enter: ")
message = """\
Subject: New Disc Golf Sponsorship Agreement

This message was sent from Python. Pick up pswd from new place!"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)