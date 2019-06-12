# -*- coding:utf-8 -*-
#此模块练习python的导入用法

# 导入整个模块
import sys
from sys import argv,path
if __name__ == "__main__":
    print("1")
for i in sys.argv:
    print(i)
print("\n python的路径为：", sys.path)

#通过help()函数可以查看命令详情。比如print()，函数的参数
#sep:   string inserted between values, default a space.连接字符串，默认为一个空格
help(print)
print("abc", "123")

# 尝试导入特定成员
# 可以在任何地方随时导入
from sys import path
print("单个特定成员：", path)

#以下函数可以查看其他函数的文档字符串
help(max)
#help(help)

#仅仅想得到文档字符串
print(help.__doc__)