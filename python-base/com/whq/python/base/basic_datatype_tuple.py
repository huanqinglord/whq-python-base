# -*- coding:utf-8 -*-

'''
    元组Tuple：与列表list类似，但是无法修改其中的元素
'''

if __name__ == '__main__':
    print("元组测试")
    tuple1 = ('a', 1 , 1.2, ['b', 4],('c',5))
    #访问具体元素
    print(tuple1[3])
    #访问第2个到第4个元素
    print(tuple1[1:4])
    #访问第2个到最后一个元素
    print(tuple1[1:])
    #访问第1个到倒数第二个元素
    print(tuple1[:-1])
    #访问全部元素
    print(tuple1)
    print(tuple1[:])
    #以步长为2的方式访问元素
    print(tuple1[::2])
    #倒序输出
    print(tuple1[::-1])
    #重复输出元素
    print(tuple1 * 2)
    #元组拼接
    print(tuple1 + tuple1[2:4])

    #修改元组中的元素是非法的
    print("修改元组中的元素是非法的")
    #以下执行报错
    '''
    Traceback (most recent call last):
    File "D:/IDEA/workspace-github-whq/whq-python-base/python-base/com/whq/python/base/basic_datatype_tuple.py",
     line 40, in <module>
    tuple1[1] = 2
    TypeError: 'tuple' object does not support item assignment
    '''
    #tuple1[1] = 2
    print(tuple1)

    #但是可以修改元组中的列表中的元素
    #将['b', 4] 改成 ['', 4]
    tuple1[3][0] = "c"
    print(tuple1)

    print("单个元素的元组声明")
    tuple2 = ()
    print("空元组 ", tuple2)

    '''
    Traceback (most recent call last):
    File "D:/IDEA/workspace-github-whq/whq-python-base/python-base/com/whq/python/base/basic_datatype_tuple.py",
    line 53, in <module>
    print("单个元素的元组,声明时未加逗号 ", tuple3[0])
    TypeError: 'int' object is not subscriptable
    '''
    tuple3 = (1)
    #print("单个元素的元组,声明时未加逗号 ", tuple3[0])
    tuple4 = (2,)
    print("单个元素的元组，声明时加逗号 ", tuple4[0])