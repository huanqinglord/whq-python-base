#coding:utf-8

'''
try语句按照如下方式工作；
    首先，执行try子句（在关键字try和关键字except之间的语句）
    如果没有异常发生，忽略except子句，try子句执行后结束。
    如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except
        之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
    如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
'''

if __name__=="__main__":
    print("python异常")
    '''
    while True:
        try:
            x = input("请输入一个数字：")
            try:
                a = int(x)
                print("你输入的数字是整数：", a)
            except:
                try:
                    a = float(x)
                    print("你输入的数字是浮点数：", a)
                except:
                    a = complex(x)
                    print("你输入的数字是复数：", a)
        except:
            print("你输入的不是数字！")
        else:
            goon = input("是否继续？Y/N")
            if str(goon).upper() == 'N':
                break
    '''
    print("raise抛出异常")

    if True:
        try:
            raise NameError("异常测试")
        except NameError as e:
            print(e)

    print("自定义异常")


    #自定义异常类
    class MyTestError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)

    #finally 无论是否有异常都会执行
    try:
        try:
            raise MyTestError("test")
        finally:
            print("finally test")
    except MyTestError as e:
        print(e)

    #定义预清理行为
    #在文件操作用with open(file,mode) as f 中，无论后续处理文件是否有异常都会close掉打开的文件

    ########################################################################
    '''
    assert 断言
    assert expression
    等价于：
    if not expression
        raise AssertionError
    assert 后面也可以紧跟参数:
        assert expression [, arguments]

    if not expression:
    raise AssertionError(arguments)
    '''

    print("assert Test")
    try:
        assert 1==2
    except AssertionError as e:
        print("assert1", e)

    try:
        assert 1==2, "当断言失败时，异常描述信息"
    except AssertionError as e:
        print("assert2", e)
