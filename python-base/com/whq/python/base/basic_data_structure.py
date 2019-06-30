# -*- coding: utf-8 -*-

'''
python中的数据结构
'''

if __name__ == '__main__':
    print("list相关操作")
    list1 = [1,2,"a"]
    print(list1)
    print("append方法添加元素")
    list1.append("b")
    print(list1)
    #通过以下方式同样添加
    list1[len(list1):] = "c"
    print(list1)

    print("extend方法拼接列表")
    list1.extend(list("whq"))
    print(list1)
    list1[len(list1):] = list("TT")
    print(list1)
    #拼接并替换部分列表元素
    list1[-4:-2] = list("123456")
    print(list1)
    print("insert方法插入新元素")
    list1.insert(-2, "X")
    print(list1)
    #list1.insert(len(list1), "X")相当于list1.append("X")
    #尝试添加列表,将列表作为一个元素添加
    list1.insert(-2, list("H"))
    print(list1)

    print("remove方法移除元素")
    list1.remove(["H"])
    print(list1)
    #remove方法只能移除元素
    #list1.remove(list1[0:2])
    #print(list1)

    print("pop方法移除并返回相应元素，如果不存在索引元素则返回并移除最后一个元素")
    print(list1.pop())
    print(list1)
    #尝试移除空列表
    ################################
    #IndexError: pop from empty list
    #list2 = []
    #print(list2)
    #print(list2.pop())

    print("clean方法移除列表中的所有元素")
    #list1.clear()
    #print(list1)
    #del 同样可以做到
    #del list1[0:len(list1)]
    #del list1[:]
    #print(list1)
    #del 删除列表对象  NameError: name 'list1' is not defined
    #del list1
    #print(list1)
    #del 移除部分元素
    del list1[0]
    print(list1)
    print("index(x)返回列表中第一次出现x的索引")
    print(list1.index("6"))

    print("count(x)方法统计x元素在列表中的个数")
    print(list1.count("T"))
    print("sort()方法排序")
    #TypeError: '<' not supported between instances of 'str' and 'int'
    #默认排序无法同时排序不同类型
    #list1.sort()
    print(list1)

    print("reverse方法颠倒列表")
    list1.reverse()
    print(list1)
    #################################
    #将列表当作堆栈使用，对战先进后出
    list1.clear()
    for x in list("123456789"):
        list1.append(x)
    print(list1)
    while True:
        try:
            print(list1.pop(), end=",")
        except:
            break

    '''
    列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，
        用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。
    每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根
        据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就
        必须使用括号。
    '''
    print()
    print("列表推导式")
    list1 = list("12345")
    print(list1)
    list2 = [int(x)**2 for x in list1]
    print(list2)
    #返回的元组print没法打印 必须循环打印
    list3 = (int(x)**2 for x in list1)
    print("tuple list3")
    it1 = iter(list3)

    print("aaaaaaaaaaaaaaaa")
    for x in list3:
        print(x)
    tuple1 = (1, 2, 3)
    print(tuple1)

    #加if条件判断
    print("list2" , list2)
    list3 = [x**2 for x in list2 if x > 10]
    print(list3)

    list3 = [x + y for x in list2 if x>10 for y in list2 if y<=10]
    print(list3)

    def printMatrix(a):
        for x in a:
            print(x)
    print("矩阵3x4 变成4x3")
    matrix = [\
        [1,2,3,4], \
        [5,6,7,8], \
        [9,10,11,12]]

    printMatrix(matrix)

    matrix = [[x[i] for x in matrix] for i in range(len(matrix[0]))]
    printMatrix(matrix)



    print("字典遍历")
    dict1 = dict([[1,"a"], [2, "b"], [3, "c"]])
    for k, v in dict1.items():
        print(k, v)
    print("遍历多个序列")
    print(list3)
    list4 = list(dict1.keys())
    list4.extend(list(dict1.values()))
    print(list4)
    for l2, i1 in zip(list3, list4):
        print(l2, i1)

    print("")

    print("")

    print("")

    print("")

    print("")
