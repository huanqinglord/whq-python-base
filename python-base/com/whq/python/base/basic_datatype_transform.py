# -*- coding:utf-8 -*-

'''
此模块练习数据类型转换
'''

if __name__ == '__main__':
    print("将一个字符串转换为整数")
    print(int("1"))
    #无法转换一个非数字的值 ValueError: invalid literal for int() with base 10: 'a'
    #print(int("a"))

    print("将一个字符串转换为浮点数据")
    print(float("1"))

    print("创建一个复数")
    complex1 = complex(1+1j)
    print(complex1)
    print("将一个对象转换为字符串")
    print(str(1))
    #尝试转换列表、元组、集合、字典
    list1 = [1,2,"list"]
    tuple1 = (1,2,"tuple")
    set1 = {1,2,"set"}
    dictionary1 = {1:"a","2":"b"}
    print(str(list1))
    print(str(tuple1))
    print(str(set1))
    print(str(dictionary1))

    print("将对象 x 转换为表达式字符串")
    print(repr("1"))

    print("用来计算在字符串中的有效Python表达式,并返回一个对象")
    print(eval("123"))

    print("将序列 s 转换为一个元组")
    #TypeError: 'int' object is not iterable
    #print(tuple(12345679))
    print(tuple(list1))
    print(tuple("123456789"))

    print("\
将序列 s 转换为一个列表")
    print(list(set1))
    #字典默认转换Key值
    print(list(dictionary1))
    print(list(dictionary1.keys()))
    print(list(dictionary1.values()))

    print("转换为可变集合")
    print(set(list1))
    list1 = list1 + [1]
    print(list1)
    #去重
    print(set(list1))

    print("创建一个字典。d 必须是一个序列 (key,value)元组")
    list2 = [(1,"a"),("2","b")]
    print(dict(list2))
    tuple2 = ((1,"a"),("2","b"))
    print(dict(tuple2))

    print("转换为不可变集合")
    print(list1)
    list1[1] = "a"
    print(list1)
    list1 = frozenset(list1)
    print(list1)
    #经过frozenset函数转换后变为不可变集合
    #TypeError: 'frozenset' object does not support item assignment
    #list1[1] = 2
    #print(list1)

    print("将一个整数转换为一个字符")
    x = 2
    print(chr(x))

    print("将一个字符转换为它的整数值")
    #TypeError: ord() expected a character, but string of length 3 found
    #print(ord("1.2"))
    print(ord("a"))

    print("将一个整数转换为一个十六进制字符串")
    print(hex(123))

    print("将一个整数转换为一个八进制字符串")
    print(oct(123))