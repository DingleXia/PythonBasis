# coding=utf-8

# 字符串常见操作

# find
mystr = 'hello python'
print mystr.find('python')
print mystr.find('python', 0, len(mystr))
print mystr.find('python', 7, len(mystr))

# index
mystr = 'hello python'
print mystr.index('python')
print mystr.index('python', 0, len(mystr))
# print mystr.index('python', 7, len(mystr))    # 跟find()方法一样，只不过如果str不在 mystr 中会报一个异常.

# count
mystr = 'hello python'
print mystr.count('o')
print mystr.count('python')

# replace
mystr = 'hello python'
print mystr.replace('python', 'world')
print mystr

# split
mystr = 'hello python ha ha'
print mystr.split(' ')
print mystr.split(' ', 2)

# capitalize
mystr = 'hello python'
print mystr.capitalize()

# title
mystr = 'hello python'
print mystr.title()

# startswith
mystr = 'hello python'
print mystr.startswith('hello')

# endswith
mystr = 'hello python'
print mystr.startswith('python')

# lower
mystr = 'HELLO PYTHON'
print mystr.lower()

# upper
mystr = 'hello python'
print mystr.upper()

# ljust
# 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
mystr = 'hello'
print mystr.ljust(10)

# rjust
# 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
mystr = 'hello'
print mystr.rjust(10)

# center
# 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
mystr = 'hello python'
print mystr.center(50)

# lstrip
# 删除 mystr 左边的空白字符
mystr = '      python'
print mystr.lstrip()

# rstrip
# 删除 mystr 字符串末尾的空白字符
mystr = 'hello      '
print mystr.rstrip()

# strip
# 删除mystr字符串两端的空白字符
mystr = '     hello python     '
print mystr.strip()

# rfind
# 类似于 find() 函数，不过是从右边开始查找
mystr = 'hello python'
print mystr.rfind('python', 6)

# rindex
# 类似于 index()，不过是从右边开始
mystr = 'hello python'
print mystr.rindex('python')

# partition
# 把mystr以str分割成三部分,str前，str和str后
mystr = 'hello the python'
print mystr.partition('the')

# rpartition
# 类似于 partition()函数,不过是从右边开始
mystr = 'hello the python'
print mystr.rpartition('the')

# splitlines
# 按照行分隔，返回一个包含各行作为元素的列表
mystr = 'hello\npython'
print mystr.splitlines()

# isalpha
# 如果 mystr 所有字符都是字母 则返回 True,否则返回 False
mystr = 'hello python'
print mystr.isalpha()
print 'hello'.isalpha()

# isdigit
# 如果 mystr 只包含数字则返回 True 否则返回 False.
mystr = 'hello python'
print mystr.isdigit()
print '123'.isdigit()

# isalnum
# 如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
mystr = 'hello2python'
print mystr.isalnum()

# isspace
# 如果 mystr 中只包含空格，则返回 True，否则返回 False.
mystr = '     '
print mystr.isspace()

# join
print ' '.join(['hello', 'python'])
