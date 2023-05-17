import os
import argparse

from .utils import check_dir_name


custom = check_dir_name(cyber_yaml)
input_name = custom['input']
report_name = custom['report']
output_name = custom['output']
script_name = custom['script']
picture_name = 'picture'
table_name = 'table'
store_name = 'store'
#Supplement_name = 'Supplement'

def create_folder_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_description_if_not_exists(path):
    file_path = os.path.join(path, 'description.yaml')
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write('- Name: \n  Description: \n  Source: \n')

def create_report_if_not_exists(path):
    file_path = os.path.join(path, 'report.yaml')
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write('Pre-report: \n  Type: \n  Title: \n  Aim: \n  Date: \n  Location: \n  Laboratory: \n  Operator: \n  Platform: \n\nSupplement: \n  - Name: \n      Path: \n      Details: \n  - Name: \n      Path: \n      Details: \n  - Name: \n      Path: \n      Details: \n\nPost-report: \n  Discussion: \n  Plan: ')

def cyber_task(task_path,script_name,input_name,output_name,report_name,picture_name,table_name,store_name):
    script_path = os.path.join(task_path,script_name)
    create_folder_if_not_exists(script_path)
    input_path = os.path.join(task_path,input_name)
    create_folder_if_not_exists(input_path)
    output_path = os.path.join(task_path,output_name)
    create_folder_if_not_exists(output_path)
    report_path = os.path.join(task_path,report_name)
    create_folder_if_not_exists(report_path)
    picture_path = os.path.join(output_path,picture_name)
    create_folder_if_not_exists(picture_path)
    table_path = os.path.join(output_path,table_name)
    create_folder_if_not_exists(table_path)
    store_path = os.path.join(output_path,store_name)
    create_folder_if_not_exists(store_path)
    #Supplement_path = os.path.join(output_path,Supplement_name)
    #create_folder_if_not_exists(Supplement_path)
    
    create_description_if_not_exists(input_path)
    create_report_if_not_exists(report_path)

def main():
    parser = argparse.ArgumentParser(description='Formalize the task folder to adapt cyber')
    parser.add_argument('task_path', type=str, help='Path to the task folder')
    args = parser.parse_args()
    task_path = args.task_path
    cyber_task(task_path,script_name,input_name,output_name,report_name,picture_name,table_name,store_name,Supplement_name)

if __name__ == '__main__':
    main()