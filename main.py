"""
Process:
1) Scrape info on disc golf players who have confirmed new sponsorships for 2021 (and perhaps beyond)
2) Save info into a dictionary
2a) If CSV is empty, write dictionary into CSV
3) If there is more info in the dictionary than CSV, email me the incremental info
4) Use Windows Task Scheduler to run daily at 9:05am
"""

# print('hello world')

# Modules to write
import os
import scrape_functions
import csv_functions
import email_functions

DISC_GOLF_ARTICLE_URL = 'https://discgolf.ultiworld.com/2020/11/02/2021-player-sponsorship-tracker/'
PRIMARY_DG_CSV_FILENAME = 'disc_golf_info.csv'
EMAIL_PASSWORD_FILENAME = 'email_info.txt'
EMAIL_SENDING_LOG = 'emailing_log.csv'
SCRAPING_LOG = 'scraping_log.csv'
CURRENT_MODULE_PATH = os.path.abspath(__file__)
CURRENT_MODULE_DIRECTORY = os.path.dirname(CURRENT_MODULE_PATH)


# Scrape disc golf article into dg_dict
dg_dict = scrape_functions.get_dict_from_url(DISC_GOLF_ARTICLE_URL, SCRAPING_LOG, CURRENT_MODULE_DIRECTORY)
# Write dg_dict into CSV (only if CSV does not exist)
if not csv_functions.file_exists(PRIMARY_DG_CSV_FILENAME, CURRENT_MODULE_DIRECTORY):
    csv_functions.write_to_primary_dg_csv(dg_dict, PRIMARY_DG_CSV_FILENAME, CURRENT_MODULE_DIRECTORY)
incremental_names = csv_functions.get_incremental_names(dg_dict, PRIMARY_DG_CSV_FILENAME, CURRENT_MODULE_DIRECTORY)
if incremental_names:
    email_functions.send_email(incremental_names, DISC_GOLF_ARTICLE_URL, EMAIL_PASSWORD_FILENAME, EMAIL_SENDING_LOG, CURRENT_MODULE_DIRECTORY)
