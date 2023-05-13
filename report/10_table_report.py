import os
import pandas as pd
from hashlib import sha256
import argparse

def get_files_info(directory):
    files_info = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.xls', '.xlsx', '.csv', '.txt', '.tsv')):
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    content = f.read()
                    hash = sha256(content).hexdigest()
                creation_time = os.path.getctime(file_path)
                if os.stat(file_path).st_size == 0:
                    rows, cols = 0, 0
                elif file.endswith(('.xls', '.xlsx', '.csv', '.tsv')):
                    df = pd.read_csv(file_path, sep='\t' if file.endswith('.tsv') else ',')
                    rows, cols = df.shape
                else:
                    with open(file_path, 'r') as f:
                        lines = [f.readline().strip()[:30] + ('...' if len(f.readline().strip()) > 30 else '') for _ in range(6)]
                        rows, cols = len(lines), max(len(line) for line in lines)
                files_info.append({'file_name': file, 'file_path': file_path, 'creation_time': creation_time, 'hash': hash, 'rows': rows, 'cols': cols})
    df = pd.DataFrame(files_info)
    return df

def to_html(df):
    html = '<style> .label { font-weight: bold; color: green; } </style>'
    for _, row in df.iterrows():
        html += '<p><span class="label">file_name:</span><br>&emsp;{}</p >'.format(row['file_name'])
        html += '<p><span class="label">file_path:</span><br>&emsp;{}</p >'.format(row['file_path'])
        html += '<p><span class="label">creation_time:</span><br>&emsp;{}</p >'.format(row['creation_time'])
        html += '<p><span class="label">hash:</span><br>&emsp;{}</p >'.format(row['hash'])
        html += '<p><span class="label">rows:</span><br>&emsp;{}</p >'.format(row['rows'])
        html += '<p><span class="label">cols:</span><br>&emsp;{}</p >'.format(row['cols'])
        html += '<br>'
    return html

def main():
    parser = argparse.ArgumentParser(description='Get script info')
    parser.add_argument('folder_path', type=str, help='Path to the folder containing scripts')
    parser.add_argument('output', type=str, help='Dir to the output HTML file')
    args = parser.parse_args()
    df = get_files_info(args.folder_path)
    html = to_html(df)
    with open(args.output, 'w') as f:
        f.write(html)


if __name__ == '__main__':
    main()