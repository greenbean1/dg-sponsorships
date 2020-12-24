import csv
from datetime import datetime
from os import path
from typing import Dict, List, Union


def log_timestamp(log_filename: str, log_directory: str) -> None:  # Type Hints IDE checks file parameter data types
    log_path = path.join(log_directory, log_filename)
    with open(log_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        date_time_obj = datetime.now()
        now_info = [date_time_obj.date(), date_time_obj.replace(microsecond=0)]
        writer.writerow(now_info)


def file_exists(filename: str, path_directory: str) -> bool:
    return path.exists(path.join(path_directory, filename))


def write_to_primary_dg_csv(dg_dict: Dict[int, List[str]], dg_csv_filename: str, dg_csv_directory: str) -> None:
    # Writes current run's dictionary to CSV
    dg_csv_path = path.join(dg_csv_directory, dg_csv_filename)
    field_names = ['Player', 'Type', '2020 Sponsor', '2021 Sponsor', 'Terms']
    with open(dg_csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(field_names)
        for value in dg_dict.values():
            writer.writerow(list(value))


def get_incremental_names(dg_dict: Dict[int, List[str]],
                          dg_csv_filename: str,
                          dg_csv_directory: str) -> Union[None, List[str]]:
    # Check if current website dict info has more info than CSV which has prior run info
    # If more on current website, add the incremental info to the CSV
    dg_csv_path = path.join(dg_csv_directory, dg_csv_filename)
    current_num_players = len(dg_dict)
    with open(dg_csv_path) as csv_file:
        prior_csv_num_players = len(csv_file.readlines()) - 1  # -1 because len function includes header
        if prior_csv_num_players == current_num_players:
            print('The number of players in the CSV matches the website')  # Refactor with custom "debug" function
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
