# coding: utf-8

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
n1 = 255
n2 = 1000
print(hex(n1),'and',hex(n2))





















