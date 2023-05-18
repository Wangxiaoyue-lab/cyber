import os
import sys
import argparse
import session_info


def cyber_packages(task_path):
    report_folder = os.path.join(task_path, 'report')
    if not os.path.exists(report_folder):
        os.makedirs(report_folder)
    file_name = os.path.join(report_folder, 'loading_packages_Python.txt')
    original_stdout = sys.stdout
    with open(file_name, 'w') as f:
        sys.stdout = f
        session_info.show()
        sys.stdout = original_stdout

def main():
    parser = argparse.ArgumentParser(description='Save session info')
    parser.add_argument('--task_path', type=str, required=True, help='Path to the task to save session info')
    args = parser.parse_args()
    cyber_packages(args.folder_path)

if __name__ == '__main__':
    main()