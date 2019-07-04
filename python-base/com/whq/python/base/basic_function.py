# -*- coding:utf-8 -*-
'''
你可以定义一个由自己想要功能的函数，以下是简单的规则：
    函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
    任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
    函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    函数内容以冒号起始，并且缩进。
    return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
'''

def hello1():
    return "Hello World!"

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
    def testNoKnowValue(a, *vartuple):
        "打印所有参数"
        print(a)
        print(vartuple)
        return
    testNoKnowValue("a", 1, 2)

    def testSecondNoKnowValue(a, **vardict):
        "多参数字典类型传入"
        print(a)
        print(vardict)
        return
    #如下调用报错
    #TypeError: testSecondNoKnowValue() takes 1 positional argument but 3 were given
    #testSecondNoKnowValue("a", 1, 2)
    testSecondNoKnowValue("a", c=2, b=3)

    #声明函数时，参数中星号 * 可以单独出现
    #如果单独出现星号 * 后的参数必须用关键字传入
    print("第八个函数：*后参数必须关键字传入")
    def testMustKeyWords(a, b, *, c):
        print(a, b, c)
    #TypeError: testMustKeyWords() takes 2 positional arguments but 3 were given
    #testMustKeyWords(1, 2, 3)
    testMustKeyWords(1, 2, c = 3)

    ####################################################################
    '''
    匿名函数：
        python 使用 lambda 来创建匿名函数。
        所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
        lambda 只是一个表达式，函数体比 def 简单很多。
        lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
        lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
        虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
    '''
    """
        lambda 函数的语法只包含一个语句，如下：
        lambda [arg1 [,arg2,.....argn]]:expression
    """
    print("第九个函数：匿名函数")
    sum = lambda a, b: a * b
    print(sum(1, 2))

    ##############################################################
    '''
    变量作用域
        Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
        变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
        L （Local） 局部作用域
        E （Enclosing） 闭包函数外的函数中
        G （Global） 全局作用域
        B （Built-in） 内置作用域（内置函数所在模块的范围）
        以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），
            再找不到就会去全局找，再者去内置中找。

        内置作用域是通过一个名为 builtin 的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，
            所以必须导入这个文件才能够使用它。在Python3.0中，可以使用以下的代码来查看到底预定义了哪些变量:
            >>> import builtins
            >>> dir(builtins)

        Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
            其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
            也就是说这些语句内定义的变量，外部也可以访问，如下代码：
            >>> if True:
            ...  msg = 'I am from Runoob'
            ...
            >>> msg
            'I am from Runoob'
            >>>
    '''

    #################################################
    """
    global 和 nonlocal关键字
        当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
    """
    print("第十个函数：global关键字")
    num = 1
    print(num)
    def testglobalKeyWord(num1):
        "在声明需要修改num变量之前的代码无法使用num参数"
        #num = 3
        #print(num)
        global num
        num = num1
        print(num)
        return num
    print(testglobalKeyWord(2))

    #如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
    print("第十一个函数：nonlocal关键字")
    def testnonlocalKeyWord():
        num = 1
        print(num)
        def inner():
            nonlocal num
            print(num)
            num = 2
            return
        inner()
        print(num)
        return
    testnonlocalKeyWord()
    #查看函数说明
    print(testglobalKeyWord.__doc__)

    a = 1
    def a():
        a = a + 1