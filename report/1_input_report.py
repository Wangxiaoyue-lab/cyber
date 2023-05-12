import os
import hashlib
from datetime import datetime

def get_sha256(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def get_info(path):
    for root, dirs, files in os.walk(path):
        for name in dirs:
            dir_path = os.path.join(root, name)
            if os.path.islink(dir_path):
                stat = os.lstat(dir_path)
                print(f"Link: {name}")
                print(f"Path: {dir_path}")
                print(f"Creation time: {datetime.fromtimestamp(stat.st_ctime)}")
                print(f"Reference: {os.readlink(dir_path)}")
                print()
            else:
                stat = os.stat(dir_path)
                print(f"Directory: {name}")
                print(f"Path: {dir_path}")
                print(f"Creation time: {datetime.fromtimestamp(stat.st_ctime)}")
                print(f"Number of files: {len(os.listdir(dir_path))}")
                print()
        for name in files:
            file_path = os.path.join(root, name)
            if os.path.islink(file_path):
                stat = os.lstat(file_path)
                print(f"Link: {name}")
                print(f"Path: {file_path}")
                print(f"Creation time: {datetime.fromtimestamp(stat.st_ctime)}")
                print(f"Reference: {os.readlink(file_path)}")
                print()
            else:
                stat = os.stat(file_path)
                print(f"File: {name}")
                print(f"Path: {file_path}")
                print(f"Creation time: {datetime.fromtimestamp(stat.st_ctime)}")
                print(f"Size: {stat.st_size} bytes")
                print(f"SHA256: {get_sha256(file_path)}")
                print()

get_info('/path/to/directory')