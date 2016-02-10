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
#1. for...in循环，依次把list或tuple中的每个元素迭代出来
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
students = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def by_name(t):
	
	
# from operator import itemgetter
# print(sorted(students, key=itemgetter(0)))
# print(sorted(students, key=lambda t: t[1]))
# print(sorted(students, key=itemgetter(1), reverse=True))























