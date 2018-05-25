# coding=utf-8

# raw_input() 会把用户输入的任何值都作为字符串来对待
a = raw_input()     # 1 + 2
print a, type(a)    # 1 + 2 <type 'str'>
# input() 接受表达式输入，并把表达式的结果赋值给等号左边的变量
b = input()         # 1 + 2
print b, type(b)    # 3 <type 'int'>


