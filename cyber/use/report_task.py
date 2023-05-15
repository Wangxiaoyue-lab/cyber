import os
import yaml
import argparse
from datetime import datetime
import pandas as pd

import .utils
from .style import style_dir
from ..report._7_date_report import get_dates
from ..report._1_input_report import get_files_info
from ..report._5_script_report import get_script_info
from ..report._8_tree import generate_file_tree,visualize_file_tree
from ..report._9_pictures import find_images,convert_image,add_watermark,images_to_div
from ..report._10_table_report import get_tables_info,tables_to_div
from ..report._13_supplement import filter_supplement,generate_supplement_div
from ..report._12_packages import get_txts_with_prefix,read_txts
from ..report._14_report import Pre_report_to_div,Post_report_to_div,report_head

#script_name = 'script'
#input_name = 'input'
#output_name = 'output'
#report_name = 'report'
#picture_name = 'picture'
table_name = 'table'
store_name = 'store'
Supplement_name = 'Supplement'


def generate_html(
    div_date,
    style_date,
    div_head,
    style_head,
    div_Pre_report,
    style_Pre_report,
    div_input,
    style_input,
    div_packages,
    style_packages,
    div_script,
    style_script,
    div_tree,
    style_tree,
    div_pictures,
    style_pictures,
    div_tables,
    style_tables,
    div_store,
    style_store,
    div_supplement,
    style_supplement,
    div_Post_report,
    style_Post_report
    ):
    html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            body { 
                margin: 0; 
                padding: 0; 
                background-color: #D1EED1 
                }
            {style_date}
            {style_head}
            {style_Pre_report}
            {style_input}
            {style_packages}
            {style_script}
            {style_tree}
            {style_pictures}
            {style_tables}
            {style_store}
            {style_supplement}
            {style_Post_report}
        </head>
        <body>
            {div_date}
            {div_head}
            {div_Pre_report}
            {div_input}
            {div_packages}
            {div_script}
            {div_tree}
            {div_pictures}
            {div_tables}
            {div_store}
            {div_supplement}
            {div_Post_report}
        </body>
        </html>
    """



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
    loading_txts_path = get_txts_with_prefix(loading_path,"loading_")
    loading_txts = read_txts(loading_txts_path)
    div_packages = list_to_div(loading_txts,"packages")
    style_packages = style_dir['style_packages']

    #读取output文件夹生成文件树的pdf文件
    output_path = os.path.join(task_path,output_name)
    tree = generate_file_tree(output_path)
    graph, _= visualize_file_tree(tree)
    tree_store = os.path.join(report_path,'output_tree')
    graph.render(tree_store, view=False)
    div_tree = tree_to_div(report_path)
    style_tree = style_dir['style_tree']

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
    
    div_pictures = images_to_div(processed_images, report_path, image_name_list)
    style_pictures = style_dir['style_pictures']

    #读取output下table文件夹生成预览
    table_path = os.path.join(output_path,'table')
    tables = get_tables_info(table_path)
    div_tables = tables_to_div(tables)
    style_tables = style_dir['style_tables']

    #读取output下store文件夹生成表格
    store_path = os.path.join(output_path,'store')
    store_df = get_files_info(store_path)
    div_store = df_to_div(store_df,"store-table")
    style_store = style_dir['style_store']

    #读取report.yaml里supplement部分
    raw_data = report['Supplement']
    filtered_data = filter_supplement(raw_data)
    div_supplement = generate_supplement_div(filtered_data)
    style_supplement = style_dir['style_supplement']
    
    #report.yaml其他部分对应到style
    Pre_report = report['Pre-report']
    div_Pre_report = Pre_report_to_div(Pre_report)
    style_Pre_report = style_dir['style_Pre_report']

    Post_report = report['Post-report']
    div_Post_report = Post_report_to_div(Post_report)
    style_Post_report = style_dir['style_Post_report']

    # html的主题head
    div_head = report_head('WangLab Bioinfomatics Report')
    style_head = style_dir['style_head']

    #在report文件夹下生成html文件
    report_html = generate_html(
        div_date,
        style_date,
        div_head,
        style_head,
        div_Pre_report,
        style_Pre_report,
        div_date,
        style_date,
        div_input,
        style_input,
        div_packages,
        style_packages,
        div_script,
        style_script,
        div_tree,
        style_tree,
        div_pictures,
        style_pictures,
        div_tables,
        style_tables,
        div_store,
        style_store,
        div_supplement,
        style_supplement,
        div_Post_report,
        style_Post_report
        )
    html_name = ''.join('Report_the_task_',formatted_today,'.html')    
    report_html_path = os.path.join(report_path,html_name)
    with open(report_html_path, "w") as file:
        file.write(report_html)
    
    #html文件转为pdf文件

    #删除中间文件





def main():
    parser = argparse.ArgumentParser(description='Formalize the task folder to adapt cyber')
    parser.add_argument('task_path', type=str, help='Path to the task folder')
    args = parser.parse_args()
    task_path = args.task_path
77554


if __name__ == '__main__':
    main()