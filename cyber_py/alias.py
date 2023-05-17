import os
absolute_path = os.path.split(os.path.realpath(__file__))[0]
cyber_path = os.path.split(absolute_path)[0]
alias_cmd_p = f"alias cyber_p='cd {cyber_path} && python -m cyber.report_project'"
alias_cmd_f = f"alias cyber_f='cd {cyber_path} && python -m cyber.cyber.formalize'"
alias_cmd_r = f"alias cyber_r='cd {cyber_path} && python -m cyber.report_task'"
with open(os.path.expanduser("~/.bashrc"),"a") as f:
    f.write(alias_cmd_p + "\n")
    f.write(alias_cmd_f + "\n")
    f.write(alias_cmd_r + "\n")
os.system("source ~/.bashrc")