import os

RECEIVING_EMAILS = ['beauhoover1@gmail.com', 'uninathan@gmail.com', 'jancvanbruggen@gmail.com', 'chrisschek@gmail.com']
# RECEIVING_EMAILS = ['beauhoover1@gmail.com']  # For debuggin'

DISC_GOLF_ARTICLE_URL = 'https://discgolf.ultiworld.com/2020/11/02/2021-player-sponsorship-tracker/'
PRIMARY_DG_CSV_FILENAME = 'disc_golf_info.csv'
EMAIL_PASSWORD_FILENAME = 'email_info.txt'
EMAIL_SENDING_LOG = 'emailing_log.csv'
SCRAPING_LOG = 'scraping_log.csv'
CURRENT_MODULE_PATH = os.path.abspath(__file__)
CURRENT_MODULE_DIRECTORY = os.path.dirname(CURRENT_MODULE_PATH)