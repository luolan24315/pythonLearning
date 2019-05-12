# _*_coding: utf-8_*_
# Author:rongjinjin
# Time:20190512
# 进制转换

"""print("请输入数字")
number = input()
print(int(number,2)) #2进制转10进制
"""
print("输入10进制数字")
number = int(input())

binaryNum = bin(number)
#binaryNum[2:] #从第2位开始取值
print("2进制为",binaryNum)

octonaryNum = oct(number)
print("8进制为 ",octonaryNum)

hexadecimalNum = hex(number)
print("16进制为 ",hexadecimalNum)
