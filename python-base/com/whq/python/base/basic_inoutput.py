#encoding:utf-8
import math

if __name__=="__main__":
    print("练习python输入与输出")

    print("字符串格式化")
    #str()： 函数返回一个用户易读的表达形式。
    #repr()： 产生一个解释器易读的表达形式。

    print("输入平方立方表，同时靠左显示")
    for i in range(1, 11):
        #旧方式格式化字符串，其中%后面的数字代表每个参数占用多少字节，
        # 负号代表在后面用空格补充，正数代表在前面用空格补充
        print("%-2d %-3d %-4d" %(i, i**2, i **3))

    print("format方法格式化字符串")
    for i in range(1, 11):
        #>靠右， <靠左，^居中
        print("{0:>2d},{1:<3d},{2:^4d}".format(i, i**2, i**3))

    print("格式化指定参数位置")
    print("{0} {1}".format("a", "b"))
    print("{1} {1}".format("", "b"))

    print("关键字指定格式化对应参数（类似关键字函数）")
    print("{name} {age}".format(name="whq", age=1992))

    print("关键字与位置定位方式结合格式化字符串")
    print("{0:<5d}, {1:>5}, {name:^5}".format(0, 1, name="a"))

    print("'!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:")
    print("{!a} {!r} {!s} {!r}".format("a", "b", 1, 2))

    print("保留小数位数")
    print("{:.3f}".format(math.pi))
    #取前三位字符
    print("{:.3}".format("abcdef"))
    #没有.的时候保证至少有三个字节存放次参数，超过自动扩展
    print("{:3}".format("abcdef"))

    print("通过字典或者列表等实现字符串格式化")
    print("列表")
    list1 = list("abc")
    print("{0[0]}, {0[1]}, {0[2]}".format(list1))
    print("字典")
    dict1 = {}
    dict1[1] = "a"
    dict1["b"] = 2
    print(dict1)
    print("{0[1]}, {0[b]}".format(dict1))

