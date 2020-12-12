import csv
from os import path
from datetime import datetime


def log_timestamp(log_filename, log_directory):
    log_path = path.join(log_directory, log_filename)
    with open(log_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        date_time_obj = datetime.now()
        now_info = [date_time_obj.date(), date_time_obj.replace(microsecond=0)]
        writer.writerow(now_info)


def file_exists(filename, path_directory):
    return path.exists(path.join(path_directory, filename))


def write_to_primary_dg_csv(dg_dict, dg_csv_filename, dg_csv_directory):
    dg_csv_path = path.join(dg_csv_directory, dg_csv_filename)
    # if not path.exists(CSV_FILENAME):
    field_names = ['Player', 'Type', '2020 Sponsor', '2021 Sponsor', 'Terms']
    with open(dg_csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(field_names)
        for value in dg_dict.values():
            # print(value)
            writer.writerow(list(value))
#     print('Looks like the CSV had been there')
# else:
#     print('The CSV already exists buddy')


def get_incremental_names(dg_dict, dg_csv_filename, dg_csv_directory):
    dg_csv_path = path.join(dg_csv_directory, dg_csv_filename)
    current_num_players = len(dg_dict)
    with open(dg_csv_path) as csv_file:
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
            write_to_primary_dg_csv(dg_dict, dg_csv_filename, dg_csv_directory)
            return incremental_names
