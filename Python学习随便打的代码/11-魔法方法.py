"""
魔法方法总是被双下划线包围，例如 __init__ 。
魔法方法是面向对象的 Python 的一切，如果你不知道魔法方法，说明你还没能意识到面向对象的 Python 的强大。
魔法方法的“魔力”体现在它们总能够在适当的时候被自动调用。
魔法方法的第一个参数应为 cls （类方法） 或者 self （实例方法）。
1. cls ：代表一个类的名称
2. self ：代表一个实例对象的名称
"""

#一、基本的魔法方法
    #   1.__init__(self[,...]    构造器, 当一个实例被创建的时候调用的初始化方法
class Rectangle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getPeri(self):
        return (self.x+self.y)*2
    def getArea(self):
        return self.x*self.y

rect=Rectangle(4,5)
print(rect.getPeri())   #18
print(rect.getArea())   #20

    #   2.__new__(cls[, ...])
"""
1. __new__ 是在一个对象实例化的时候所调用的第一个方法，在调用 __init__ 初始化前，先调用 __new__ 。
2. __new__ 至少要有一个参数 cls ，代表要实例化的类，此参数在实例化时由 Python 解释器自动提供，后面的参数直
接传递给 __init__ 。
3. __new__ 对当前类进行了实例化，并将实例返回，传给 __init__ 的 self 。但是，执行了 __new__ ，并不一定会
进入 __init__ ，只有 __new__ 返回了，当前类 cls 的实例，当前类的 __init__ 才会进入。
"""
    #例子1
class A(object):
    def __init__(self,value):
        print('into A __init__')
        self.value=value
    def __new__(cls,*args,**kwargs):
        print('into A __new__')
        print(cls,'cls',args,'*args',kwargs,'*kwargs')    #输出要实例化的类
        return object.__new__(cls)  #返回当前类的实例
class B(A):
    def __init__(self,value):
        print('into B __init__')
        self.value=value
    def __new__(cls,*args,**kwargs):
        print("into B __new__");
        print(cls,'cls')    #输出要实例化的类
        return super().__new__(cls,*args,**kwargs)  #调用类的__new__

b=B(10)
"""
输出:
into B __new__
<class '__main__.B'> cls
into A __new__
<class '__main__.B'> cls (10,) *args {} *kwargs
into B __init__
"""
    #例子2
class AA(object):
    def __init__(self):
        print('into AA __init__')
        self.value=value

    def __new__(cls,*args,**kwargs):
        print('into AA __new__')
        print(cls)
        return object.__new__(cls)

class BB(AA):
    def __init__(self,value):
        print('into BB __init__');
        self.value=value

    def __new__(cls, *args, **kwargs):
        print('into BB __new__')
        print(cls)
        return super().__new__(AA,*args,**kwargs)    #改变cls为AA

bb=BB(10)
"""
输出:
into BB __new__
<class '__main__.BB'>
into AA __new__
<class '__main__.AA'>
"""

"""
    1. 若 __new__ 没有正确返回当前类 cls 的实例，那 __init__ 是不会被调用的，即使是父类的实例也不行，将没
    有 __init__ 被调用。
    2. 可利用 __new__ 实现单例模式。
"""
    #比如
class Earth:
    pass
a=Earth()
print(id(a))    #2780775081520
b=Earth()
print(id(b))    #2780775081744

class Earth:
    __instance=None #定义一个类属性做判断
    def __new__(cls):
        if cls.__instance is None:
            # __new__(cls) 传哪个class的cls  返回的就是创建的该class的实例
            cls.__instance=object.__new__(cls)
            print('cls.__instance', cls.__instance)  # cls.__instance <__main__.Earth object at 0x0000018486E98508>
            return cls.__instance
        else:
            return cls.__instance
a=Earth()
print(id(a))    #2780775081184
b=Earth()
print(id(b))    #2780775081184

"""
1. __new__ 方法主要是当你继承一些不可变的 class 时（比如 int, str, tuple ）， 提供给你一个自定义这些类的实
例化过程的途径。
"""
class CapStr(str):
    def __new__(cls,string):
        string=string.upper()
        return str.__new__(cls,string)

a=CapStr('I love lsgogroup')
print(a)    #I LOVE LSGOGROUP

class CapInt(int):
    def __new__(cls,intValue):
        intValue=intValue+10
        return int.__new__(cls,intValue)

b=CapInt(20)
print(b)    #30

"""
2.析构器 __del__(self)
析构器，当一个对象将要被系统回收之时调用的方法
    Python 采用自动引用计数（ARC）方式来回收对象所占用的空间，当程序中有一个变量引用该 Python 对象时，Python 
    会自动保证该对象引用计数为 1；当程序中有两个变量引用该 Python 对象时，Python 会自动保证该对象引用计数为 2，
    依此类推，如果一个对象的引用计数变成了 0，则说明程序中不再有变量引用该对象，表明程序不再需要该对象，因此
    Python 就会回收该对象。
    大部分时候，Python 的 ARC 都能准确、高效地回收系统中的每个对象。但如果系统中出现循环引用的情况，比如对象
    a 持有一个实例变量引用对象 b，而对象 b 又持有一个实例变量引用对象 a，此时两个对象的引用计数都是 1，而实际上
    程序已经不再有变量引用它们，系统应该回收它们，此时 Python 的垃圾回收器就可能没那么快，要等专门的循环垃圾
    回收器（Cyclic Garbage Collector）来检测并回收这种引用循环。
"""
    #比如
class C(object):
    def __init__(self):
        print('into C __init__')
    def __del__(self):
        print('into C __del__')

c1 = C() # into C __init__
c2 = c1
c3 = c2
del c3 # into C __del__
del c2
del c1

"""
3. __str__ 和 __repr__
__str__(self) :
1. 当你打印一个对象的时候，触发__str__
2. 当你使用%s 格式化的时候，触发__str__
3. str 强转数据类型的时候，触发__str__
__repr__(self):
1. repr 是str 的备胎
2. 有__str__ 的时候执行__str__ ,没有实现__str__ 的时候，执行__repr__
3. repr(obj) 内置函数对应的结果是__repr__ 的返回值
4. 当你使用%r 格式化的时候 触发__repr__
"""


class Cat:
    """定义一个猫类"""
    def __init__(self, new_name, new_age):
        """在创建完对象之后 会自动调用, 它完成对象的初始化的功能"""
        self.name = new_name
        self.age = new_age
    def __str__(self):
        """返回一个对象的描述信息"""
        return "名字是:%s , 年龄是:%d" % (self.name, self.age)
    def __repr__(self):
        """返回一个对象的描述信息"""
        return "Cat:(%s,%d)" % (self.name, self.age)
    def eat(self):
        print("%s在吃鱼...." % self.name)
    def drink(self):
        print("%s在喝可乐..." % self.name)
    def introduce(self):
        print("名字是:%s, 年龄是:%d" % (self.name, self.age))

# 创建一个对象
tom = Cat("汤姆", 30)
print(tom)
print(str(tom))
print(repr(tom)) # Cat:(汤姆,30)
tom.eat() # 汤姆在吃鱼....
tom.introduce() # 名字是:汤姆, 年龄是:30

## __str__(self) 的返回结果可读性强。也就是说， __str__ 的意义是得到便于人们阅读的信息，就像下面的 '2019-10-11' 一样。
## __repr__(self) 的返回结果应更准确。怎么说， __repr__ 存在的目的在于调试，便于开发者使用。

import datetime
today = datetime.date.today()
print(str(today)) # 2022-06-10
print(repr(today)) # datetime.date(2022, 6, 10)
print('%s' %today) # 2022-06-10
print('%r' %today) # datetime.date(2022, 6, 10)

"""
4. 算术运算符 类型工厂函数，指的是不通过类而是通过函数来创建对象。
"""

class C:
    pass

print(type(list)) # <class 'type'>
print(type(tuple)) # <class 'type'>
print(type(C)) # <class 'type'>
print(int('123'))  # 123

# 这个例子中list工厂函数把一个元组对象加工成了一个列表对象。
print(list((1, 2, 3))) # [1, 2, 3]

# 1. __add__(self, other) 定义加法的行为： +
# 2. __sub__(self, other) 定义减法的行为： -

class MyClass:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
    # 两个对象的长相加，宽不变.返回一个新的类
    def __add__(self, others):
        return MyClass(self.height + others.height, self.weight + others.weight)
    # 两个对象的宽相减，长不变.返回一个新的类
    def __sub__(self, others):
        return MyClass(self.height - others.height, self.weight - others.weight)
    # 说一下自己的参数
    def intro(self):
        print("高为", self.height, " 重为", self.weight)

def main():
    a = MyClass(height=10, weight=5)
    a.intro()
    b = MyClass(height=20, weight=10)
    b.intro()
    c = b - a
    c.intro()
    d = a + b
    d.intro()

if __name__ == '__main__':
    main()  #高为 10  重为 5  高为 20  重为 10  高为 10  重为 5  高为 30  重为 15

# 1. __mul__(self, other) 定义乘法的行为： *
# 2. __truediv__(self, other) 定义真除法的行为： /
# 3. __floordiv__(self, other) 定义整数除法的行为： //
# 4. __mod__(self, other) 定义取模算法的行为： %
# 5. __divmod__(self, other) 定义当被 divmod() 调用时的行为
# 6. divmod(a, b) 把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b) 。

print(divmod(7, 2)) # (3, 1)
print(divmod(8,2)) # (4, 0)

# 1. __pow__(self, other[, module]) 定义当被 power() 调用或 ** 运算时的行为
# 2. __lshift__(self, other) 定义按位左移位的行为： <<
# 3. __rshift__(self, other) 定义按位右移位的行为： >>
# 4. __and__(self, other) 定义按位与操作的行为： &
# 5. __xor__(self, other) 定义按位异或操作的行为： ^
# 6. __or__(self, other) 定义按位或操作的行为： |

"""
5. 反算术运算符  反运算魔方方法，与算术运算符保持一一对应，不同之处就是反运算的魔法方法多了一个“r”。当文件左操作不支持相应的操作时被调用。
"""

# 1. __radd__(self, other) 定义加法的行为： +
# 2. __rsub__(self, other) 定义减法的行为： -
# 3. __rmul__(self, other) 定义乘法的行为： *
# 4. __rtruediv__(self, other) 定义真除法的行为： /
# 5. __rfloordiv__(self, other) 定义整数除法的行为： //
# 6. __rmod__(self, other) 定义取模算法的行为： %
# 7. __rdivmod__(self, other) 定义当被 divmod() 调用时的行为
# 8. __rpow__(self, other[, module]) 定义当被 power() 调用或 ** 运算时的行为
# 9. __rlshift__(self, other) 定义按位左移位的行为： <<
# 10. __rrshift__(self, other) 定义按位右移位的行为： >>
# 11. __rand__(self, other) 定义按位与操作的行为： &
# 12. __rxor__(self, other) 定义按位异或操作的行为： ^
# 13. __ror__(self, other) 定义按位或操作的行为： |

# 这里加数是a ，被加数是b ，因此是a 主动，反运算就是如果a 对象的__add__() 方法没有实现或者不支持相应的操
# 作，那么 Python 就会调用b 的__radd__() 方法。
class Nint(int):
    def __radd__(self, other):
        return int.__sub__(other, self) # 注意 self 在后面

a = Nint(5)
b = Nint(3)
print(a + b) # 8
print(1 + b) # -2
print(b + 1) # 4

"""
6. 增量赋值运算符
1. __iadd__(self, other) 定义赋值加法的行为： +=
2. __isub__(self, other) 定义赋值减法的行为： -=
3. __imul__(self, other) 定义赋值乘法的行为： *=
4. __itruediv__(self, other) 定义赋值真除法的行为： /=
5. __ifloordiv__(self, other) 定义赋值整数除法的行为： //=
6. __imod__(self, other) 定义赋值取模算法的行为： %=
7. __ipow__(self, other[, modulo]) 定义赋值幂运算的行为： **=
8. __ilshift__(self, other) 定义赋值按位左移位的行为： <<=
9. __irshift__(self, other) 定义赋值按位右移位的行为： >>=
10. __iand__(self, other) 定义赋值按位与操作的行为： &=
11. __ixor__(self, other) 定义赋值按位异或操作的行为： ^=
12. __ior__(self, other) 定义赋值按位或操作的行为： |=
"""
a = 3
a *= 4
print(a) # 12

"""
7.一元运算符
1. __neg__(self) 定义正号的行为： +x
2. __pos__(self) 定义负号的行为： -x
3. __abs__(self) 定义当被abs() 调用时的行为
4. __invert__(self) 定义按位求反的行为： ~x
"""
b = -3
print(-b)  # 3


"""
8. 属性访问
__getattr__ ， __getattribute__ ， __setattr__ 和__delattr__
__getattr__(self, name) : 定义当用户试图获取一个不存在的属性时的行为。
__getattribute__(self, name) ：定义当该类的属性被访问时的行为（先调用该方法，查看是否存在该属性，若不存
在，接着去调用__getattr__ ）。
__setattr__(self, name, value) ：定义当一个属性被设置时的行为。
__delattr__(self, name) ：定义当一个属性被删除时的行为。
"""
class C:
    def __getattribute__(self, item):
        print('__getattribute__')
        return super().__getattribute__(item)
    def __getattr__(self, item):
        print('__getattr__')
    def __setattr__(self, key, value):
        print('__setattr__')
        super().__setattr__(key, value)
    def __delattr__(self, item):
        print('__delattr__')
        super().__delattr__(item)
c = C()
c.x  #  # __getattribute__  __getattr__

c.x = 1   # __setattr__
del c.x   # __delattr__


""""
9. 描述符 描述符就是将某种特殊类型的类的实例指派给另一个类的属性。
1. __get__(self, instance, owner) 用于访问属性，它返回属性的值。
2. __set__(self, instance, value) 将在属性分配操作中调用，不返回任何内容。
3. __del__(self, instance) 控制删除操作，不返回任何内容。
"""
class MyDecriptor:
    def __get__(self, instance, owner):
        print('__get__', self, instance, owner)
    def __set__(self, instance, value):
        print('__set__', self, instance, value)
    def __delete__(self, instance):
        print('__delete__', self, instance)
class Test:
    x = MyDecriptor()

t = Test()
t.x  #  __get__ <__main__.MyDecriptor object at 0x0000028FA7E72F48> <__main__.Test object at 0x0000028FA7E72888> <class '__main__.Test'>
t.x = 'x-man'  # __set__ <__main__.MyDecriptor object at 0x0000022EB1842948> <__main__.Test object at 0x0000022EB1847108> x-man
del t.x  # __delete__ <__main__.MyDecriptor object at 0x0000022EB1842948> <__main__.Test object at 0x0000022EB1847108>


"""
10.定制序列   协议（Protocols）与其它编程语言中的接口很相似，它规定你哪些方法必须要定义。然而，在 Python 中的协议就显得不那
么正式。事实上，在 Python 中，协议更像是一种指南。

容器类型的协议
1. 如果说你希望定制的容器是不可变的话，你只需要定义__len__() 和__getitem__() 方法。
2. 如果你希望定制的容器是可变的话，除了__len__() 和__getitem__() 方法，你还需要定义__setitem__()
和__delitem__() 两个方法。
"""


# 编写一个不可改变的自定义列表，要求记录列表中每个元素被访问的次数。
class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        self.count[item] += 1
        return self.values[item]

c1 = CountList(1,3,5,7,9)
c2 = CountList(2,4,6,8,10)
print(c1[1])   # 3
print(c2[2])  # 6
print(c1[1] + c2[1])  # 7

print(c1.count)  # {0: 0, 1: 2, 2: 0, 3: 0, 4: 0}

print(c2.count)  # {0: 0, 1: 1, 2: 1, 3: 0, 4: 0}

# 1. __len__(self) 定义当被len() 调用时的行为（返回容器中元素的个数）。
# 2. __getitem__(self, key) 定义获取容器中元素的行为，相当于self[key] 。
# 3. __setitem__(self, key, value) 定义设置容器中指定元素的行为，相当于self[key] = value 。
# 4. __delitem__(self, key) 定义删除容器中指定元素的行为，相当于del self[key] 。


# 编写一个可改变的自定义列表，要求记录列表中每个元素被访问的次数。
class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)
    def __len__(self):
        return len(self.values)
    def __getitem__(self, item):
        self.count[item] += 1
        return self.values[item]
    def __setitem__(self, key, value):
        self.values[key] = value
    def __delitem__(self, key):
        del self.values[key]
        for i in range(0, len(self.values)):
            if i >= key:
                self.count[i] = self.count[i + 1]
        self.count.pop(len(self.values))

c1 = CountList(1,3,5,7,9)
c2 = CountList(2,4,6,8,10)
print(c1[1])  # 3
print(c2[1])  # 4
c2[2] = 12
print(c1[1] + c2[2])  # 15
print(c1.count) # {0: 0, 1: 2, 2: 0, 3: 0, 4: 0}\
print(c2.count)  # {0: 0, 1: 1, 2: 1, 3: 0, 4: 0}

del c1[1]
print(c1.count)  # {0: 0, 1: 0, 2: 0, 3: 0}

"""
11.迭代器
1. 迭代是 Python 最强大的功能之一，是访问集合元素的一种方式。
2. 迭代器是一个可以记住遍历的位置的对象。
3. 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
4. 迭代器只能往前不会后退。
5. 字符串，列表或元组对象都可用于创建迭代器：
"""

string = 'lsgogroup'
for c in string:
    print(c)   # l s g o g r o u p

for c in iter(string):
    print(c)  # l s g o g r o u p

links = {'B': '百度', 'A': '阿里', 'T': '腾讯'}
for each in links:
    print('%s -> %s' % (each, links[each]))  # B -> 百度 A -> 阿里 T -> 腾讯

for each in iter(links):
    print('%s -> %s' % (each, links[each]))  # B -> 百度 A -> 阿里 T -> 腾讯

# 1. 迭代器有两个基本的方法： iter() 和 next() 。
# 2. iter(object) 函数用来生成迭代器。
# 3. next(iterator[, default]) 返回迭代器的下一个项目。
# 4. iterator -- 可迭代对象
# 5. default -- 可选，用于设置在没有下一个元素时返回该默认值，如果不设置，又没有下一个元素则会触发
# StopIteration 异常。

links = {'B': '百度', 'A': '阿里', 'T': '腾讯'}
it = iter(links)
print(next(it)) # B
print(next(it)) # A
print(next(it)) # T
# print(next(it)) # StopIteration

it = iter(links)
while True:
    try:
        each = next(it)  # B A T
    except StopIteration:
        break
    print(each)

# 把一个类作为一个迭代器使用需要在类中实现两个魔法方法 __iter__() 与 __next__() 。
# 1. __iter__(self) 定义当迭代容器中的元素的行为，返回一个特殊的迭代器对象， 这个迭代器对象实现了
# __next__() 方法并通过 StopIteration 异常标识迭代的完成。
# 2. __next__() 返回下一个迭代器对象。
# 3. StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完
# 成指定循环次数后触发 StopIteration 异常来结束迭代。

class Fibs:
    def __init__(self, n = 10):
        self.a = 0
        self.b = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.a , self.b = self.b, self.a+self.b
        if self.a > self.n:
            raise StopIteration
        return self.a

fibs = Fibs(100)
for each in fibs:
    print(each, end= ' ')


"""
12. 生成器
1. 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
2. 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
3. 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下
一次执行 next() 方法时从当前位置继续运行。
4. 调用一个生成器函数，返回的是一个迭代器对象。
"""

def myGen():
    print('生成器执行')
    yield 1
    yield 2

myG = myGen()  # 生成器执行
print(next(myG))  # 1

print(next(myG))  # 2
# print(next(myG))  # StopIteration

myG = myGen()
for each in myG:
    print(each)  # 生成器执行  1  2

# 用生成器实现斐波那契数列。
def libs(n):
    a = 0
    b = 1
    while True:
        a,b = b, a+b
        if a > n:
            return
        yield a

for each in libs(100):
    print(each, end = ' ')  # # 1 1 2 3 5 8 13 21 34 55 89

