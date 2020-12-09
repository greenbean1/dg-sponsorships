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
import email_functions

DISC_GOLF_ARTICLE_URL = 'https://discgolf.ultiworld.com/2020/11/02/2021-player-sponsorship-tracker/'

# Scrape disc golf article into dg_dict
dg_dict = scrape_functions.get_data() # have this function log timestamp of scraping
# Write dg_dict into CSV (only if CSV does not exist)
csv_functions.write_to_csv(dg_dict)
# Save incremental article information (incremental relative to the prior existing CSV
incremental_info = csv_functions.dict_incremental_info(dg_dict)
# If there is actually any incremental info, email me the info
if incremental_info is not empty:
    email_functions.send_email() # have this function log timestamp of emailing
