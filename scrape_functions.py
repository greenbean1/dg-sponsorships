"""
This module contains functions relevant to web scraping using BeautifulSoup
"""

from bs4 import BeautifulSoup
from typing import Dict, List
import urllib.request

import csv_functions


# Takes URL and returns a BeautifulSoup object
def _get_html_soup(url: str) -> BeautifulSoup:
    with urllib.request.urlopen(url) as response:
        html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup


# Sample td tag: <td class="column-1">Chris Dickerson</td>
def _get_text_from_td_tag(td: str) -> str:
    start = td.find(">") + 1
    end = td.find("/") - 1
    return td[start:end]


def _soup_to_table_body(soup: BeautifulSoup):
    # Get the only table in the HTML (FRAIL LOGIC)
    table_all = soup.table
    # Get the table body (has relevant information)
    return table_all.contents[3]


def _table_body_to_dict(table_body) -> Dict[int, List[str]]:
    size_of_table = len(table_body.contents)
    dg_info_dict = {}
    for x in range(1, size_of_table):
        if x % 2 != 0:
            player_info_list = []
            row = table_body.contents[x]
            # List of table cells (tds)
            cells = row.find_all('td')
            num_col = len(cells)
            # Could extend loop to include final cell to get article link (would need to be able to extract URL)
            for y in range(0, num_col - 1):
                cell_info = _get_text_from_td_tag(str(cells[y]))
                player_info_list.append(cell_info)
            dg_info_dict[x // 2 + 1] = player_info_list
    print(dg_info_dict)
    return dg_info_dict


# The only thing that really matters!
def get_dict_from_url(url: str,
                      log_filename: str,
                      log_directory: str) -> Dict[int, List[str]]:
    soup = _get_html_soup(url)
    csv_functions.log_timestamp(log_filename, log_directory)
    table_body = _soup_to_table_body(soup)
    return _table_body_to_dict(table_body)
