#一、针对序列的内置函数
#   1. list(sub) 把一个可迭代对象转换为列表
a=list()
print(a)    #[]

b='I love Lsgsh'
b=list(b)
print(b)    #['I', ' ', 'l', 'o', 'v', 'e', ' ', 'L', 's', 'g', 's', 'h']

c=(1,2,3,4,5)
c=list(c)
print(c)    #[1, 2, 3, 4, 5]

#   2. tuple(sub) 把一个可迭代对象转换为元组
d=tuple()
print(d)    #()

e='I love Lsgsh'
e=tuple(e)
print(e)    #('I', ' ', 'l', 'o', 'v', 'e', ' ', 'L', 's', 'g', 's', 'h')

f=(1,2,3,4,5)
f=tuple(f)
print(f)    #(1, 2, 3, 4, 5)

#   3.str(obj) 把obj对象转换为字符串
aa=123
g=str(aa)
print(g,type(g))    #123 <class 'str'>

#   4.len(s) 返回对象（字符、列表、元组等）长度或元素个数。
bb=list()
print(len(bb))  #0
cc=('I', ' ', 'L', 'o', 'v', 'e', ' ', 'L', 's', 'g', 'o', 'G', 'r', 'o', 'u', 'p')
print(len(cc))  #16
dd= 'I Love LsgoGroup'
print(len(dd)) # 16

#   5. max(sub) 返回序列或者参数集合中的最大值
print(max((1,2,3,4,5)))   #5
print(max(1,2,3,4,5))   #5
print(max([-88,99,3,7,43])) #99
print(max('Ilovwjdalkfj'))  #w

#   6. min(sub) 返回序列或参数集合中的最小值
print(min(1,2,3,4,5))   #1
print(min((1,2,3,4,5))) #1
print(min([-88,99,3,7,43])) #-88
print(min('Ilovwjdalkfj'))  #I

#   7. sum(iterable[, start=0]) 返回序列 iterable 与可选参数 start 的总和
print(sum([1,3,5,7,8]))     #24
print(sum((1,5,6,7,8)))     #27
# print(sum(1,5,6,7,8))   #TypeError: sum expected at most 2 arguments, got 5
print(sum([1,5,8,3,2],5))      #24
print(sum((1,6,9,6,3,3),5))     #33

#   8. sorted(iterable, key=None, reverse=False) 对所有可迭代的对象进行排序操作。
"""
a. iterable -- 可迭代对象。
b. key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代
对象中的一个元素来进行排序。
c. reverse -- 排序规则， reverse = True 降序 ， reverse = False 升序（默认）。
d. 返回重新排序的列表。
"""
x=[1,-4,6,9,10]     #[-4, 1, 6, 9, 10]
print(sorted(x))
#降序
print(sorted(x,reverse=True))   #[10, 9, 6, 1, -4]

y=({'age':20,"name":'a'},{'age':25,'name':'b'},{'age':10,'name':"c"})
print(type(y))      #<class 'tuple'>
z=sorted(y,key=lambda a:a['age'])   #按照age进行排序
print(z)    #[{'age': 10, 'name': 'c'}, {'age': 20, 'name': 'a'}, {'age': 25, 'name': 'b'}]

#   9. reversed(seq) 函数返回一个反转的迭代器。
    # a.seq--要转换的序列,可以使tuple,string,list或range
    #list
print(list(reversed([1,5,6,8,4])))    #[4, 8, 6, 5, 1]
str=list(reversed('djlafjla'))
    #string
print(str)   #['a', 'l', 'j', 'f', 'a', 'l', 'j', 'd']

str1=''.join(str)
print(str1)
    #tuple
print(tuple(reversed((1,5,6,8,4))))     #(4, 8, 6, 5, 1)
    #range
print(list(reversed(range(10))))  #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#   10.enumerate(sequence, [start=0])用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
seasons= ['Spring', 'Summer', 'Fall', 'Winter']
sea=list(enumerate(seasons))
print(sea)  #[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

sea1=list(enumerate(seasons,1))
print(sea1) #[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

for i,element in sea:
    print('{0},{1}'.format(i,element))  #第一次循环:0,Spring 第二次循环:1,Summer 第三次循环:2,Fall 第四次循环:3,Winter

#   11. zip(iter1 [,iter2 [...]])
"""
    a. 用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样
做的好处是节约了不少的内存。
    b. 我们可以使用 list() 转换来输出列表。
    c. 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为
    列表。
"""
aaa = [1, 2, 3]
bbb= [4, 5, 6]
ccc= [4, 5, 6, 7, 8]
zipped=zip(aaa,bbb)
print(zipped)       #<zip object at 0x0000024AA47ED608>
print(list(zipped))     #[(1, 4), (2, 5), (3, 6)]
zipped=zip(aaa,ccc)
print(list(zipped))     #[(1, 4), (2, 5), (3, 6)]

a1,b1=zip(*zip(aaa,bbb))
print(list(a1),list(b1))    #[1, 2, 3] [4, 5, 6]
a1,c1=zip(*zip(aaa,ccc))
print(list(a1),list(c1))    #[1, 2, 3] [4, 5, 6]



