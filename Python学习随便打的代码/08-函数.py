#一、函数定义与函数调用
"""
1. 函数以 def 关键词开头，后接函数名和圆括号()。
2. 函数执行的代码以冒号起始，并且缩进。
3. return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None
"""

def functionName(str):
    print(str)
functionName('456')     #456

# 二、序列作为函数参数
def add(a,b):
    print(a+b)
add([1,2,3],[4,5,6])    #[1, 2, 3, 4, 5, 6]
add((1,2,3),(4,5,6))    #(1, 2, 3, 4, 5, 6)
# add(range(5),range(5))  #unsupported operand type(s) for +: 'range' and 'range'
add('abcdef','ghijkl')  #abcdefghijkl


#三、函数文档
def MyFirstFunction(name):
    "此处name是形参,表示占据一个参数位置"
    print('传递进来的{0}为实参,因为它是具体的参数值'.format(name))
print(MyFirstFunction.__doc__)  #此处name是形参,表示占据一个参数位置
MyFirstFunction('程序员')  #传递进来的程序员为实参,因为它是具体的参数值

#四、函数参数
"""
1. 位置参数 (positional argument)
2. 默认参数 (default argument)
3. 可变参数 (variable argument)
4. 关键字参数 (keyword argument)
5. 命名关键字参数 (name keyword argument)
6. 参数组合
"""
    # 1.位置参数
    #  arg1 - 位置参数 ，这些参数在调用函数 (call function) 时位置要固定。
def functionname(arg1):
    print(arg1)
functionname('你好啊') #你好啊

    #2.默认参数
    #1. arg2 = v - 默认参数 = 默认值，调用函数时，默认参数的值如果没有传入，则被认为是默认值。
    #2. 默认参数一定要放在位置参数 后面，不然程序会报错。
def functiona(arg1,arg2='我很好'):
    print(arg1,arg2,sep=',')
functiona('哈哈哈')    #哈哈哈,我很好

    #注意:1. Python 允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
def printInfo(name,age):
    print('Name: {0} Age:{1}'.format(name,age))
printInfo(age=20,name='哈哈哈')    #Name: 哈哈哈 Age:20

    #3.可变参数
    #可变参数就是传入的参数个数是可变的，可以是 0, 1, 2 到任意个，是不定长的参数。
"""
1. *args - 可变参数，可以是从零个到任意个，自动组装成元组。
2. 加了星号（*）的变量名会存放所有未命名的变量参数
"""
def functionb(arg1,*args):
    print(arg1) #20
    print(args) #(30, 50, 60, 70)
functionb(20,30,50,60,70)

    #4.关键字参数
    # **kw - 关键字参数，可以是从零个到任意个，自动组装成字典
def functionc(arg1,*args,**kw):
    print(arg1) #7
    print(args) #(4, 5, 3, 2, 1)
    print(kw)   #{'a': 3}
functionc(7,4,5,3,2,1,a=3)
    #比较:
"""
「可变参数」和「关键字参数」的同异总结如下：
1. 可变参数允许传入零个到任意个参数，它们在函数调用时自动组装为一个元组 (tuple)。
2. 关键字参数允许传入零个到任意个参数，它们在函数内部自动组装为一个字典 (dict)。
"""

    #5.命名关键字参数
"""
1. *, nkw - 命名关键字参数，用户想要输入的关键字参数，定义方式是在nkw 前面加个分隔符 *。
2. 如果要限制关键字参数的名字，就可以用「命名关键字参数」
3. 使用命名关键字参数时，要特别注意不能缺少参数名
"""
def functiond(arg1,*,nkw,**kw):
    print(arg1)    #30
    print(nkw)  #10
    print(kw)   #{'z': 1, 'b': 2}
functiond(30,nkw=10,z=1,b=2)    #自我认为命名关键字参数是为了防止nkw被当做**kw放进字典里

    #6.参数组合
"""
参数组合顺序:
1. 位置参数、默认参数、可变参数和关键字参数。
2. 位置参数、默认参数、命名关键字参数和关键字参数
"""
    #警告：虽然可以组合多达 5 种参数，但不要同时使用太多的组合，否则函数很难懂。

#五、函数的返回值
def add(a,b):
    return a + b;
print(add(1,2)) #3
print(add([1,2,3],[4,5,6])) #[1, 2, 3, 4, 5, 6]

def back():
    return [1,'小马的程序人生',3.14]

print(back())   #[1, '小马的程序人生', 3.14]


#6.变量作用域
"""
1. Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
2. 定义在函数内部的变量拥有局部作用域，该变量称为局部变量。
3. 定义在函数外部的变量拥有全局作用域，该变量称为全局变量。
4. 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问
"""

def discounts(price,rate):
    final_price=price*rate
    return final_price

# old_price=float(input('请输入原价:'))
# rate=float(input('请输入折扣率:'))
# new_price=discounts(old_price,rate)
# print('打折后的价格是:%.2f'%new_price) #88.20

    #注意 当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了。

num=1
def func1():
    global num  #使用global关键字声明
    print(num)  #1
    num=123
    print(num)  #123

func1()
print(num)  #123
    #内嵌函数
def outer():
    print('Outer函数在这被调用')   #Outer函数在这被调用
    def inner():
        print('Inner函数在这被调用')   #Inner函数在这被调用
    inner() #该函数只能在outer函数内部被调用
outer()

    #闭包
"""
1. 是函数式编程的一个重要的语法结构，是一种特殊的内嵌函数。
2. 如果在一个内部函数里对外层非全局作用域的变量进行引用，那么内部函数就被认为是闭包。
3. 通过闭包可以访问外层非全局作用域的变量，这个作用域称为 闭包作用域。
"""
def funX(x):
    def funY(y):
        return x*y
    return funY

i=funX(8)
print(type(i))    #<class 'function'>
print(i(5)) #40

    #如果要修改闭包作用域中的变量则需要 nonlocal 关键字
    # nonlocal用来修改不是全局作用域也不是局部作用域的变量的作用域
def outer():
    num=10  #100
    def inner():
        nonlocal num #nonlocal关键字声明
        num=100
        print(num)  #100
    inner()
    print(num)
outer()

    #递归
def factorial(n):
    if n==1:
        return 1
    return factorial(n-1)*n
print(factorial(10))   #3628800
    #斐波那契数列循环和递归
    #循环
i=0
j=1
lst=[i,j]
for k in range(2,11):
    k=i+j
    lst.append(k)
    i=j
    j=k
print(lst)  #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    #递归
lst1 = []
def recur_fibo(n):
    if n<=1:
        return n
    return recur_fibo(n-1)+recur_fibo(n-2)
for k in range(11):
    lst1.append(recur_fibo(k))
print(lst1) #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    #例子:设置递归的层数，Python默认递归层数为 100
import sys
sys.setrecursionlimit(1000)





