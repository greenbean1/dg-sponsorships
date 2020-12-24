# Organize via blocks of imports for standard Python, nonstandard Python & local modules
import os

import csv_functions
import email_functions
import scrape_functions

DISC_GOLF_ARTICLE_URL = 'https://discgolf.ultiworld.com/2020/11/02/2021-player-sponsorship-tracker/'
PRIMARY_DG_CSV_FILENAME = 'disc_golf_info.csv'
EMAIL_PASSWORD_FILENAME = 'email_info.txt'
EMAIL_SENDING_LOG = 'emailing_log.csv'
SCRAPING_LOG = 'scraping_log.csv'
CURRENT_MODULE_PATH = os.path.abspath(__file__)
CURRENT_MODULE_DIRECTORY = os.path.dirname(CURRENT_MODULE_PATH)


dg_dict = scrape_functions.get_dict_from_url(DISC_GOLF_ARTICLE_URL, SCRAPING_LOG, CURRENT_MODULE_DIRECTORY)
if not csv_functions.file_exists(PRIMARY_DG_CSV_FILENAME, CURRENT_MODULE_DIRECTORY):
    csv_functions.write_to_primary_dg_csv(dg_dict, PRIMARY_DG_CSV_FILENAME, CURRENT_MODULE_DIRECTORY)
incremental_names = csv_functions.get_incremental_names(dg_dict, PRIMARY_DG_CSV_FILENAME, CURRENT_MODULE_DIRECTORY)
if incremental_names:
    email_functions.send_email(incremental_names,
                               DISC_GOLF_ARTICLE_URL,
                               EMAIL_PASSWORD_FILENAME,
                               EMAIL_SENDING_LOG,
                               CURRENT_MODULE_DIRECTORY)
