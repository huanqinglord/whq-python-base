# -*- coding:utf-8 -*-
'''
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
'''
if __name__ == '__main__':
    print("Dictionart 类似于java的Map，java之前也是使用Dictionary类")
    dictionary1 = {}
    print("空字典声明 ", dictionary1)

    #添加元素
    dictionary1["a"] = {"a"}
    print(dictionary1["a"])
    # 字典中的key值唯一
    dictionary1["a"] = {2}
    print(dictionary1["a"])

    dict2 = {"b":"b","c":3,3:"d","3":"e"}
    #数字3和字符串3因为数据类型不同，可以同时作为key值
    print(dict2)
    print(dict2[3])
    print(dict2["3"])

    keys = dict2.keys()
    print("输出所有的keys值：", keys)
    print("输出所有的values值：", dict2.values())

    #构造函数dict()
    print("入参为列表的构造")
    list1 = [("a",1),("b",2),("c", 3)]
    dict3 = dict(list1)
    print(dict3)

    print("入参为元组的构造")
    list2 = (("a",1),("b",2),("c", 3))
    dict4 = dict(list2)
    print(dict4)

    print("入参为键值对")
    dict5 = dict(d=4, e=5, f=6)
    print(dict5)