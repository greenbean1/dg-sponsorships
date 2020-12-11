"""
Process:
1) Scrape info on disc golf players who have confirmed new sponsorships for 2021 (and perhaps beyond)
2) Save info into a dictionary
2a) If CSV is empty, write dictionary into CSV
3) If there is more info in the dictionary than CSV, email me the incremental info
4) Use Windows Task Scheduler to run daily at 9:05am
"""

# Modules to write
import scrape_functions
import csv_functions
# import email_functions

DISC_GOLF_ARTICLE_URL = 'https://discgolf.ultiworld.com/2020/11/02/2021-player-sponsorship-tracker/'

# Scrape disc golf article into dg_dict
dg_dict = scrape_functions.get_data(DISC_GOLF_ARTICLE_URL)
# Write dg_dict into CSV (only if CSV does not exist)
if not csv_functions.csv_dg_info_exists():
    csv_functions.write_to_csv(dg_dict)
incremental_names = csv_functions.get_incremental_names(dg_dict)
# # If there is actually any incremental info, email me the info
# if len(incremental_names) != 0:
#     email_functions.send_email(incremental_names, DISC_GOLF_ARTICLE_URL)  # have this function log timestamp of emailing
