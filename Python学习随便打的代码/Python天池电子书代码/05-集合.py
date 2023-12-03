#   一、创建集合
#   1.集合的key不可重复
num={}
print(type(num))    #<class 'dict'>
num={1,2,3,4}
print(type(num))    #<class 'set'>

#   2.集合的创建
basket=set()
basket.add('apple')
basket.add('banana')
#   自动过滤重复元素
basket.add('apple')
print(basket)   #{'banana', 'apple'}

#   3.用 set(value) 工厂函数，把列表或元组转换成集合。
a=set('adajdhwo')
b=set(('Google','sjaldk','Taobao','Taobao'))
c=set(['Google','sjaldk','Taobao','Taobao'])
print(a)    #{'a', 'h', 'o', 'w', 'd', 'j'}
print(b)    #{'sjaldk', 'Google', 'Taobao'}
print(c)    #{'sjaldk', 'Google', 'Taobao'}

#   4.实例:. 去掉列表中重复的元素
    #方法一:
lst=[0,1,2,3,4,5,5,3,1]
temp=[]
for item in lst:
    if item not in temp:
        temp.append(item)
print(temp) #[0, 1, 2, 3, 4, 5]
    #方法二:
d=set(lst)
print(list(d))  #[0, 1, 2, 3, 4, 5]

#   二、访问集合的值
#   1.可以使用 len() 內建函数得到集合的大小。
thisset=set(['Google','Baidu','Taobao'])
print(len(thisset)) #3

#   2.使用 for 把集合中的数据一个个读取出来
for item in thisset:
    print(item) #第一次循环:Baidu  第二次循环:Google 第三次循环:Taobao

#   3.通过 in 或 not in 判断一个元素是否在集合中已经存在
print('Google' in thisset)  #True
print('taobao' in thisset)  #False

#  三、集合的内置方法
#   1. set.add(elmnt) 用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作。
fruits={'apple'}
fruits.add('apple')
print(fruits)   #{'apple'}
fruits.add('banana')
print(fruits)   #{'apple', 'banana'}

#   2.set.update(set) 用于修改当前集合，可以添加新的元素或集合到当前集合中，如果添加的元素在集合中已存在，则该元素只会出现一次，重复的会忽略。
x={'apple','banana'}
y={'apple','watermelon','strawberry'}
x.update(y)
print(x)    #{'watermelon', 'apple', 'banana', 'strawberry'}
x.update('dja',[1,2,3],(4,5,6))
print(x)    #{1, 2, 3, 'd', 4, 5, 6, 'watermelon', 'apple', 'strawberry', 'banana', 'a', 'j'}
#x.update(1) # print(x)  #TypeError: 'int' object is not iterable

#   3.set.remove(item) 用于移除集合中的指定元素。如果元素不存在，则会发生错误
x.remove(1)     #{2, 3, 4, 5, 6, 'banana', 'strawberry', 'apple', 'a', 'd', 'j', 'watermelon'}
print(x)
x.remove('d')
print(x)    #{1, 2, 3, 4, 5, 6, 'j', 'a', 'strawberry', 'apple', 'banana', 'watermelon'}

#   4. set.discard(value) 用于移除指定的集合元素。 remove() 方法在移除一个不存在的元素时会发生错误，而discard() 方法不会
x.discard(4)
print(x)    #{2, 3, 5, 6, 'watermelon', 'apple', 'strawberry', 'a', 'j', 'banana'}


#   5. set.pop() 用于随机移除一个元素
x.pop()
print(x)    #{3, 5, 6, 'apple', 'j', 'strawberry', 'a', 'banana', 'watermelon'}
#x.pop(3)   #不能这样写，提供任何参数

#   6.进行集合之间的数学操作
    #    set.intersection(set1, set2 ...) 返回两个集合的交集
n={'hello','world',1,2,3,4,7}
m={'world',7,9,0,10}
result=m.intersection(n)
print(result)   #{'world', 7}
    #  set1 & set2 返回两个集合的交集
result1=m&n
print(result1)  #{'world', 7}
    #  set.intersection_update(set1, set2 ...) 交集，在原始的集合上移除不重叠的元素
n.intersection_update(m)
print(n)    #{'world', 7}
    #   set.union(set1, set2...) 返回两个集合的并集
result3=m.union(n)
print(result3)  #{0, 7, 9, 10, 'world'}
    #   set1 | set2 返回两个集合的并集。
result4=m|n
print(result4)  #{0, 'world', 7, 9, 10}
    #   set.difference(set) 返回集合的差集
t={'hello','world',1,2,3,4,7}
y={'world',7,9,0,10}
result5=t.difference(y)
print(result5)  #{1, 2, 3, 4, 'hello'}
    #   set1 - set2 返回集合的差集。

result6=t-y
print(result6)  #{1, 2, 3, 4, 'hello'}
    #   set.difference_update(set) 集合的差集，直接在原来的集合中移除元素，没有返回值
t.difference_update(y)
print(t)    #{1, 2, 3, 4, 'hello'}
    #    set.symmetric_difference(set) 返回集合的异或
r={'hello','world',1,2,3,4,7}
e={'world',7,9,0,10}
result7=r.symmetric_difference(e)
print(result7)  #{0, 1, 2, 3, 4, 9, 10, 'hello'}
    #    set1 ^ set2 返回集合的异或
result8=r^e
print(result8)  #{0, 1, 2, 3, 4, 9, 10, 'hello'}
    #    set.symmetric_difference_update(set) 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
r.symmetric_difference_update(e)
print(r)    #{0, 1, 2, 3, 4, 9, 10, 'hello'}
    #    set.issubset(set) 判断集合是不是被其他集合包含，如果是则返回 True，否则返回 False。
q={1,4,6,7}
z={1,6}
print(q.issubset(z))   #False
print(z.issubset(q))    #True
    #    set1 <= set2 判断集合是不是被其他集合包含，如果是则返回 True，否则返回 False。
print(z<=q) #True
print(q<=z) #False
    #    set.issuperset(set) 用于判断集合是不是包含其他集合，如果是则返回 True，否则返回 False
print(q.issuperset(z))   #True
print(z.issuperset(q))    #false
    #    set1 >= set2 判断集合是不是包含其他集合，如果是则返回 True，否则返回 False
print(z >= q)  # False
print(q >= z)  # True

    #    set.isdisjoint(set) 用于判断两个集合是不是不相交，如果是返回 True，否则返回 False。
print(z.isdisjoint(q))  #False
v={2,5}
print(z.isdisjoint(v))  #True

#四、集合的转换
se = set(range(4))
li = list(se)
tu = tuple(se)
print(se, type(se)) # {0, 1, 2, 3} <class 'set'>
print(li, type(li)) # [0, 1, 2, 3] <class 'list'>
print(tu, type(tu)) # (0, 1, 2, 3) <class 'tuple'>

#五、 不可变集合
    # frozenset([iterable]) 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
ha=frozenset(range(10))
print(ha)    #frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
#ha.add('a') #AttributeError: 'frozenset' object has no attribute 'add'
hb=frozenset('djalfjwlfl')
print(hb)   #frozenset({'a', 'w', 'l', 'j', 'd', 'f'})

