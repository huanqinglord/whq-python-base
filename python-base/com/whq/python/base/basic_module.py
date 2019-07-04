#coding=utf-8

'''
脚本上是用 python 解释器来编程，如果你从 Python 解释器退出再进入，那么你定义的所有的方法和变量就都消失了。
为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。
模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。
这也是使用 python 标准库的方法。
'''
import sys
'''
import将把所有的名字都导入进来，但是那些由单一下划线（_）开头的名字不在此例。
大多数情况， Python程序员不使用这种方法，因为引入的其它来源的命名，很可能覆盖了已有的定义。
'''

from com.whq.python.base import basic_function
#一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，
# 模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
import basic_module_1

if __name__ == "__main__":
    print("命令行参数：")
    for i in sys.argv:
        print(i)
    print("python路径为：", sys.path)

    print(basic_function.hello1())
    #basic_function.testKeyWord(1, 2)

#dir() 函数
#内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
    print(dir(basic_module_1))
    print(dir(basic_function))
