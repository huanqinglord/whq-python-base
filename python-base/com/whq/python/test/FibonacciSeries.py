# -*- coding:utf-8 -*-

'''
    斐波那契数列，下一个数为前两个数之和
'''
if __name__ == "__main__":
    a, b = 0, 1
    while(b<10):
        a, b = b, a+b
        #print(b)
        print(b, end=" ")