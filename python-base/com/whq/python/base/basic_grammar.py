# -*- coding: utf-8 -*-
"""
此模块练习python基础语法
"""

if __name__ == '__main__':
    if True:
        print("1 " + "True")
    else:
        print("else")
    '''
    以下缩进不对会提示如下异常
    File "D:/IDEA/workspace-github-whq/whq-python-base/python-base/com/whq/python/base/basic_grammar.py", line 11
    print("缩进不对！")
                  ^
    IndentationError: unindent does not match any outer indentation level
    '''
       # print("缩进不对！")


    '''
    \可以实现代码换行，如下：
    total = item_one + \
            item_two + \
            item_three
    在[]、{}、()中的多行代码不需要使用\换行，如下：
    total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
    '''
    total = ['item_one', 'item_two', 'item_three',
             'item_four', 'item_five']
    print(2, end=" ")
    print(total)

    item_one = 'item_one'
    item_two = 'item_two'
    item_three = 'item_three'
    total = item_one + \
        item_two + \
        item_three
    print("3 " + total)

    # python 中的单引号和双引号 作用完全相同
    # 以后使用双引号（java习惯）
    one = 'one'
    two = "two"
    print("4 " + one + two)

    # '''(三个单引号) 或者 """(三个双引号)可以定义多行字符串

    one = '''这是三个单引号定义的多行字符串，
已换行
    '''
    two = """这是三个双引号定义的多行字符串，
    已换行"""
    print("5 " + one)
    print("6 " + two)

    #转义符 \
    escape_character = "这句话后要换行，\n已换行。"
    print("7 " + escape_character)

    #使用r可以让反斜杠\不进行转义
    r = r"这句话后要换行，\n换行符没有起作用。"
    print("8 " + r)

    #字符串可以用+号运算符连接在一起，*号运算符重复
    #*号相当于字符串乘几次，小于或等于0认为此字符串不输出,且必须为整数才能正常显示
    this = "this "
    ise = "is "
    string = "string"
    print("9 " + this+ise+string)
    print("10 " + this * 1 + ise * 2 + string * 3)

    #python中没有字符类型，一个字符就是长度为1的字符串
    char = "a"
    print("11 " + char)

    #python 中的字符串不能改变
    #字符串索引，从左往右从0开始，从右往左从-1开始
    #字符串的截取的语法格式：变量[头下标:尾下标:步长]
    str = "123456789"

    print("12 " + str[1])   #获得第二个字符
    print("13 " + str[1: 3])    #获得第二个到第三个字符串,与java中String中的方法subString相同，包含起始索引字符
                                #不包括结束索引字符
    print("14 " + str[1: -1])   #获取第二个字符到倒数第二个字符
    print("15 " + str[1: ])     #输出从第二个字符到后面所有的字符

    #########################################
    # python中空行也是代码的一部分，各函数之间、类的方法之间、类和函数入口之间加空行以便日后维护
    #########################################

    #用户键盘录入
    #input("\n\n按下 enter 键后退出！")

    #python中多条语句在同一行使用必须用分号分隔
    test = "分号将多条语句连接在一起啦！"; haha = "真的吗？"; hehe = "真的！" ; print("16 " + test + haha + hehe)