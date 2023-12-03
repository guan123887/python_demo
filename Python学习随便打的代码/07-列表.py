#创建一个列表

x=[2,5,4,3,6]
print(x,type(x))
#利用range()创建列表
y=list(range(10))
print(y,type(y))

#利用推导式创建列表
a=list(i for i in range(10,1,-2))
print(a,type(a))

b=list(0 for i in range(2,10,3))
print(b,type(b))


#注意指针引用的问题
#比如
d=[[0]*3]*4
#如果改变[0]为[1]
d[1][1]=1
print(d)
#判断列表是否可重复
c=[1,2,3,4,2]
print(c) #可重复

print((4,2)<(4,1))

e=[1,3,5,6,7,8,2]
e.sort(key=lambda a:a)
print(e)


#列表一种特殊情况
a=[0]*4;
print([a]*3)   #[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]