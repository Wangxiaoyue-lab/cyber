import os
import argparse


def start_cyber(project_path):
    if not os.path.exists(path):
        os.makedirs(path)

    file_path = os.path.join(path, 'cyber.yaml')
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write('Setting: \n  Location: \n  Laboratory: \n  Operator: \n  Platform: \n\nConfig: \n  input: \n  script: \n  output: \n  report: \n  path_wkthmltopdf: \n  fastchat:')

def main():
    parser = argparse.ArgumentParser(description='Formalize the cyber yaml')
    parser.add_argument('project_path', type=str, help='Path to the project folder')
    args = parser.parse_args()
    task_path = args.project_path
    start_cyber(project_path)

if(__name__=="__main__"):
    main()