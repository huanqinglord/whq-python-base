# -*- coding: utf-8 -*-

# 此模块练习python中的数据类型
if __name__ == "__main__":
# Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
    int_type = 1
    float_type = 1.0
    string_type = "a"
    print(int_type, float_type, string_type)
# 多个变量赋值
    a, b, c = 1, 2, "c"
    print(a, b, c)
    a = b = c = "a"
    print(a, b, c)

    '''
    Python3 中有六个标准的数据类型：
    Number（数字）
    String（字符串）
    List（列表）
    Tuple（元组）
        元组和列表十分类似，只不过元组和字符串一样是不可变的，即你不能修改元组。
        元组通过圆括号中用逗号分割的项目定义。
        元组通常用在使语句或用户定义的函数能够安全地采用一组值的时候，即被使用的元组的值不会改变。
    Set（集合）
    Dictionary（字典）
    Python3 的六个标准数据类型中：
    不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
    可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
    '''

# Number
# Python3 支持 int、float、bool、complex（复数）。
    a, b, c, d = 1, 1.0, True, 1+1j
    # 通过内置函数type()查看变量类型
    print(type(a), type(b), type(c), type(d))
    #isinstance()判断是否是一种类型，type()不会认为子类是一种父类类型，isinstance()可以
    print(isinstance(a, int))

    #python2中布尔类型0代表False，1代表True，python3中用False和True表示，但实际还是Number类型
    print(True + 1) # 输出结果为2
    print(False + 1) # 输出结果为1