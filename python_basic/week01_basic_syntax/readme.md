# Week 01 - Basic Syntax

目标：
- 熟悉 Python 基础语法、变量、输入输出。
- 掌握 if / for / while 的基本用法。
- 能遍历 list，完成简单的小程序。

本周练习列表：
- ex01_hello_and_age.py
- ex02_simple_calculator.py
- ex03_max_of_three.py
- ex04_sum_and_average.py
- ex05_times_table.py
- ex06_list_filter.py


总结一下这周代码里暴露出来的几个“典型基础点”

    input() 一律返回字符串
    只要要做大小比较 / 数值运算，记得先 int() 或 float()；
    字符串比较是字典序："9" > "10" 是 True，很坑。
    类型要始终保持一致
    不要让同一个变量在循环里忽然变成别的类型（num_max 先 float 后 str）；
    否则下一轮比较就会崩。
    慎用内置名做变量名
    比如 max 会遮住内置函数 max()。
    能用简单逻辑就不要写过度复杂的 if 嵌套
    三个数求最大值，用 max() 或简单循环就好，比你那个 main 版清晰太多。