# -*- coding: utf-8 -*-

# 此模块练习string字符串相关操作

if __name__ == '__main__':
    str1 = 'str1'
    str2 = "str2"
    print("在python中单引号和双引号都可以定义字符串", str1, str2)

    # 字符串截取语法
    # 变量[起始下标:结束下标]
    print(str2[0]) # 包含起始下标
    print(str2[0:2]) # 不包含结束下标
    print(str2[2:]) #结束下标不注明则默认截取到字符串末尾
    print(str2[0:-1]) #字符串下标从后到前依次为-1、-2、-3...
    print(str1 + str2) #连接字符串
    #但是不支持字符串和其他数据类型连接
    #TypeError: unsupported operand type(s) for +: 'int' and 'str'
    #print(1 + str2)
    print(str1 * 2) #字符串输出几遍就在*后面写几

    #\python中使用反斜杠转义字符
    #end 属性配置为空则不会换行，通过\n实现换行
    print(str1 + "\n", end="")
    print(str2)

    # 在字符串前加r则反斜杠失去转义作用
    str3 = r"""多行文档
    第一行\n第二行"""
    print(str3)

    #反斜杠可以实现一行代码写多行
    str4 = \
    "str4"
    print(str4)

    str5 = "sdfd\
sdfs"
    print(str5)