# Disc Golf Sponsorships
This project sends email notifications if there is "new" news on professional disc golf players signing contracts with sponsors.

## Motivation
1. After regularly checking a website to see if there was news on players' sponsorships, I wanted to be told when there was news.
2. This appeared to be a great project to practice my data hacking skills

## How Does This Work?
1. Scrape the [sponsorship website's](https://discgolf.ultiworld.com/2020/11/02/2021-player-sponsorship-tracker/) player sponsorship information via [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library.
2. If there is no pre-existing CSV, save scraped info to a CSV on my local machine
3. Get the list (if any) of newly sponsored players (new on the website relative to the CSV)
4. If there are any newly sponsored players, email me (or whoever I specify) via [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol#:~:text=The%20Simple%20Mail%20Transfer%20Protocol,protocol%20for%20electronic%20mail%20transmission.)
5. In order for this code to deliver the intended benefit, it must be run periodically. I set this up locally via [Windows Task Scheduler](http://theautomatic.net/2017/10/03/running-python-task-scheduler/)

## Repository Organization
- Main calls functions relating the main logical components of the process & contains constants relating to file names
- Modules containing functions for each of [scraping](https://github.com/greenbean1/dg-sponsorships/blob/main/scrape_functions.py), [csv management](https://github.com/greenbean1/dg-sponsorships/blob/main/csv_functions.py) & [emailing](https://github.com/greenbean1/dg-sponsorships/blob/main/email_functions.py)

## Credits
Thank you, Nathan Hoover and Jan Van Bruggen for your guidance on this project!

## Misc Resources
 - [Markdown](https://www.markdownguide.org/cheat-sheet/)
 - [Python Style Guide](https://www.python.org/dev/peps/pep-0008/)
