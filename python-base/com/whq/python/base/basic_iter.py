# -*- coding:utf-8 -*-

'''
    此模块练习python迭代器内容.
    迭代器是一个可以记住遍历的位置的对象。
    迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
    迭代器有两个基本的方法：iter() 和 next()
'''
import sys

if __name__ == "__main__":
    print("迭代器")
    print("字符串创建迭代器")
    str1 = "123456798"
    it1 = iter(str1)
    a = 0
    while a<len(str1):
        strEnd = ","
        if a == len(str1) - 1:
            strEnd = None
        print(next(it1), end=strEnd)
        a+=1

    print("list创建迭代器")
    list1 = list("abc")
    it2 = iter(list1)
    a = 0
    while a < len(list1):
        strEnd = ","
        if a == len(list1) - 1:
            strEnd = None
        print(next(it2), end=strEnd)
        a += 1

    print("tuple创建迭代器")
    tuple1 = (1, "a", 2, "b")
    it3 = iter(tuple1)
    a, b = 0, len(tuple1)
    #当迭代器中没有元素的时候，如果继续使用next方法获取下一个元素会提示如下错误：
    #StopIteration
    #while a < b:
    #    print(next(it3))

    #尝试迭代set
    print("set创建迭代器")
    set1 = {1, "a", 2, "b"}
    it4 = iter(set1)
    a, b = 0, len(set1)
    while a < b:
        print(next(it4), end=",")
        a += 1
    print()

    print("字典dict创建迭代器")
    dict1 = {}
    dict1[1] = "a"
    print(dict1)
    dict2 = dict(((2, "b"),("c", "c")))
    print(dict2)
    #以下合并字典效率最高
    dict3 = dict1.copy()
    dict3.update(dict2)
    print(dict3)
    #
    it5 = iter(dict3.keys())
    a, b = 0, len(dict3)
    while a < b:
        c = next(it5)
        print(c, dict3[c], end=",")
        a += 1
    print()
    print("for循环遍历 迭代器")
    print(dict2)
    #遍历字典的Key值
    for x in iter(dict2):
        print(x, end=",")

    """
        创建迭代器，通过面向对象 类来实现
    """
    print("创建迭代器，通过面向对象 类来实现")
    class MyIter:
        def __iter__(self):
            self.a = 1
            return self

        def __next__(self):
            x = self.a
            self.a += 1
            #防止迭代无限循环下去
            if x > 3:
                raise StopIteration
            return x

    myIter = MyIter()
    it6 = iter(myIter)
    print(next(it6))
    print(next(it6))
    print(next(it6))
    #迭代器中判断条件符合时 抛出StopIteration异常
    #print(next(it6))

    '''
        yield 生成器，返回的是一个迭代器
    '''
    print("生成器 yield 使用")
    def fibonacciSeries(n):
        a, b, coun = 0, 1, 0
        while True:
            if coun > n:
                return
            yield a
            a, b = b, a + b
            coun += 1
    it7 = fibonacciSeries(20)

    a = 0;
    while 1:
        try:
            print(next(it7), end=",")
            a += 1
        except StopIteration:
            print(a)
            sys.exit()
