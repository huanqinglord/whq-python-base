# -*- coding:utf-8 -*-

'''
你可以定义一个由自己想要功能的函数，以下是简单的规则：
    函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
    任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
    函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    函数内容以冒号起始，并且缩进。
    return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
'''

if __name__ == "__main__":
    print("第一个函数")
    def hello():
        return "Hello World!"

    print(hello())

    print("第二个函数")
    def area(width, hight):
        return width * hight

    print("长：5，宽：4 的面积是：", area(5, 4))
    #必须使用return结束函数
    """
    #####################################
    python中类型属于对象，变量是没有类型的。它仅仅是一个对象的引用（一个指针），
    可以指向任何类型的对象
    """

    """
    #########################################
    python中strings、tuples、numbers是不可变的数据类型，其他数据类型都可以改变，例如：list、dict
    不可变类型（immutable）：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，
                再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
    可变类型（mutable）：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，
                本身la没有动，只是其内部的一部分值被修改了。
    """

    """
    不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。
                如fun（a），传递的只是a的值，没有影响a对象本身。
                比如在 fun（a）内部修改 a 的值，只是修改另一个
                复制的对象，不会影响 a 本身。
    可变类型：类似 c++ 的引用传递，如 列表，字典。
                如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
    python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
    """
    print("第三个函数:传不可变对象实例")
    immutable1 = 1
    immutable2 = "a"
    immutable3 = (1,2,"a")
    def testImmutable(immutable1, immutable2, immutable3):
        immutable1 = 2
        immutable2 = "b"
        immutable3 = ("c")
        print(immutable1, immutable2, immutable3)
        return
    print(testImmutable(immutable1, immutable2, immutable3))
    print(immutable1, immutable2, immutable3)
    #以上测试可以看到 immutable三个不可变对象变量在函数testImmutable中只是将值赋予新的对象引用指针，
    #    函数中只是将新的指针引用指向了新的对象，而函数外面的指针引用依然不变


    print("第四个函数：传可变对象实例")
    mutable1 = list("0123465789")
    def testMutable(a):
        a[2] = "a"
        return a
    print(mutable1)
    it1 = iter(testMutable(mutable1))
    for x in it1:
        print(x, end=",")
    print()

    '''
    ############################################
    参数
        以下是调用函数时可使用的正式参数类型：
        必需参数
            必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样
        关键字参数
            关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
            使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
        默认参数
            调用函数时，如果没有传递参数，则会使用默认参数。
        不定长参数
            你可能需要一个函数能处理比当初声明时更多的参数。
            这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下：
            def functionname([formal_args,] *var_args_tuple ):
               "函数_文档字符串"
               function_suite
               return [expression]
            加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。

            还有一种就是参数带两个星号 **基本语法如下：
            def functionname([formal_args,] **var_args_dict ):
               "函数_文档字符串"
               function_suite
               return [expression]
            加了两个星号 ** 的参数会以字典的形式导入。
    '''

    print("第五个函数：关键字参数")

    def testKeyWord(a , b):
        print(a, b)
        return
    #以下调用先传入的是 b参数的值
    testKeyWord(b = 1, a = 2)

    print("第六个函数：默认参数")
    def testDefault(a = "Hello World!"):
        return a
    print(testDefault())
    print(testDefault(1))

    print("第七个函数：不定长参数")


    print("第八个函数：关键字参数")
