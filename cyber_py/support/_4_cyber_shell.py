import subprocess
import argparse
import os
import datetime

def cyber_packages(file_path,cmds):
    cmds = cmds.split(',')
    with open(file_path, 'w') as f:
        for cmd in cmds:
            try:
                version = subprocess.check_output([cmd, '-v'], stderr=subprocess.STDOUT).decode('utf-8')
            except subprocess.CalledProcessError:
                try:
                    version = subprocess.check_output([cmd, '--version'], stderr=subprocess.STDOUT).decode('utf-8')
                except subprocess.CalledProcessError:
                    version = 'unknown'
            f.write(f'{cmd} version: {version}\n')

def main():
    parser = argparse.ArgumentParser(description='Save session info of linux')
    parser.add_argument('--task_path', type=str, required=True, help='Path to the task to save session info')
    parser.add_argument('--cmds', type=str, required=True, help='cmds needed to get version')
    args = parser.parse_args()
    today = datetime.now()
    formatted_today = today.strftime('%Y-%m-%d')
    packages_file_name = ''.join['loading_packages_shell_',formatted_today,'.txt']
    file_path=os.path.join(args.task_path,"report",packages_file_name)
    cyber_packages(file_path,args.cmds)

if __name__ == '__main__':
    main()



 