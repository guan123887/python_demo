#一、匿名函数定义
"""
在 Python 里有两类函数：
1. 第一类：用 def 关键词定义的正规函数
2. 第二类：用 lambda 关键词定义的匿名函数
"""

"""
python 使用 lambda 关键词来创建匿名函数，而非 def 关键词，它没有函数名，其语法结构如下：
lambda argument_list: expression

1. lambda - 定义匿名函数的关键词。
2. argument_list - 函数参数，它们可以是位置参数、默认参数、关键字参数，和正规函数里的参数类型一样。
3. : - 冒号，在函数参数和表达式中间要加个冒号。
4. expression - 只是一个表达式，输入函数参数，输出一些值。
"""

"""
注意：
1. expression 中没有 return 语句，因为 lambda 不需要它来返回，表达式本身结果就是返回值。
2. 匿名函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
"""


#def和lambda一个简单的demo
def sqr(x):
    return x**2
print(sqr)  #<function sqr at 0x000002CA3D971EA0>
y=[sqr(x) for x in range(10)]
print(y)    #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

lbd_sqr=lambda x:x**2
print(lbd_sqr)  #<function <lambda> at 0x000002CA3DD17A60>
lbd_y=[lbd_sqr(x) for x in range(10)]
print(lbd_y)    #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

sumary=lambda arg1,arg2:arg1+arg2
print(sumary(10,20))    #30

func=lambda *args:sum(args)
print(func(3,4,5,6))    #18

#二、匿名函数的应用

"""
函数式编程 是指代码中每一块都是不可变的，都由纯函数的形式组成。这里的纯函数，是指函数本身相互独立、互不影
响，对于相同的输入，总会有相同的输出，没有任何副作用。
"""

    #例子1 非函数式编程
def f(x):
    for i in range(0,len(x)):
        x[i]+=10
    return x
x=[1,2,3]
f(x)
print(x)    #[11, 12, 13]

    #例子2 函数式编程  对比于以上例子，发现非函数式编程有输入变量的改变，下一次在输入此变量就发生了变化，不满足函数式编程定义
def f1(x):
    y=[]
    for item in x:
        y.append(item+10)
    return y
x1=[1,2,3]
f1(x1)
print(x1)   #[1, 2, 3]

"""
匿名函数 常常应用于函数式编程的高阶函数 (high-order function)中，主要有两种形式：
    1. 参数是函数 (filter, map)
    2. 返回值是函数 (closure)
"""
    #比如
    #filter(function, iterable) 过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
odd=lambda x: x%2==1
templist=filter(odd,[1,2,3,4,5,6,7,8,9])
print(list(templist))   #[1, 3, 5, 7, 9]

    #map(function, *iterables) 根据提供的函数对指定序列做映射。
m1=map(lambda x:x**2,[1,2,3,4,5,6])
print(list(m1)) #[1, 4, 9, 16, 25, 36]

m2=map(lambda x,y:x+y,[1,23,4],[5,6,7,8])
print(list(m2)) #[6, 29, 11]

    #除了 Python 这些内置函数，我们也可以自己定义高阶函数
def apply_to_list(fun,some_list):
    return fun(some_list)
lst=[1,2,3,4,5]
print(apply_to_list(sum,lst))   #15

print(apply_to_list(len,lst))   #5

print(apply_to_list(lambda x:sum(x)/len(x),lst))    #3.0

