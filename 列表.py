# -*- codeing=utf-8 -*-
# @Time: 22:12
# @Author :liuwei
# @File:列表.py

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

list = ['physics', 'chemistry', 1997, 2000]
print("list1[2]: ", list[2])
list[2]=1999

print("list1[2]已经改变: ", list[2])
del list[2]
print("list1[2]已经删除: ", list[2])

print(list.count(2000))

a=[1,2,3,4,5]
print(a.count(2))

b=['你','我','他']
print(b[0])