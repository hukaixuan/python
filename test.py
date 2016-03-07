#!/usr/bin/env python3
#coding: utf-8

# ##判断
# height = float(input('你的身高为：'))
# weight = float(input('你的体重为：'))

# bmi = weight / (height*height)

# if bmi<18.5:
# 	print('您的体重过轻')
# elif bmi>=18.5 and bmi<25:
# 	print('您的体重正常')
# elif bmi>=25 and bmi<28:
# 	print('过重')
# elif bmi>=28 and bmi<32:
# 	print('肥胖')
# else:
# 	print('严重肥胖')



#循环
#1. for...in循环，依次把list(列表)或tuple(初始化后就不可更改的list)中的每个元素迭代出来
# names = ['hukaixuan','xiaohong','xiogdd','jack','胡凯旋']
# for name in names:
# 	print(name)
# #计算从0加到100的和 Python一定要注意缩进格式
# sum = 0
# for x in range(101):
# 	sum = sum + x
# print(sum)

#2.while循环
#计算0-100内所有奇数的和
# sum = 0
# n = 99
# while n>0:
# 	sum += n
# 	n = n-2
# print(sum)


#dict =其他语言的map
# d = {'Michal':89, 'Bob':79, 'Kacey':96}
# name = input('请输入你要查询成绩的人名：')
# # if name in d:
# # 	print(d[name])
# # else:
# # 	print('没有这个人')	
# # 等同于下面代码 哈哈，一行顶四行
# print(d.get(name,'没有这个人')) #get方法根据key取出value，若不存在，返回第二个参数
# name = input('你想要删除的同学的信息')
# d.pop(name)
# print('删除后的dict为',d)

#set 只存key的集合，没有重复值
# s = set([3,4,1,6])
# print(s)
# s.add(9)
# s.remove(1)
# print(s)


#函数
#abs()求绝对值 max()参数可以任意多个
#数据类型转换 int() float() str() bool()
#hex() int->16进制
# n1 = 255
# n2 = 1000
# print(hex(n1),'and',hex(n2))

# import math
# def quadratic(a, b, c):
# 	x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
# 	x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
# 	return x1,x2
# 
# a = float( input('计算ax*x+bx+c=0的解，请输入参数a='))
# b = float( input('b='))
# c = float( input('c='))
# if b*b-4*a*c<0:
# 	print('方程无解')
# else:
# 	print('方程的解为',quadratic(a,b,c))

# 递归
#汉诺塔问题
# def hanno(n, a, b, c):
# 	if n==1:
# 		print(a,'  --> ',c)
# 		return
# 	else:
# 		hanno(n-1, a, c, b)
# 		hanno(1, a, b, c)
# 		hanno(n-1, b, a, c)
# n = int(input('请输入汉诺塔的层数:'))
# print(hanno(n, 'a', 'b', 'c'))
# def move(n, a, b, c):
#     if n == 1:
#         print('move', a, '-->', c)
#         return
#     move(n-1, a, c, b)
#     print('move', a, '-->', c)
#     move(n-1, b, a, c)

# move(4, 'a', 'b', 'c')



#高级特性

#切片
# L = [4,2,56,12,7,22,68]
# L = list(range(100))
# print('原数列：',L)
# print('第四到第六个元素',L[3:6])
# print('倒数第一个元素',L[-1])
# print('倒数三个元素',L[-3:])
# print('原样复制的',L[:])
# # tuple切片 
# T = tuple(range(10))
# print('切片前：',T)
# T = T[3:7]
# print('切片后：',T)
#字符串也可以看作是一种list，每个元素就是一个字符，也可进行切片操作
# print('salfjdeDSsaaS'[5:11])

#迭代
# from collections import Iterable
# print(isinstance('abc',Iterable))
# print(isinstance([1,2,3],Iterable))
# print(isinstance(123,Iterable))
#  利用enumerate函数把一个list变成索引-元素对
# for i,value in enumerate(['pp','lsd','kace','bob']):
# 	print(i, value)
#同时引用两个变量
# for x, y in [(1, 1), (2, 4), (3, 9)]:
# 	print(x, y)	

#列表生成式
# L1 = ['Hello', 'world', 21, 'KacEy', None, 'Apple']
# L2 = [s.lower() for s in L1 if isinstance(s, str)]
# print(L2)
#生成器 generator
# g = (x*x for x in range(20) if x%2==0)  #列表生成式与生成器的区别仅在[],()
# for n in g:
# 	print(n)

# #斐波那契数列
# def fib(max):
# 	n, a, b = 0, 0, 1
# 	while n<max:
# 		# print(b)
# 		yield b
# 		a, b = b, a+b
# 		n = n+1
# 	return 'done'
# # print(fib(20))
# for n in fib(20):
# 	print(n)

#高阶函数 Higher-order function
#1.变量可以指向函数
# f = abs
# print(f)
# print(f(-23))
#2.函数名完全相同
#不能 abs = 10 
#     abs(-10)
#3.传入函数  (编写高阶函数，就是让函数的参数能够接收别的函数)
# def add(x, y, f):
# 	return f(x)+f(y)
# print(add(-5, 6, abs))

##Google三驾马车：google file system， mapreduce， bigtable
##Python内置map()映射 reduce()化简 函数，
# def f(x):
# 	return x*x*x
# l = [1,3,45,22,45,23,6]
# r = map(f, l) #利用map操作一个列表
# print(r)
# print(list(r))
# print(l);  #每个元素都是被独立操作的，而原始列表没有被更改，因为这里创建了一个新的列表来保存新的答案。这就是说，Map操作是可以高度并行的
# print(list(map(str, l)))  #将所有数字转化为字符串
## reduce操作相当于 reduce(f, [x1, x2, x3, x4]) = f( f( f(x1,x2),x3 ),x4 )
#from functools import reduce 
# def str2int(s):     #自己实现int()函数
# 	def fn(x, y):
# 		return x*10 + y
# 	def char2num(s):
# 		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# 	return reduce(fn, map(char2num, s))
# print(isinstance(str2int('432'), int) )

# def normalize(name):
# 	return name.lower().capitalize() #转换成只有首字母大写的名字
# L1 = ['adam','LIsA','bartT']
# print( list( map(normalize, L1) ) )

# from functools import reduce 
# def prod(L): #可以接收一个list求乘积
# 	def multi(x1, x2):
# 		return x1*x2 
# 	return reduce(multi, L)
# print('3*5*7*9=', prod([3,5,7,9]))

# from functools import reduce 
# n = 0.1
# def str2float(s):
# 	def fn(x, y):
# 		if y == '.':
# 			x = float(x)
# 			return x
# 		if isinstance(x, int):
# 			return x*10+y
# 		elif isinstance(x, float):
# 			global n
# 			result = x+y*n
# 			n = n*0.1
# 			return result
# 	def char2num(s):
# 		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.':'.'}[s]
# 	return reduce( fn, map(char2num,s) )
# print('str2float(\'125.215\') = ', str2float('125.215'))

##filter求素数
###埃氏筛法
# def _odd_iter(): #奇数序列（生成器，无限数列）
# 	n = 1
# 	while True:
# 		n = n+2 
# 		yield n 
# def _not_divisible(n):
# 	return lambda x: x%n>0 #返回不能被n整除的数
# def primes():
# 	yield 2 
# 	it = _odd_iter()
# 	while True:
# 		n = next(it)
# 		yield n 
# 		it = filter(_not_divisible(n), it)
# for n in primes():
# 	if n < 1000:
# 		print(n)
# 	else:
# 		break
# def is_palindrome(n):   #得回数
# 	flag = True
# 	n = str(n)
# 	length = len(n)
# 	for x in range(0, length//2):
# 		if n[x] != n[-x-1]:
# 			flag = False
# 	return flag
# output = filter(is_palindrome, range(1,1000))  #由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。
# print(list(output)) 

##sorted
#print( sorted([23,52,1,-22,4,-95], key=abs, reverse=True) )
# print( sorted(['bob','Duck','kacey','Tommy','Zoo'],key=str.lower))
# students = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88),('zra',76)]
# def by_name(t):
# 	return t[0]
# def by_score(t):
# 	return t[1]
# print( sorted(students,key=by_name) )
# L2 = sorted(students, key=by_score, reverse=True)
# print(L2)
	
# from operator import itemgetter
# print(sorted(students, key=itemgetter(0)))
# print(sorted(students, key=lambda t: t[1]))
# print(sorted(students, key=itemgetter(1), reverse=True))

##函数作为返回值
# def lazy_sum(*args):
# 	def sum():
# 		ax = 0 
# 		for n in args:
# 			ax = ax + n 
# 		return ax 
# 	return sum     #函数作为返回值
# ##用例
# f = lazy_sum(1,4,25,19,2)
# print(f)   #function lazy_sum.(locals).sum at 0x008c8c00
# print(f())  #调用的时候才进行运算
# ##相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
# ##返回的函数并没有立刻执行，而是直到调用了f()才执行
# ##返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# def count():
# 	def f(j):
# 		def g():
# 			return j*j
# 		return g
# 	fs = []
# 	for i in range(1, 4):
# 		fs.append(f(i))
# 	return fs 
# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())

##匿名函数 lambda 只能有一个表达式，不用写return，返回值就是该表达式的结果
##装饰器  本质上，decorator就是一个返回函数的高阶函数
#定义装饰器
# def log(func):
# 	def wrapper(*args, **kw):
# 		print('call %s():' %func.__name__)
# 		return func(*args, **kw)
# 	return wrapper
# #使用装饰器
# @log    ##把@log放在函数定义处，相当于执行语句 now = log(now)
# def now():
# 	print('2016/2/11')
# now()
##装饰器本身需要传入参数的情况
# import functools
# def log(text):
# 	def decorator(func):
# 		@functools.wraps(func)    
# 		def wrapper(*args, **kw):   #*args表示任何多个无名参数，它是一个tuple**kwargs表示关键字参数，它是一个dict
# 			print('%s %s():' %(text, func.__name__))
# 			return func(*args, **kw)
# 		return wrapper
# 	return decorator
# @log('execute')
# def now():     #now = log('execute')(now)
# 	print('2016/2/11')
# now()
# print(now.__name__)

# import functools
# def log(func):
# 	@functools.wraps(func)
# 	def wrapper(*args, **kw):
# 		print('begin call');
# 		f = func(*args, **kw)
# 		print('end call')
# 		return f
# 	return wrapper
# @log 
# def f():
# 	print('hello world!')
# f()


# #偏函数 function.partial帮助我们创建一个偏函数
# import functools
# int2 = functools.partial(int, base=2)    #相当于创建了这么一个函数    def int2(x, base=2):                                                  return int(x, base)
# print( int2('100100') )   
# #相当于
# print( int('100100',base=2))


##模块和包
###__init__.py

##pip install

##面向对象编程
# class Student(object):
# 	def __init__(self, name, score):
# 		self.name = name 
# 		self.__score = score   #双下划线开头的是私有变量   单下划线开头表示虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”   以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，
# 	def print_score(self):
# 		print('%s: %s' %(self.name, self.score))
# 	def get_grade(self):
# 		if self.score>=90:
# 			return 'A'
# 		elif self.score>=60:
# 			return 'B'
# 		else:
# 			return 'C'

# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# print(bart.get_grade())
# lisa.print_score()
# print(lisa.get_grade())
# bart.age = 8  ###和静态语言不同，Python允许对实例变量绑定任何数据，
# print(bart.age)

# print(bart.__score)  # 错误
# print(bart._Student__score)  ##可以访问到，但是不建议
 
##判断类型 type()
##dir() 获得一个对象的所有属性和方法


# ##一般情况下，类的实例可以绑定任何属性和方法
# class Student(object):
# 	pass 

# s = Student()
# s.name = 'Michael'  #绑定属性
# print(s.name)

# def set_age(self, age):
# 	self.age = age 
# from types import MethodType
# s.set_age = MethodType(set_age, s)  #绑定方法
# s.set_age(25)
# print(s.age)
# ##为了给所有实例都绑定方法，可以给class绑定方法：
# def set_score(self, score):
# 	self.score = score 

# Student.set_score = MethodType(set_score, Student)

# s.set_score(89)
# print(s.score)

# ###限定实例的属性，定义__slots__变量
# class Student(object):
# 		__slots__ = ('name', 'age')  #用tuple定义允许绑定的属性名称

# s = Student()
# s.name = 'Michael'
# s.age = 21
# # s.score = 67   ##错误：‘student’ object has no attribute 'score'

# ##使用@property
# class Screen(object):
# 	@property
# 	def width(self):
# 	    return self._width
# 	@width.setter
# 	def width(self, value):
# 		self._width = value
# 	@property
# 	def height(self):
# 	    return self._height
# 	@height.setter
# 	def height(self, value):
# 		self._height = value
# 	@property
# 	def resolution(self):
# 	    return self._height*self._width
	

# s = Screen()
# s.width = 1024
# s.height = 768
# print(s.height)
# print(s.resolution)

# ##Mixln

# ##定制类
## __slots__ 
## __len__()
## __str__

# class Student(object):
# 	def __init__(self, name):
# 		self.name = name 
# 	def __str__(self):
# 		return 'Student object (name: %s)' %self.name 
# 	__repr__ = __str__ 
# print(Student('Michael'))

##__iter__
##类想用于for...in 循环，必须实现__iter__()方法，该方法返回一个迭代对象
##然后for循环不断调用该迭代对象的__next__()方法拿到循环的下一个值，知道
##遇到StopIteration错误时退出循环
##斐波那契数列
# class Fib(object):
# 	def __init__(self):
# 		self.a, self.b = 0, 1 ##初始化两个计数器a，b
# 	def __iter__(self):
# 		return self    #实例本身就是迭代对象，故返回自己
# 	def __next__(self):
# 		self.a, self.b = self.b, self.a+self.b  #计算下一个值
# 		if self.a >100000:
# 			raise StopIteration()
# 		return self.a
# 	def __getitem__(self, n):
# 		a, b = 1, 1 
# 		for x in range(n):
# 			a, b = b, a+b 
# 		return a 
# 	def __call__(self):
# 		print('我是Fib函数，你在调用我干嘛？')
# # for n in Fib():
# # 	print(n)

# ##实现__getitem__(),才能像list一样按照下标取出元素
# f = Fib()
# print( f[100] )

# ##__getattr__ 动态返回一个属性, 动态调用

# ##__call__ 方法，可以直接对实例进行调用
# f()
# ##完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别



##Enum
# from enum import Enum

# Month = Enum('Month', ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec') )

# print(Month.Jun.value)
# for name, member in Month.__members__.items():
# 	print(name, '=>', member, ',', member.value)

##元类metaclass是Python中非常具有魔术性的对象，它可以改变类创建时的行为。这种强大的功能使用起来务必小心。
##调试 print assert logging pdb pdb.set_trace()
 

##  IO
## 同步IO  CPU等待
## 异步IO  CPU不等待   同步和异步的区别就在于是否等待IO执行的结果
## 文件读写
# try:
# 	f = open('E:\python/testIO.txt','r')
# 	print(f.read())
# finally:
# 	if f:
# 		f.close()
###等同于：
# with open('E:/python/testIO.txt','r') as f:
# 	print(f.read(2))   ##read() read(size) readline() readlines()

##像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object
##读取二进制文件，如图片，视频等等， 用 'rb' 模式打开
##字符编码， 给open() 函数传入encoding参数,如读取GBK编码的文件：encoding = 'gbk'
##编码不规范，可以errors='ignore'掉

##写入
# with open('E:\python/testIO.txt','w',encoding='utf-8') as f:
# 	f.write('你好，世界！')   #使用with语句操作文件IO是个好习惯。

# StringIO 在内存中读写str
# from io import StringIO
# f = StringIO()  ##创建一个StringIO
# for i in range(1,11):
# 	f.write('%d.hello world\n' %i)
# print(f.getvalue())
# f = StringIO('Hello\nHi\nGoodbye')
# while True:
# 	s = f.readline()
# 	if s == '':
# 		break
# 	print(s.strip())

## BytesIO  内存中读写二进制数据 bytes
# from io import BytesIO
# f = BytesIO()
# f.write('中文&english'.encode('utf-8'))
# print(f.getvalue())
# f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(f.read())

##操作文件和目录
# import os
# os.name 
# os.uname() ##windows 下不支持
# os.environ #环境变量
# os.environ.get('key')  #获得某个环境变量的值
# print(os.path.abspath('.'))  #查看当前目录的绝对路径
# os.path.join('E:\python','')  #拼接路径
# os.path.split()  #拆分路径，后一部分总是最后级别的目录和文件名
# os.path.splitext()  #得到文件的扩展名

# os.rename('testIO.txt','testFile')
# os.remove()

##shutil模块提供了copyfile()函数，该模块的很多函数可以看作os模块的补充
# print([x for x in os.listdir('.') if os.path.isdir(x)])  #列出当前目录下的所有目录
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py' ])

# from datetime import datetime
# import os

# pwd = os.path.abspath('.')

# print('      Size     Last Modified  Name')
# print('------------------------------------------------------------')

# for f in os.listdir(pwd):
#     fsize = os.path.getsize(f)
#     mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
#     flag = '/' if os.path.isdir(f) else ''
#     print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

##把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
##在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
##把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

# import pickle  ##pickle模块实现序列化
# d = dict(name='Bob', age=20, score=93)
# # print( pickle.dumps(d) ) ##pickle.dumps()把任意对象序列化为一个bytes
# with open('E:\python/testFile','wb') as f:
# 	pickle.dump(d, f)   #pickle.dump()直接把对象序列化后写入一个file-like Object
# with open('E:\python/testFile','rb') as f:
# 	d = pickle.load(f)
# print(d)

# ##JSON
# import json
# d = dict(name='Bob',age=20,score=88)
# print(json.dumps(d))   #返回一个标准JSON格式的str（序列化）
# json_str = '{"age": 18, "score": 75, "name": "Kacey"}'
# print( json.loads(json_str) )   #反序列化

##普通对象的序列化
# import json
# class Student(object):
# 	pass
# s = Student()
# s.name='Kacey'
# s.age='21'
# print(json.dumps(s, default=lambda obj:obj.__dict__))

##正则表达式
##直接给出字符，精确匹配
##\d 匹配一个数字    \w 匹配一个字母
## . 匹配任意字符
## * 匹配任意个字符（包括0个）
## + 至少一个字符
## ？0个或1个字符 
##{n}表示n个字符
##{n,m} 表示n-m个字符
##\s 匹配一个空格（包括Tab等空白符）
##
##eg:  \d{3}\s+\d{3,8}  三个数字+至少一个空格+三到八个数字
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##





