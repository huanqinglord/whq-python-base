# -*- coding:utf-8 -*-
'''
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
'''
if __name__ == '__main__':
    set1 = {1,2,"a"}
    print(set1)

    set2 = set("121sddsfsd")
    print(set2)

    set3 = set()
    print("创建空集合 ", set3)

    if "a" in set1:
        print(True)
    else:
        print(False)

    print("集合运算")
    print("差集")
    print(set1 - set2)
    set4 = {1, 2, "b", "c", "s"}
    #set2中的1和2为字符类型 不会去除
    print(set1 - set4)
    print("交集")
    print(set1 & set4)
    print("并集")
    print(set1 | set4)
    print("两个集合中不同时存在的元素")
    print(set1 ^ set4)