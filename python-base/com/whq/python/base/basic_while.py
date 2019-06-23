# -*- coding: utf-8 -*-

'''
    循环与别的语言类似，不过在python中后续可以用esle处理其他情况，for循环也同样可以如此处理
'''
if __name__ == "__main__":
    a = 1
    while a < 8:
        print(a)
        a+=1
    else:
        print(a)

    #当while循环中只有一句代码时可以直接写在后面
    print("-----------------------------------------")
    #无限循环
    b = 1
    #while (b < 5): print(b)

    """
    for <variable> in <sequence>:
    <statements>
    else:
        <statements>
    """
    print("for循环")

    #set 无序且去重
    for x in set("123456111111111111"):
        print(x)

    for x in [1, 2, "s" ,"a"]:
        print(x)

    print("break跳出循环")

    for x in list("abcdefg"):
        if x == "c":
            break
        print(x)

    #range()函数
    print("range()函数")
    for x in range(5):
        print(x)

    print("使用range指定区间的值")
    print(list(range(5, 9)))

    print("指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长')")
    print(set(range(0, 10 , 3)))
    print(list(range(10, 0, -2)))

    print("结合range()和len()函数以遍历一个序列的索引")
    list1 = ["a", "b", "c", "d"]
    dict1 = {}
    for x in list(range(len(list1))):
        dict1[x] = list1[x]
    print(dict1)


    print(list(range(2, 2)))

    print("""Python pass是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句，如下实例 """)
    '''
        当程序中有些地方不清楚具体的操作时可以先用pass代替，防止语法错误，比如：
        if True:
            pass
    '''
    #while 1:
    #    pass

    # 冒泡排序
    list2 = [2,456,7,6,987,2,64,0,-1,-52,-56,987]
    print(list2)
    a = 0
    c = range(len(list2))
    for i in c:
        d = range(i+1, len(list2))
        for x in d:
            if list2[i] > list2[x]:
                list2[i], list2[x] = list2[x], list2[i]
            a+=1
    print(list2)
    print(a)

