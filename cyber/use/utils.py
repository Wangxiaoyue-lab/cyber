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
def report_yaml_update(cyber_yaml,task_path)
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
    report_path = os.path.join(task_path,report_name,"report.yaml")
    with open(report_path, 'r') as f:
        report = yaml.safe_load(f)
    
    # Updates the Date field in the report.yaml file.
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
 
    with open(report_path, 'w') as f:
        yaml.dump(report)    