"""
This module contains constants used throughout this project
"""

import constants as c
import csv_functions
import email_functions
import scrape_functions


dg_dict = scrape_functions.get_dict_from_url(c.DISC_GOLF_ARTICLE_URL, c.SCRAPING_LOG, c.CURRENT_MODULE_DIRECTORY)
if not csv_functions.file_exists(c.PRIMARY_DG_CSV_FILENAME, c.CURRENT_MODULE_DIRECTORY):
    csv_functions.write_to_primary_dg_csv(dg_dict, c.PRIMARY_DG_CSV_FILENAME, c.CURRENT_MODULE_DIRECTORY)
incremental_names = csv_functions.get_incremental_names(dg_dict, c.PRIMARY_DG_CSV_FILENAME, c.CURRENT_MODULE_DIRECTORY)
if incremental_names:
    email_functions.send_email(incremental_names,
                               c.DISC_GOLF_ARTICLE_URL,
                               c.EMAIL_PASSWORD_FILENAME,
                               c.EMAIL_SENDING_LOG,
                               c.CURRENT_MODULE_DIRECTORY)
