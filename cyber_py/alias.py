import os

def create_file_with_content(filename, content):
    filename = os.path.expanduser(filename)
    #if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write(content)


def replace_function_content(filename, new_content):
    with open(filename, 'r') as f:
        lines = f.readlines()
    start = None
    end = None
    for i, line in enumerate(lines):
        if '####key function####' in line:
            start = i
        elif start is not None and '########' in line:
            end = i
            break
    if start is not None and end is not None:
        lines[start+1:end] = new_content
    with open(filename, 'w') as f:
        f.writelines('\n'.join(lines))


def main():
    absolute_path = os.path.split(os.path.realpath(__file__))[0]
    cyber_path = os.path.split(absolute_path)[0]
    alias_cmd_dir = f"alias cyber_dir='(cd {cyber_path} && pwd)'"
    alias_cmd_pacakages = f'cyber_packages() {{ cd "{cyber_path}" && python -m cyber_py.support._4_cyber_shell "$@"; cd -; }}'
    alias_cmd_p = f'cyber_p() {{ cd "{cyber_path}" && python -m cyber_py.report_project "$@"; cd -; }}'
    alias_cmd_f = f'cyber_f() {{ cd "{cyber_path}" && python -m cyber_py.formalize "$@"; cd -; }}'
    alias_cmd_r = f'cyber_r() {{ cd "{cyber_path}" && python -m cyber_py.report_task "$@"; cd -; }}'

    cyberrc=os.path.expanduser("~/.cyberrc")
    default_content="####key variable####\n########\n\n####key function####\n########"
    create_file_with_content(cyberrc, default_content)
    function_content=[alias_cmd_dir,alias_cmd_pacakages,alias_cmd_p,alias_cmd_f,alias_cmd_r]
    replace_function_content(cyberrc, function_content)

    bashrc_path = os.path.expanduser("~/.bashrc")
    cyberrc_line = 'if [ -f ~/.cyberrc ]; then\nsource ~/.cyberrc\nfi\n'

    with open(bashrc_path, "r") as f:
        lines = f.readlines()

    if cyberrc_line not in lines:
        with open(bashrc_path, "a") as f:
            f.write(cyberrc_line)

    os.system("source ~/.bashrc")

if(__name__=="__main__"):
    main()