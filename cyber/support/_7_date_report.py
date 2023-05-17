import os
import datetime
import sys
import argparse

def get_dates(folder_path):
    earliest_date = datetime.datetime.now()
    latest_date = datetime.datetime(1970, 1, 1)

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        file_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        if file_time < earliest_date:
            earliest_date = file_time
        if file_time > latest_date:
            latest_date = file_time

    earliest_date_str = earliest_date.strftime('%Y-%m-%d')
    latest_date_str = latest_date.strftime('%Y-%m-%d')
    return f'Earliest date: {earliest_date_str}, Latest date: {latest_date_str}'

def main():
    parser = argparse.ArgumentParser(description='Get script info')
    parser.add_argument('folder_path', type=str, help='Path to the folder containing scripts')
    parser.add_argument('output', type=str, help='Path to the output HTML file')
    args = parser.parse_args()
    dates_str = get_dates(args.folder_path)
    with open(args.output, 'w') as f:
        f.write(dates_str)

if __name__ == '__main__':
    main()
