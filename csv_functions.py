import csv
from os import path
from datetime import datetime

CSV_FILENAME = 'disc_golf_info.csv'


def log_timestamp(csv_name):
    with open(csv_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        date_time_obj = datetime.now()
        now_info = [date_time_obj.date(), date_time_obj.replace(microsecond=0)]
        writer.writerow(now_info)


def csv_dg_info_exists():
    return path.exists(CSV_FILENAME)


def write_to_csv(dg_dict):
    # if not path.exists(CSV_FILENAME):
    field_names = ['Player', 'Type', '2020 Sponsor', '2021 Sponsor', 'Terms']
    with open(CSV_FILENAME, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(field_names)
        for value in dg_dict.values():
            # print(value)
            writer.writerow(list(value))
#     print('Looks like the CSV had been empty before')
# else:
#     print('The CSV already exists buddy')


def get_incremental_names(dg_dict):
    current_num_players = len(dg_dict)
    with open(CSV_FILENAME) as csv_file:
        prior_csv_num_players = len(csv_file.readlines()) - 1  # -1 because len function includes header
        if prior_csv_num_players == current_num_players:
            print('The number of players in the CSV matches the website')
        else:
            print('The number of players in the CSV does NOT match the website')
            incremental_dg_info_dict = {key: value for key, value in dg_dict.items() if key > prior_csv_num_players}
            incremental_names = []
            for value in incremental_dg_info_dict.values():
                incremental_names.append(value[0])
            print('Incremental players:')
            print(incremental_names)
            print('Full Incremental Player Info')
            print(incremental_dg_info_dict)
            write_to_csv(dg_dict)
            return incremental_names
