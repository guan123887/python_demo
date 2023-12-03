#1. 怎么找出序列中的最⼤、⼩值？
    # 以列表为例
lst=[1,5,7,8,4,3,3]     #8
print(max(lst)) #
#2. sort() 和 sorted() 区别
    #区别在于sort()只能用于列表，且无返回值，sorted()可用于任何可迭代对象，有返回值(列表)
lst.sort()
print(lst)  #[1, 3, 3, 4, 5, 7, 8]
lst1=[1,5,7,8,4,3,3]
print(sorted(lst1))     #[1, 3, 3, 4, 5, 7, 8]
tu=(1,3,4,5,6,43,2,2)
print(sorted(tu))       #[1, 2, 2, 3, 4, 5, 6, 43]
#3. 怎么快速求 1 到 100 所有整数相加之和？
print(sum(range(101)))  #5050
#4. 求列表 [2,3,4,5] 中每个元素的立方根。
import math
lst2=[2,3,4,5]
for i in range(len(lst2)):
    lst2[i]=math.pow(lst2[i],1/3)
print(lst2)     #[1.2599210498948732, 1.4422495703074083, 1.5874010519681994, 1.7099759466766968]
#5. 将[‘x’,‘y’,‘z’] 和 [1,2,3] 转成 [(‘x’,1),(‘y’,2),(‘z’,3)] 的形式。
ls=['x','y','z']
ls1=[1,2,3]
zipped=zip(ls,ls1)
print(list(zipped))       #[('x', 1), ('y', 2), ('z', 3)]