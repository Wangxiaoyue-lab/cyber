import os

absolute_path = os.path.split(os.path.realpath(__file__))[0]
cyber_path = os.path.split(absolute_path)[0]
alias_cmd_dir = f"alias cyber_dir='(cd {cyber_path} && pwd)'"
alias_cmd_pacakages = f'cyber_packages() {{ cd "{cyber_path}" && python -m cyber_py.support._4_cyber_shell "$@"; cd -; }}'
alias_cmd_p = f'cyber_p() {{ cd "{cyber_path}" && python -m cyber_py.report_project "$@"; cd -; }}'
alias_cmd_f = f'cyber_f() {{ cd "{cyber_path}" && python -m cyber_py.formalize "$@"; cd -; }}'
alias_cmd_r = f'cyber_r() {{ cd "{cyber_path}" && python -m cyber_py.report_task "$@"; cd -; }}'
 
with open(os.path.expanduser("~/.cyberrc"),"a") as f:
    f.write(alias_cmd_dir + "\n")
    f.write(alias_cmd_pacakages + "\n")
    f.write(alias_cmd_p + "\n")
    f.write(alias_cmd_f + "\n")
    f.write(alias_cmd_r + "\n")

with open(os.path.expanduser("~/.bashrc"),"a") as f:
    f.write('if [ -f ~/.cyberrc ]; then source ~/.cyberrc fi\n')

os.system("source ~/.bashrc")