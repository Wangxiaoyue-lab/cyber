Comprehensive Yielding Bioinformatics Electronic Report

This is a preliminary and untested bioinfomatics project standard, please use caution.

If you have any suggestion , contact with me at caojundudu@qq.com

# 0.Prepare

You should have these folders in your home directionary:
project
software
reference
cyber

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


R

```R
source(past0(cyber_dir,'/cyber_py/support/_2_cyber_log.R'))
task_path <- "/path/of/task"
cyber_packages(task_path)
```



python

```python
import sys
sys.path.append(cyber_dir)
from cyber_py.support._3_cyber_log import cyber_packages
task_path = "/path/of/task"
cyber_packages(task_path)
```


shell

```shell
cyber_packages() {
    local cmd=$1
    local version
    version=$($cmd -v 2>&1)
    if [[ $version == *"-v"* ]]; then
        version=$($cmd --version 2>&1)
    fi
    echo "$cmd version: $version"
}



```

# 6.Report the task

We  should generate a readable and adiaphorous report

```shell
cyber_r /path/of/yout/task
```

# 7.Report summary
