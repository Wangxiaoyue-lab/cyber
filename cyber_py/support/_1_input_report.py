import os
import argparse
import hashlib
from datetime import datetime
import yaml
import pandas as pd


def get_file_sha256(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def get_dir_sha256(dir_path):
    sha256 = hashlib.sha256()
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            file_path = os.path.join(root, name)
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as f:
                    while True:
                        data = f.read(65536)
                        if not data:
                            break
                        sha256.update(data)
    return sha256.hexdigest()

def get_sha256(path):
    if os.path.isfile(path):
        return get_file_sha256(path)
    elif os.path.isdir(path):
        return get_dir_sha256(path)

def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Y', suffix)

def get_input_info(path):
    yaml_file = os.path.join(path, 'description.yaml')
    with open(yaml_file, 'r') as f:
        yaml_data = yaml.safe_load(f)

    supplemental_info = {}
    for item in yaml_data:
        name = item['Name']
        supplemental_info[name] = item

    data = []
    for name in os.listdir(path):
        if name == 'description.yaml':
            continue

        entry_path = os.path.join(path, name)
        if os.path.isdir(entry_path):
            if os.path.islink(entry_path):
                stat = os.lstat(entry_path)
                data.append({
                    'Name': name,
                    'Type': 'Link',
                    'Path': entry_path,
                    'Creation time': datetime.fromtimestamp(stat.st_ctime),
                    'Details': f"ref {os.readlink(entry_path)}",
                    'SHA256': get_sha256(os.readlink(entry_path)),
                    'Description': supplemental_info.get(name, {}).get('Description', ''),
                    'Source': supplemental_info.get(name, {}).get('Source', '')
                })
            else:
                stat = os.stat(entry_path)
                data.append({
                    'Name': name,
                    'Type': 'Directory',
                    'Path': entry_path,
                    'Creation time': datetime.fromtimestamp(stat.st_ctime),
                    'Details': f"counts {len(os.listdir(entry_path))}",
                    'SHA256': get_sha256(entry_path),
                    'Description': supplemental_info.get(name, {}).get('Description', ''),
                    'Source': supplemental_info.get(name, {}).get('Source', '')
                })
        elif os.path.isfile(entry_path):
            if os.path.islink(entry_path):
                stat = os.lstat(entry_path)
                data.append({
                    'Name': name,
                    'Type': 'Link',
                    'Path': entry_path,
                    'Creation time': datetime.fromtimestamp(stat.st_ctime),
                    'Details': f"ref {os.readlink(entry_path)}",
                    'SHA256': get_sha256(os.readlink(entry_path)),
                    'Description': supplemental_info.get(name, {}).get('Description', ''),
                    'Source': supplemental_info.get(name, {}).get('Source', '')
                })
            else:
                stat = os.stat(entry_path)
                data.append({
                    'Name': name,
                    'Type': 'File',
                    'Path': entry_path,
                    'Creation time': datetime.fromtimestamp(stat.st_ctime),
                    'Details': f"size {sizeof_fmt(stat.st_size)}",
                    'SHA256': get_sha256(entry_path),
                    'Description': supplemental_info.get(name, {}).get('Description', ''),
                    'Source': supplemental_info.get(name, {}).get('Source', '')
                })

    df = pd.DataFrame(data)
    return df

def get_files_info(path):
    data = []
    for name in os.listdir(path):
        entry_path = os.path.join(path, name)
        if os.path.isdir(entry_path):
            if os.path.islink(entry_path):
                stat = os.lstat(entry_path)
                data.append({
                    'Name': name,
                    'Type': 'Link',
                    'Path': entry_path,
                    'Creation time': datetime.fromtimestamp(stat.st_ctime),
                    'Details': f"ref {os.readlink(entry_path)}",
                    'SHA256': get_sha256(os.readlink(entry_path)),
                })
            else:
                stat = os.stat(entry_path)
                data.append({
                    'Name': name,
                    'Type': 'Directory',
                    'Path': entry_path,
                    'Creation time': datetime.fromtimestamp(stat.st_ctime),
                    'Details': f"counts {len(os.listdir(entry_path))}",
                    'SHA256': get_sha256(entry_path),
                })
        elif os.path.isfile(entry_path):
            if os.path.islink(entry_path):
                stat = os.lstat(entry_path)
                data.append({
                    'Name': name,
                    'Type': 'Link',
                    'Path': entry_path,
                    'Creation time': datetime.fromtimestamp(stat.st_ctime),
                    'Details': f"ref {os.readlink(entry_path)}",
                    'SHA256': get_sha256(os.readlink(entry_path)),
                })
            else:
                stat = os.stat(entry_path)
                data.append({
                    'Name': name,
                    'Type': 'File',
                    'Path': entry_path,
                    'Creation time': datetime.fromtimestamp(stat.st_ctime),
                    'Details': f"size {sizeof_fmt(stat.st_size)}",
                    'SHA256': get_sha256(entry_path),
                })

    df = pd.DataFrame(data)
    return df

def print_supplemental_info(name, supplemental_info):
    if name in supplemental_info:
        info = supplemental_info[name]
        print(f"Description: {info.get('Description', '')}")
        print(f"Source: {info.get('Source', '')}")
        print()

def print_info(path):
    yaml_file = os.path.join(path, 'description.yaml')
    with open(yaml_file, 'r') as f:
        yaml_data = yaml.safe_load(f)

    supplemental_info = {}
    for item in yaml_data:
        name = item['Name']
        supplemental_info[name] = item

    for name in os.listdir(path):
        if name == 'description.yaml':
            continue

        entry_path = os.path.join(path, name)
        if os.path.isdir(entry_path):
            if os.path.islink(entry_path):
                stat = os.lstat(entry_path)
                print(f"Name: {name}")
                print(f"Type: Link")
                print(f"Path: {entry_path}")
                print(f"Creation time: {datetime.fromtimestamp(stat.st_ctime)}")
                print(f"Details: ref {os.readlink(entry_path)}")
                print(f"SHA256: {get_sha256(os.readlink(entry_path))}")
                print_supplemental_info(name, supplemental_info)
            else:
                stat = os.stat(entry_path)
                print(f"Name: {name}")
                print(f"Type: Directory")
                print(f"Path: {entry_path}")
                print(f"Creation time: {datetime.fromtimestamp(stat.st_ctime)}")
                print(f"Details: counts {len(os.listdir(entry_path))}")
                print(f"SHA256: {get_sha256(entry_path)}")
                print_supplemental_info(name, supplemental_info)
        elif os.path.isfile(entry_path):
            if os.path.islink(entry_path):
                stat = os.lstat(entry_path)
                print(f"Name: {name}")
                print(f"Type: Link")
                print(f"Path: {entry_path}")
                print(f"Creation time: {datetime.fromtimestamp(stat.st_ctime)}")
                print(f"Details: ref {os.readlink(entry_path)}")
                print(f"SHA256: {get_sha256(os.readlink(entry_path))}")
                print_supplemental_info(name, supplemental_info)
            else:
                stat = os.stat(entry_path)
                print(f"Name: {name}")
                print(f"Type: File")
                print(f"Path: {entry_path}")
                print(f"Creation time: {datetime.fromtimestamp(stat.st_ctime)}")
                print(f"Details: size {sizeof_fmt(stat.st_size)}")
                print(f"SHA256: {get_sha256(entry_path)}")
                print_supplemental_info(name, supplemental_info)

def main():
    parser = argparse.ArgumentParser(description='Get info about a directory.')
    parser.add_argument('path', type=str, help='Path to the directory')
    parser.add_argument('output', type=str, help='Path to the output HTML file')
    args = parser.parse_args()

    df = get_input_info(args.path)
    html_table = df.to_html()

    with open(args.output, 'w') as f:
        f.write("""
        <style>
            table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
            }
            th {
                text-align: center;
                background-color: green;
                color:white;
            }
            td {
                padding: 5px;
                text-align: left;
                max-width: 180px;
                word-wrap: break-word;
                background-color: lightyellow;
            }
        </style>
        """)
        f.write(html_table)

if __name__ == '__main__':
    main()