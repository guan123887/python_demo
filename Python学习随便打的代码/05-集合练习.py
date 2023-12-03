#1. 怎么表示只包含⼀个数字1的元组。
tu=(1,1,2,1,1,3,4,1)
print(tu)
zs=set(tu)
tu=tuple(zs)
print(tu)   #(1, 2, 3, 4)

#2. 创建一个空集合，增加 {‘x’,‘y’,‘z’} 三个元素。
s=set()
s.add('x')
s.add('y')
s.add('z')
print(s)    #{'y', 'x', 'z'}

#3. 列表['A', 'B', 'A', 'B']去重。
lst=['A', 'B', 'A', 'B']
zs=set(lst)
lst=list(zs)
print(lst)  #['A', 'B']

#4. 求两个集合{6, 7, 8}，{7, 8, 9}中不重复的元素.差集指的是两个集合交集外的部分。
a={6, 7, 8}
b={7, 8, 9}
    #方法一:
print(a^b)    #{9, 6}
    #方法二:
print(a.symmetric_difference(b))    #{9, 6}
    #方法三
a.symmetric_difference_update(b)
print(a)    #{9, 6}

#5. 求{'A', 'B', 'C'}中元素在 {'B', 'C', 'D'}中出现的次数。
c={'A', 'B', 'C'}
d={'B', 'C', 'D'}
print(len(c&d)) #2