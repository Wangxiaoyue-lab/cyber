import os
import pandas as pd
from nbconvert import PythonExporter
import argparse

def get_script_info(folder_path):
    script_info = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.py'):
                with open(file_path, 'r') as f:
                    script = f.read()
                    script_info.append({'name': file, 'path': file_path, 'language': 'Python', 'length': len(script)})
            elif file.endswith('.R'):
                with open(file_path, 'r') as f:
                    script = f.read()
                    script_info.append({'name': file, 'path': file_path, 'language': 'R', 'length': len(script)})
            elif file.endswith('.sh'):
                 with open(file_path, 'r') as f:
                    script = f.read()
                    script_info.append({'name': file, 'path': file_path, 'language': 'Shell', 'length': len(script)})
            elif file.endswith('.cpp'):
                with open(file_path, 'r') as f:
                    script = f.read()
                    script_info.append({'name': file, 'path': file_path, 'language': 'C++', 'length': len(script)})
            elif file.endswith('.java'):
                with open(file_path, 'r') as f:
                    script = f.read()
                    script_info.append({'name': file, 'path': file_path, 'language': 'Java', 'length': len(script)})
    df = pd.DataFrame(script_info)
    return df

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
if __name__ == '__main__':
    main()