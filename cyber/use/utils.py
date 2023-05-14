def get_files_with_prefix(folder_path, prefix):
    files = os.listdir(folder_path)
    result = [file for file in files if file.startswith(prefix) and file.endswith('.txt')]
    if not result:
        result.append('Unknown')

    return result

def df_to_div(df, class_name):
    html_table = df.to_html()
    html_div = f'<div class="{class_name}">{html_table}</div>'
    return html_div    

def check_dir_name(cyber_yaml):
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



def report_yaml_update(cyber_yaml,task_path)
    #读取cyber.yaml文件
    cyber_file = os.path.basename(cyber_yaml)
    if cyber_file != 'cyber.yaml':
        return ValueError('Please provide the valid cyber.yaml!')
    with open(cyber_yaml, 'r') as f:
        cyber = yaml.safe_load(f)

    #读取report.yaml文件
    report_path = os.path.join(task_path,report_name,"report.yaml")
    with open(report_path, 'r') as f:
        report = yaml.safe_load(f)
    
    #获得task的日期区间
    script_path = os.path.join(task_path,script_name)
    dates_str = get_dates(script_path)
    report['Pre-report']['Date'] = dates_str

    #根据cyber更新report
    Title = report['Pre-report']['Title']
    Aim = Title if not report['Pre-report']['Aim'] else report['Pre-report']['Aim']
    report['Pre-report']['Aim'] = Aim
    report['Pre-report']['Location'] = cyber['Setting']['Location'] if not report['Pre-report']['Location'] else report['Pre-report']['Location']
    report['Pre-report']['Laboratory'] = cyber['Setting']['Laboratory'] if not report['Pre-report']['Laboratory'] else report['Pre-report']['Laboratory']
    report['Pre-report']['Operator'] = cyber['Setting']['Operator'] if not report['Pre-report']['Operator'] else report['Pre-report']['Operator']
    report['Pre-report']['Platform'] = cyber['Setting']['Platform'] if not report['Pre-report']['Platform'] else report['Pre-report']['Platform']
 
    with open(report_path, 'w') as f:
        yaml.dump(report)    