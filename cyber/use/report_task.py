import os
import yaml
import argparse
from datetime import datetime
import pandas as pd

import .utils
import .style
from .style import style_dir
from ..report._7_date_report import get_dates
from ..report._1_input_report import get_files_info
from ..report._5_script_report import get_script_info
from ..report._8_tree import generate_file_tree,visualize_file_tree
from ..report._9_pictures import find_images,convert_image,add_watermark,
from ..report._10_table_report import get_tables_info
from ..report._13_supplement import filter_supplement,generate_supplement_div


script_name = 'script'
input_name = 'input'
output_name = 'output'
report_name = 'report'
picture_name = 'picture'
table_name = 'table'
store_name = 'store'
Supplement_name = 'Supplement'


#def generate_html(df, class_name, style):
#    html_div = df_to_div(df, class_name)
#    html = f"""
#        <!DOCTYPE html>
#        <html>
#        <head>
#            {style}
#        </head>
#        <body>
#            {html_div}
#        </body>
#        </html>
#    """
#    return html


def report_generate(cyber_yaml,task_path,style_dir):
    #获得自定义变量名
    custom = check_dir_name(cyber_yaml)
    input_name = custom['input']
    report_name = custom['report']
    output_name = custom['output']
    script_name = custom['script']

    #读取report.yaml
    report_path = os.path.join(task_path,report_name)
    report_yaml_path = os.path.join(report_path,"report.yaml")
    with open(report_path, 'r') as f:
        report = yaml.safe_load(f)
    
    #获得当天日期
    today = datetime.now()
    formatted_today = today.strftime('%Y-%m-%d')
    div_date = f"<div class='date'>{formatted_today}</div>"
    style_date = style_dir['style_date']

    #产生输入文件的表格
    input_path = os.path.join(task_path,input_name)
    input_df = get_files_info(input_path)
    div_input = df_to_div(input_df,"input-table")
    style_input = style_dir['style_input']

    #读取script文件夹下文件产生脚本表格
    script_path = os.path.join(task_path,script_name)
    script_df = get_script_info(script_path)
    div_script = df_to_div(script_df,"script-table")
    style_script = style_dir['style_script']

    #脚本解释

    #读取report文件夹下的loading_packages_*.txt文件
    loading_path = os.path.join(task_path,report_name)
    loading = get_files_with_prefix(loading_path,"loading_")

    #读取output文件夹生成文件树的pdf文件
    output_path = os.path.join(task_path,output_name)
    tree = generate_file_tree(output_path)
    graph, _= visualize_file_tree(tree)
    tree_store = os.path.join(report_path,'output_tree')
    graph.render(tree_store, view=False)

    #读取output下picture文件夹生成预览图
    picture_path = os.path.join(output_path,'picture')
    image_paths = find_images(picture_path)
    whole_width = 800
    processed_images = []
    image_name_list = []
    for image_path in image_paths:
        images = convert_image(image_path, whole_width)
        for image in images:
            image_name = os.path.basename(image_path)
            image_name_list.append(image_name)
            date = datetime.now().date()
            image = add_watermark(image, image_name, date)
            processed_images.append(image)
    

    #读取output下table文件夹生成预览
    table_path = os.path.join(output_path,'table')
    tables = get_tables_info(table_path)
    div_tables
    style_tables

    #读取output下store文件夹生成表格
    store_path = os.path.join(output_path,'store')
    store_df = get_files_info(store_path)
    div_store
    style_store

    #读取report.yaml里supplement部分
    raw_data = report['Supplement']
    filtered_data = filter_supplement(raw_data)
    div_supplement = generate_supplement_div(filtered_data)

    #在report文件夹下生成html文件

    #html文件里添加图片

    #html文件转为pdf文件

    #删除中间文件





def main():
    parser = argparse.ArgumentParser(description='Formalize the task folder to adapt cyber')
    parser.add_argument('task_path', type=str, help='Path to the task folder')
    args = parser.parse_args()
    task_path = args.task_path



if __name__ == '__main__':
    main()