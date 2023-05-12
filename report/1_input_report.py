import os
import hashlib
from datetime import datetime
import yaml

def get_sha256(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Y', suffix)

def print_supplemental_info(name, supplemental_info):
    if name in supplemental_info:
        info = supplemental_info[name]
        print(f"Description: {info.get('Description', '')}")
        print(f"Source: {info.get('Source', '')}")
        print()

def get_info(path):
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

get_info('/public/home/caojun/module_script/for_git/cyber/project_demo/project1/1_task_analysis/input')


 