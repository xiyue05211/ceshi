#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : 文件操作.py
# @Author : lyd
# @Time : 2022/7/2 17:50
# @Description : 相对路径和绝对路径


import os

# 判断是否为绝对路径
r = os.path.isabs(r'C:\Users\admin\Desktop\a.txt')
print(r)

# 获取路径
path = os.path.dirname(__file__)  # 获取当前文件文件夹的绝对路径
print(path)

# 获取当前的绝对路径
path = os.path.abspath('文件操作.py')
print(path)

print(os.path.abspath('匿名函数.py'))

path = os.getcwd()  # 取当前文件文件夹的绝对路径
print(path)

path = r'D:\Projects\pythonProjects\practicePy\basePy\文件操作.py'
result = os.path.split(path)  # 获取文件名
print(result)
print(result[1])

result = os.path.splitext(path)  # 获取文件类型
print(result)

result = os.path.getsize(path)  # 获取文件大小
print(result)

#连接路径
result=os.path.join(os.getcwd(),'file','aa.txt')
print(result)