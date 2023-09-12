import os
import zipfile
import yaml

from cyber_py.support._7_date_report import get_dates

# 数据框生成div块
def df_to_div(df, class_name):
    """ 
    This function takes a dataframe and a class name as arguments and returns an html div 
    containing the data from the dataframe. The div will have the class name specified 
    as the argument. 
    """
    html_table = df.to_html()
    html_div = f'<div class="{class_name}">{html_table}</div>'
    return html_div    

# 列表生成div块
def list_to_div(contents, class_name):
    """ 
    This function takes in a list of contents and a string containing the class 
    name and creates a div containing the contents of the list as well as the class 
    name provided. It returns the div as a string. 
    """
    div = f'<div class="{class_name}">'
    for content in contents:
        div += f'<p>{content}</p >'
    div += '</div>'
    return div

# 根据cyber.yaml文件提取设定好的文件夹命名
def check_dir_name(cyber_yaml):
    """ 
    This function checks for the provided cyber.yaml file and retrieves the name of the 
    input, output, report, and script directories 
    
    Parameters: 
        cyber_yaml (str): The path to the cyber.yaml file 
    
    Returns: 
        dict: A dictionary containing the name of the input, output, report, and script 
        directories 
    """ 
    cyber_file = os.path.basename(cyber_yaml)
    if cyber_file != 'cyber.yaml':
        return ValueError('Please provide the valid cyber.yaml!')
    with open(cyber_yaml, 'r') as f:
        cyber = yaml.safe_load(f)
    
    input_name = "input" if not cyber['Config']['input'] else cyber['Config']['input']
    report_name = "report" if not cyber['Config']['report'] else cyber['Config']['report']
    output_name = "output" if not cyber['Config']['output'] else cyber['Config']['output']
    script_name = "script" if not cyber['Config']['script'] else cyber['Config']['script']
    return {'input':input_name,'report':report_name,'output':output_name,'script':script_name}


# 根据cyber.yaml更新report.yaml
def report_yaml_update(cyber_yaml,task_path):
    """
    Updates the report.yaml file with the relevant information from the cyber.yaml file.

    Args:
        cyber_yaml (str): The file path to the cyber.yaml file.
        task_path (str): The path to the task directory.

    Returns:
        None

    Raises:
        ValueError: If the `cyber.yaml` file is not valid.
    """
    # Loads the cyber.yaml file
    cyber_file = os.path.basename(cyber_yaml)
    if cyber_file != 'cyber.yaml':
        return ValueError('Please provide the valid cyber.yaml!')
    with open(cyber_yaml, 'r') as f:
        cyber = yaml.safe_load(f)

    # Loads the report.yaml file
    report_name = check_dir_name(cyber_yaml)['report']
    report_path = os.path.join(task_path,report_name,"report.yaml")
    with open(report_path, 'r') as f:
        report = yaml.safe_load(f)
    
    # Updates the Date field in the report.yaml file.
    script_name = check_dir_name(cyber_yaml)['script']
    script_path = os.path.join(task_path,script_name)
    dates_str = get_dates(script_path)
    report['Pre-report']['Date'] = dates_str

    # Updates the fields in the Pre-report section of the report.yaml 
    # file with information from the cyber.yaml file
    Title = report['Pre-report']['Title']
    Aim = Title if not report['Pre-report']['Aim'] else report['Pre-report']['Aim']
    report['Pre-report']['Aim'] = Aim
    report['Pre-report']['Location'] = cyber['Setting']['Location'] if not report['Pre-report']['Location'] else report['Pre-report']['Location']
    report['Pre-report']['Laboratory'] = cyber['Setting']['Laboratory'] if not report['Pre-report']['Laboratory'] else report['Pre-report']['Laboratory']
    report['Pre-report']['Operator'] = cyber['Setting']['Operator'] if not report['Pre-report']['Operator'] else report['Pre-report']['Operator']
    report['Pre-report']['Platform'] = cyber['Setting']['Platform'] if not report['Pre-report']['Platform'] else report['Pre-report']['Platform']
    try:
        with open(report_path, 'w') as f:
            yaml.dump(report, f)
    except Exception as e:
        print(f"Error writing to file: {e}")
    #with open(report_path, 'w') as f:
    #    yaml.dump(report)


#压缩文件为zip
def zip_files(folder_path, zip_file_name='archive.zip'):
    zip_file_path = os.path.join(folder_path, zip_file_name)
    html_found = False
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file == 'output_tree_0.png' or file == 'report.yaml' or (file.startswith('Report_the_task_') and (file.endswith('.html') or file.endswith('.pdf'))):
                    if file.endswith('.html'):
                        html_found = True
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))
            if 'px_images' in dirs:
                px_images_folder = os.path.join(root, 'px_images')
                for root2, dirs2, files2 in os.walk(px_images_folder):
                    for file2 in files2:
                        file_path2 = os.path.join(root2, file2)
                        zipf.write(file_path2, os.path.relpath(file_path2, folder_path))
    if not html_found:
        print('Error: No HTML file starting with Report_the_task_ found')
        return
    print(f'Files zipped to {zip_file_path}')