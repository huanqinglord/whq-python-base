# -*- coding:utf-8 -*-

'''
    x 为0~99的随机数，y 为1~199的随机数
    输出最大数，否则输出两数之和
'''
import random

if __name__ == "__main__":
    z = 1
while(z < 100):
    x = random.choice(range(100))
    y = random.choice(range(200))
    if(x>y):
        print(x)
    elif(x<y):
        print(y)
    else:
        print("两数相等：", x+y)
    z+=1