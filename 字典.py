# -*- codeing=utf-8 -*-
# @Time: 22:32
# @Author :liuwei
# @File:字典.py
'''
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值 (key=>value) 对用冒号(:)分割，每个对之间用逗号 (,) 分割，整个字典包括在花括号 ({}) 中
'''
dict = {'Name':'Alice','Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print(dict['Alice'])
print(dict['Beth'])

#删除
del dict['Name']; # 删除键是'Name'的条目
dict.clear();     # 清空词典所有条目
del dict ;        # 删除词典