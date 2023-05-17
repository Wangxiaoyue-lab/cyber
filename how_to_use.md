Comprehensive Yielding Bioinformatics Electronic Report


# 1.Install

```shell
git clone https://github.com/Wangxiaoyue-lab/cyber.git
```

or

```shell
pip install https://github.com/Wangxiaoyue-lab/cyber.git
```


# 2.Initialize

When you use it in shell:

```shell
python /.../cyber/use/report_project.py /path/of/yout/project
```

It will generate a `cyber.yaml` file in the specified path, and the project directory is recommend .

Please fill in the `cyber.yaml` file


# 3.Managerment

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
python /.../cyber/use/formalize.py /path/of/yout/task
```


# 4.Report the task

We  should generate a readable and adiaphorous report

```shell
python /.../cyber/use/report_task.py /path/of/yout/project/cyber.yaml /path/of/yout/task
```


# 5.Report summary