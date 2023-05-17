# cyber

Comprehensive Yielding Bioinformatics Electronic Report

注：

script部分可以是snakemake。不过snakemake应该是task内部的设计，不可以跨task

script部分可以是jupyter notebook，不过请图片保存pdf版本一份。juptyter文件转成纯代码一份

# 文件结构

## 一级基本文件夹

```python
project
software
reference
```

project存储项目

software为安装软件的路径

reference为所有参考文件的位置

## project结构

```python
project1
	1_task1
	2_task2
	3_task3
project2
	1_task1
	2_task2
	3_task3
```

project里每一个大项目为一个文件夹

里面将每一个project拆分为按时间排列的task

每一个task应该标记时间与任务名

## task类型

### analysis —— 分析型task结构

```r
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

每一个task下应该有标准四个文件夹

- script存储脚本
- input存储输入的数据，如果是较大的数据或者多次利用的数据，请用ln -s软连接标记数据来源

请在description.yaml里标记输入数据相关信息

- output存储输出结果，区分类型
  - picture存储图片：png/pdf/jpg
  - table存储表格
  - 其他结果直接存储
- report
  - log.out存储服务器产生的直接控制台输出与报错
  - report.yaml请填写当前task的相关信息以生成实验报告

### development——开发型task结构

### investigation——调研型task结构

### import——外部结果型task结构

```
task1
	process
		process.yaml
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

# 工作流

## 分析

1. input

   1. 请将当前task要用到的文件与数据软链接到input里，并请填写description.yaml文件。
   2. 第一次使用的数据请标记来源，如是论文来源标记论文链接，如是数据库或者网络资源标记网址
2. script

   1. 脚本书写请清晰，分段落，有必要注释
   2. 禁止无意义或凑数变量名，统一风格如下划线或者驼峰
   3. 脚本里注意输出必要日志，严格保证控制台文件和报错文件的可读性
   4. 如若可以，尽量函数化
   5. 常用代码请模块化
3. output

   1. 图片命名严禁随意，应该标记图片类型、图片得到的关键参数、图片日期等
   2. 图片如无特殊原因，如体积过大等。应优先保存为pdf矢量图。
   3. 表格应该保证列名的意义
4. report

   1. 填写report.yaml
   2. 根据task文件夹结果生成pdf报告

## 开发

## 调研

## 外部结果

1. input

   1. 将要导出分析的文件请软链接
   2. 包含图片AI处理
2. process

   1. 如果是软件，记录版本
   2. 如果是网页工具，记录网址
3. output

   1. 将外部分析的结果返回保存

## project合并

summarize

1. 所有task合并为一个project报告
2. 自动生成目录
3. 生成task时间线，以颜色区分task类型
4. 添加文件tree
5. 手动添加项目保留情况
