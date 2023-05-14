import os
import sys
import session_info
import argparse

def save_session_info(folder_path):
    report_folder = os.path.join(folder_path, 'report')
    if not os.path.exists(report_folder):
        os.makedirs(report_folder)
    file_name = os.path.join(report_folder, 'loading_Python_packages.txt')
    original_stdout = sys.stdout
    with open(file_name, 'w') as f:
        sys.stdout = f
        session_info.show()
        sys.stdout = original_stdout

def main():
    parser = argparse.ArgumentParser(description='Save session info')
    parser.add_argument('--folder_path', type=str, required=True, help='Path to the folder to save session info')
    args = parser.parse_args()
    save_session_info(args.folder_path)

if __name__ == '__main__':
    main()
#import pkg_resources
#import os

#def cyber_log(folder_path):
#    loaded_modules = [(d.project_name, d.version) for d in pkg_resources.working_set]
#    with open(os.path.join(folder_path, 'loaded_modules.txt'), 'w') as f:
#        for module in loaded_modulSes:
#            f.write(f'{module[0]}: {module[1]}\n')