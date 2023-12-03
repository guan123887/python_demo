t1=1,4,'python'
print(t1,type(t1))

#int
temp=(1)
print(type(temp))

#tuple
temp1=1,2,3,4
print(type(temp1))

#list
temp2=[]
print(type(temp2))

#tuple
temp3=()
print(type(temp3))

#tuple
temp4=(1,)
print(type(temp4))

#所以说(8)和(8,)不一样
print(8*(8))
print(8*(8,))

#创建二维元组
nested=(1,10.31,'python'),('data',11)
print(nested)


#更新一个数组
week=('Mon','Tues','Thurs','Fri')
week=week[:2]+('Wed',)+week[2:]
print(week)

t2=(1,2,3,[4,5,6])
print(t2)
t2[3][2]=10
#t2[2]=12  #报错
print(t2)

#删除一个元组

del t2
#print(t2)   #t2 is not defined

#元组比较
t3=(6,6,6,5,4,3,2,'python')
t4=(8,7,4,3,2,'hello')
print(t3<t4)


#内置方法
    #count() 统计指定值出现次数
print(t3.count(6))
    #index() 找到该元素在元组中的索引(第一次出现)
print(t3.index(6))
    #找索引2到4之间第一次出现6的索引
print(t3.index(6,2,4))

#解压(解构)一维元组
t5=(1,10,3,'python')
(a,b,c,_)=t5
print(a,b,c)

#解压(解构)二维元组
t6=(1,10,('python','OK'))
(a,b,(c,d))=t6
print(a,b,c,d)


#使用通配符*获取多个值  如何输出时加上*将会进行解构
t7=1,2,3,4,5,6
a,b,*rest,c=t7;
print(rest)


#以上也可以写成如下形式
t8=1,2,3,4,5,6
a,b,*_,c=t8;
print(a,b)
