# -*- coding:utf-8 -*-

'''
if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句

    python中if 后面的表达式 可以用小括号也可以不适用小括号
'''
if __name__ == "__main__":
    age = int(input("请输入你家狗狗年龄："))
    if(age <= 0):
        print("你家狗狗还没出生呢！😄")
    elif(age == 1):
        print("相当于人类14岁啦！")
    elif age == 2:
        print("相当于人类22岁啦！")
    elif age > 2:
        print("相当于人类：", 22+(age-2)*5)