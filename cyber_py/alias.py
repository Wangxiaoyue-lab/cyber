import os
absolute_path = os.path.split(os.path.realpath(__file__))[0]
cyber_path = os.path.split(absolute_path)[0]
alias_cmd_dir = f"alias cyber_dir='pushd {cyber_path} && pwd && popd'"
alias_cmd_pacakages = f"alias cyber_pacakages='cd {cyber_path} && python -m cyber_py.support._4_cyber_shell $@ && popd'"
alias_cmd_p = f"alias cyber_p='pushd {cyber_path} && python -m cyber_py.report_project $@ && popd'"
alias_cmd_f = f"alias cyber_f='pushd {cyber_path} && python -m cyber_py.formalize $@ && popd'"
alias_cmd_r = f"alias cyber_r='pushd {cyber_path} && python -m cyber_py.report_task $@ && popd'"
with open(os.path.expanduser("~/.bashrc"),"a") as f:
    f.write(alias_cmd_dir + "\n")
    f.write(alias_cmd_pacakages + "\n")
    f.write(alias_cmd_p + "\n")
    f.write(alias_cmd_f + "\n")
    f.write(alias_cmd_r + "\n")
os.system("source ~/.bashrc")