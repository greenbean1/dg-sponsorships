# Sending emails via tutorial: https://realpython.com/python-send-email/
import smtplib
import ssl
from email.mime.text import MIMEText
import csv_functions
from random import randrange

EMAIL_PASSWORD_FILE = 'email_info.txt'
EMAIL_SENDING_LOG = 'emailing_log.csv'

# RECEIVING_EMAILS = ['beauhoover1@gmail.com', 'uninathan@gmail.com', 'jancvanbruggen@gmail.com']
RECEIVING_EMAILS = 'beauhoover1@gmail.com'
SENDER_EMAIL = "greenbeandev1@gmail.com"
PORT = 465  # For SSL
SMTP_SERVER = "smtp.gmail.com"


def get_password():
    file = open(EMAIL_PASSWORD_FILE, 'r')
    return file.read()


def get_interesting_word():
    interesting_words = ['Interesting', 'Exciting', 'Shocking', 'Insane', 'Sweet', 'Mysterious', 'Dank', 'Hot']
    return interesting_words[randrange(len(interesting_words))]


def compose_message(names, article_url):
    interesting_word = get_interesting_word()
    string_names = ' & '.join(names)
    message = f"""\
    Subject: New Disc Golf Sponsorship Agreement\n {interesting_word} news! {string_names} now sponsored! Check this article for more info: {article_url}"""
    fixed_message = message.replace("\x0a", " ")
    print(message)
    return fixed_message


def build_email_body(names, article_url):
    interesting_word = get_interesting_word()
    string_names = ' & '.join(names)
    return f' {interesting_word} news! {string_names} now sponsored! Check this article for info: {article_url}'


def build_full_email_message(names, article_url):
    msg = MIMEText(build_email_body(names, article_url), 'html')
    msg['Subject'] = 'New Disc Golf Sponsorship Agreement'
    msg_string = msg.as_string()
    return msg_string


def test_simple_compose_message():
    msg1 = MIMEText('BEAU HALLEAU', 'html')
    msg1['Subject'] = 'YESSSSS'
    msg2 = msg1.as_string()
    return msg2


def send_email(names, article_url):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
        for receiver_email in RECEIVING_EMAILS:
            server.login(SENDER_EMAIL, get_password())
            server.sendmail(SENDER_EMAIL, receiver_email, compose_message(names, article_url))
    csv_functions.log_timestamp(EMAIL_SENDING_LOG)


def test_send_email(names, article_url):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
        server.login(SENDER_EMAIL, get_password())
        server.sendmail(SENDER_EMAIL, RECEIVING_EMAILS, build_full_email_message(names, article_url))
    csv_functions.log_timestamp(EMAIL_SENDING_LOG)
