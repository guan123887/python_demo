# 1.上面提到了许多魔法方法，如__new__ , __init__ , __str__ , __rstr__ , __getitem__ , __setitem__ 等等，请
# 总结它们各自的使用方法。
"""
1.__new__:  __new__ 是在一个对象实例化的时候所调用的第一个方法，在调用__init__ 初始化前，先调用__new__
2.__init__:构造器，当一个实例被创建的时候调用的初始化方法
3. __str__: 当你打印一个对象的时候，触发__str__   当你使用%s 格式化的时候，触发__str__   str 强转数据类型的时候，触发__str__
4.__rstr__:repr 是str 的备胎   有__str__ 的时候执行__str__ ,没有实现__str__ 的时候，执行__repr__   repr(obj) 内置函数对应的结果是__repr__ 的返回值   当你使用%r 格式化的时候 触发__repr__
5.算术运算符、反算术运算符、增量赋值运算符、一元运算符
6.__getattr__(self, name) : 定义当用户试图获取一个不存在的属性时的行为。
7.__getattribute__(self, name) ：定义当该类的属性被访问时的行为（先调用该方法，查看是否存在该属性，若不存在，接着去调用__getattr__ ）。
8.__setattr__(self, name, value) ：定义当一个属性被设置时的行为。
9.__delattr__(self, name) ：定义当一个属性被删除时的行为。
10.__getitem__(self, key):  定义获取容器中元素的行为，相当于self[key].
11.__setitem__(self, key, value):  定义设置容器中指定元素的行为，相当于self[key] = value。
12.__delitem__(self, key): 定义删除容器中指定元素的行为，相当于del self[key] 。
13.__len__(self): 定义当被len() 调用时的行为（返回容器中元素的个数）。
14.__get__(self, instance, owner) 用于访问属性，它返回属性的值。
15.__set__(self, instance, value) 将在属性分配操作中调用，不返回任何内容。
16.__del__(self, instance) 控制删除操作，不返回任何内容。
17._iter__ : 定义当迭代容器中的元素的行为，返回一个特殊的迭代器对象， 这个迭代器对象实现了__next__() 方法并通过 StopIteration 异常标识迭代的完成。
18.__next__() : 返回下一个迭代器对
"""



"""
2. 利用python做一个简单的定时器类
要求:
a. 定制一个计时器的类。
b. start 和stop 方法代表启动计时和停止计时。
c. 假设计时器对象t1 ， print(t1) 和直接调用t1 均显示结果。
d. 当计时器未启动或已经停止计时时，调用stop 方法会给予温馨的提示。
e. 两个计时器对象可以进行相加： t1+t2 。
f. 只能使用提供的有限资源完成。
"""

import time

class Timer:
    def __init__(self):
        self.__info = '计时未开始！'
        self.__begin = None
        self.__end = None
        self.__bg = 0

    def __str__(self):
        return self.__info

    def __repr__(self):
        return self.__info

    def __add__(self, other):
        return '共运行了%.2f s' %(self.__bg + other.__bg)

    def start(self):
        print('计时开始！')
        self.__begin = time.localtime()

    def stop(self):
        if not self.__begin:
            print("计时器未启动！")
            return
        self.__end = time.localtime()
        self.__bg = time.mktime(self.__end)- time.mktime(self.__begin)
        self.__info = '共运行了%.2f s'%(self.__bg)
        self.__begin = None
        print('计时结束！')
        return self.__info

t1 = Timer()
print(t1) # 计时未开始！
t1
t1.stop() # 计时器未启动！
t1.start()  # 计时开始！
time.sleep(5)
print(t1.stop()) # 计时结束！ 共运行了5.00 s
t1.stop()  # t1.stop()
t2 = Timer()
t2.start()
time.sleep(2)
t2.stop()
print(t1 + t2)  # 共运行了7.00 s