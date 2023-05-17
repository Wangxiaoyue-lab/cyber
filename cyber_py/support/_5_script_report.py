import os
import pandas as pd
from nbconvert import PythonExporter
import argparse
from datetime import datetime

def get_script_info(folder_path):
    script_info = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            creation_time = os.path.getctime(file_path)
            creation_time = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
            if file.endswith('.py'):
                with open(file_path, 'r') as f:
                    script = f.read()
                    script_info.append({'name': file, 'path': file_path, 'language': 'Python', 'length': len(script), 'creation_time': creation_time})
            elif file.endswith('.R'):
                with open(file_path, 'r') as f:
                    script = f.read()
                    script_info.append({'name': file, 'path': file_path, 'language': 'R', 'length': len(script), 'creation_time': creation_time})
            elif file.endswith('.sh'):
                with open(file_path, 'r') as f:
                    script = f.read()
                    script_info.append({'name': file, 'path': file_path, 'language': 'Shell', 'length': len(script), 'creation_time': creation_time})
            elif file.endswith('.cpp'):
                with open(file_path, 'r') as f:
                    script = f.read()
                    script_info.append({'name': file, 'path': file_path, 'language': 'C++', 'length': len(script), 'creation_time': creation_time})
            elif file.endswith('.java'):
                with open(file_path, 'r') as f:
                    script = f.read()
                    script_info.append({'name': file, 'path': file_path, 'language': 'Java', 'length': len(script), 'creation_time': creation_time})
            else:
                with open(file_path, 'r') as f:
                    script = f.read()
                    script_info.append({'name': file, 'path': file_path, 'language': 'Other', 'length': len(script), 'creation_time': creation_time})
    df = pd.DataFrame(script_info)
    df['prefix'] = df['name'].apply(lambda x: int(x.split('_')[0]) if x.split('_')[0].isdigit() else float('inf'))
    df = df.sort_values(by=['prefix', 'creation_time'])
    df.reset_index(drop=True, inplace=True)
    return df

def get_scripts(df):
    scripts = []
    for i, row in df.iterrows():
        with open(row['path'], 'r') as f:
            script = f.read()
            scripts.append(script)
    script_df = pd.DataFrame({'script': scripts}, index=df.index)
    return script_df

def main():
    parser = argparse.ArgumentParser(description='Get script info')
    parser.add_argument('folder_path', type=str, help='Path to the folder containing scripts')
    parser.add_argument('output', type=str, help='Path to the output HTML file')
    args = parser.parse_args()
    df = get_script_info(args.folder_path)
    html_table = df.to_html()

    with open(args.output, 'w') as f:
        f.write("""
        <style>
            table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
            }
            th {
                text-align: center;
                background-color: green;
                color:white;
            }
            td {
                padding: 5px;
                text-align: left;
                max-width: 240px;
                word-wrap: break-word;
                background-color: lightyellow;
            }
        </style>
        """)
        f.write(html_table)

    script_df = get_scripts(df)
    #代码解释部分暂缺
if __name__ == '__main__':
    main()