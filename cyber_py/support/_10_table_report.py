import os
import argparse
from datetime import datetime
import chardet
from hashlib import sha256
import pandas as pd



def read_file_detect(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        encoding = chardet.detect(raw_data)['encoding']
    with open(file_path, 'r', encoding=encoding) as f:
        content = f.read()
    return content

def get_tables_info(directory):
    files_info = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.xls', '.xlsx', '.csv', '.txt', '.tsv')):
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    content = f.read()
                    hash = sha256(content).hexdigest()
                creation_time = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d')
                if os.stat(file_path).st_size == 0:
                    rows, cols = 0, 0
                    lines = []
                elif file.endswith(('.xls', '.xlsx')):
                    df = pd.read_excel(file_path)
                    rows, cols = df.shape
                    lines = df.iloc[:6, :6].fillna('').applymap(str).apply(lambda x: x.str.slice(0, 30)).values.tolist()
                    if cols > 6:
                        for line in lines:
                            line.append('...')
                elif file.endswith(('.csv', '.tsv')):
                    encoding = chardet.detect(content)['encoding']
                    df = pd.read_csv(file_path, sep='\t' if file.endswith('.tsv') else ',', encoding=encoding)
                    rows, cols = df.shape
                    lines = df.iloc[:6, :6].fillna('').applymap(str).apply(lambda x: x.str.slice(0, 30)).values.tolist()
                    if cols > 6:
                        for line in lines:
                            line.append('...')
                else:
                    content = read_file_detect(file_path)
                    lines = content.splitlines()[:6]
                    rows = len(lines)
                    cols = max(len(line.split()) for line in lines)
                files_info.append({
                    'file_name': file, 
                    'file_path': file_path, 
                    'creation_time': creation_time, 
                    'hash': hash, 
                    'rows': rows, 
                    'cols': cols, 
                    'lines': lines
                    })
    df = pd.DataFrame(files_info)
    return df

def tables_to_div(df):
    html = '<div class="tables">'
    for _, row in df.iterrows():
        html += '<p><span class="label">file_name:</span><span class="value">{}</span></p >'.format(row['file_name'])
        html += '<p><span class="label">file_path:</span><span class="value">{}</span></p >'.format(row['file_path'])
        html += '<p><span class="label">creation_time:</span><span class="value">{}</span></p >'.format(row['creation_time'])
        html += '<p><span class="label">hash:</span><span class="value">{}</span></p >'.format(row['hash'])
        html += '<p><span class="label">rows:</span><span class="value">{}</span></p >'.format(row['rows'])
        html += '<p><span class="label">cols:</span><span class="value">{}</span></p >'.format(row['cols'])
        html += '<p><span class="label">lines:</span><br>'
        for line in row['lines']:
            html += '&emsp;' + ' '.join(line) + '<br>'
        html += '</p >'
        html += '<br>'
        html += '<hr>'
    html += '</div>'
    return html

def to_html(df):
    html = '<style> .label { font-weight: bold; color: green; } .value { display: block; margin-left: 2em; max-width: 30ch; word-wrap: break-word; } </style>'
    for _, row in df.iterrows():
        html += '<p><span class="label">file_name:</span><span class="value">{}</span></p >'.format(row['file_name'])
        html += '<p><span class="label">file_path:</span><span class="value">{}</span></p >'.format(row['file_path'])
        html += '<p><span class="label">creation_time:</span><span class="value">{}</span></p >'.format(row['creation_time'])
        html += '<p><span class="label">hash:</span><span class="value">{}</span></p >'.format(row['hash'])
        html += '<p><span class="label">rows:</span><span class="value">{}</span></p >'.format(row['rows'])
        html += '<p><span class="label">cols:</span><span class="value">{}</span></p >'.format(row['cols'])
        html += '<p><span class="label">lines:</span><br>'
        for line in row['lines']:
            html += '&emsp;' + ' '.join(line) + '<br>'
        html += '</p >'
        html += '<br>'
    return html

def main():
    parser = argparse.ArgumentParser(description='Get script info')
    parser.add_argument('folder_path', type=str, help='Path to the folder containing scripts')
    parser.add_argument('output', type=str, help='Dir to the output HTML file')
    args = parser.parse_args()
    df = get_tables_info(args.folder_path)
    html = to_html(df)
    with open(args.output, 'w') as f:
        f.write(html)

if __name__ == '__main__':
    main()