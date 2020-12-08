"""
Purpose:
1) Scrap an article to get info on disc golf players who have confirmed new sponsorship deals for 2021
    and perhaps beyond
2) Save info into a dictionary
3) Write dictionary's info into a CSV

Modules
- Main
++ Get data method (returns dict)
++ CSV stuff
++ Email module
- Module for scraping/HTML
-
Notes
-Keep log file every run
-Code runs each hour/4x per day but sends email only once each day (if changes)
"""

DISC_GOLF_ARTICLE_URL = 'https://discgolf.ultiworld.com/2020/11/02/2021-player-sponsorship-tracker/'
