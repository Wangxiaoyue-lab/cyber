Comprehensive Yielding Bioinformatics Electronic Report

This is a preliminary and untested bioinfomatics project standard, please use caution.

If you have any suggestion , contact with me at caojundudu@qq.com

# 0.Prepare

You should have these folders in your home directionary:`<br>`
project `<br>`
software `<br>`
reference `<br>`
cyber `<br>`

# 1.Install

gitclone（recommend）

```shell
git clone https://github.com/Wangxiaoyue-lab/cyber.git
```

or

pip

```shell
pip install https://github.com/Wangxiaoyue-lab/cyber.git
```

Then please make alias

```shell
python //////cyber/cyber_py/alias.py
```

# 2.Project

When you use it in shell:

```shell
cyber_p /path/of/yout/project
```

It will generate a `cyber.yaml` file in the specified path, and the project directory is recommend .

Please fill in the `cyber.yaml` file

# 3.Formalization

A project should be split into several tasks including analysis task, development task, investigation task and import task.

Analysis task is the commonest task and should be split into organized and standard structure.

```shell
task1
	script
	input
		description.yaml
	output
		picture
		table
		store
	report
		log.out
		report.yaml
```

It is recommended to run the script.

```shell
cyber_f /path/of/yout/task
```

# 4.Pipeline

# 5 Packages

Firstly, get the path of cyber in shell

```shell
cyber_dir
```

copy it

R

```R
cyber_packages <- function(task) {
    today <- Sys.time() %>% as.character %>% gsub(' |-|:','_',.)
    sink(paste0(task, "/report/loading_packages_R_", today, ".txt"))
    #print(R.home)
    print(sessionInfo())
    sink()
}
cyber_packages(project_task)

```

```R
source(past0(cyber_dir,'/cyber_py/support/_2_cyber_log.R'))
task_path <- "/path/of/task"
cyber_packages(task_path)
```

python

```python
import os
import sys
import session_info
from datetime import datetime
report_folder = os.path.join(project_task, 'report')
if not os.path.exists(report_folder):
    os.makedirs(report_folder)
date_name = 'loading_packages_Python_'+datetime.now().strftime("%Y_%m_%d_%H_%M")+'.txt'
file_name = os.path.join(report_folder, date_name)
original_stdout = sys.stdout
with open(file_name, 'w') as f:
    sys.stdout = f
    print(sys.executable)
    session_info.show()
    sys.stdout = original_stdout

```

直接运行函数可能由于命名空间不统一的问题包不全

```python
import sys
sys.path.append(cyber_dir)
from cyber_py.support._3_cyber_log import cyber_packages
task_path = "/path/of/task"
cyber_packages(task_path)
```

shell

```shell
cyber_packages ${task_path} ${cmds}
# e.g. cyber_packages ${task_path} fastp,cellranger,cellbender
```

# 6.Report the task

We  should generate a readable and adiaphorous report

```shell
cyber_r /path/of/yout/task
```

# 7.Summary
