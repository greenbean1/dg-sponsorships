from email.mime.text import MIMEText
from os import path
from random import randrange
import smtplib
import ssl
from typing import List

import csv_functions


RECEIVING_EMAILS = ['beauhoover1@gmail.com', 'uninathan@gmail.com', 'jancvanbruggen@gmail.com', 'chrisschek@gmail.com']
SENDER_EMAIL = 'greenbeandev1@gmail.com'
PORT = 465  # For SSL
SMTP_SERVER = 'smtp.gmail.com'


def get_password(filename: str, directory: str) -> str:
    password_file_path = path.join(directory, filename)
    file = open(password_file_path, 'r')
    return file.read()


def get_interesting_word() -> str:
    interesting_words = ['Spicy', 'Riveting', 'Shocking', 'Captivating', 'Sweet', 'Unbelievable', 'Dank', 'Hot']
    return interesting_words[randrange(len(interesting_words))]


def build_email_body(names: List[str], article_url: str) -> str:
    interesting_word = get_interesting_word()
    string_names = ' & '.join(names)
    return f' {interesting_word} news! {string_names} now sponsored! Check this article for info: {article_url}'


def build_full_email_message(names: List[str], article_url: str) -> str:
    msg = MIMEText(build_email_body(names, article_url), 'html')
    msg['Subject'] = 'New Disc Golf Sponsorship Agreement'
    msg_string = msg.as_string()
    return msg_string


def send_email(names: List[str],
               article_url: str,
               email_password_filename: str,
               email_sending_log_filename: str,
               directory: str) -> None:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
        server.login(SENDER_EMAIL, get_password(email_password_filename, directory))
        server.sendmail(SENDER_EMAIL, RECEIVING_EMAILS, build_full_email_message(names, article_url))
    csv_functions.log_timestamp(email_sending_log_filename, directory)
