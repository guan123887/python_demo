dic={
    'python':95,
    'java':99,
    'c':100
}

#   1.字典基本操作
#   a. 请修改'java' 这个key对应的value值为98
dic['java']=98
print(dic)  #{'python': 95, 'java': 98, 'c': 100}

#   b. 删除 c 这个key
dic.pop('c')
print(dic)  #{'python': 95, 'java': 98}

#   c. 增加一个key-value对，key值为 php, value是90
dic.setdefault('php',90)
print(dic)  #{'python': 95, 'java': 98, 'php': 90}

#   d. 获取所有的key值，存储在列表里
print(list(dic.keys())) #['python', 'java', 'php']

#   e. 获取所有的value值，存储在列表里
print(list(dic.values())) #[95, 98, 90]

#   f. 判断 javascript 是否在字典中
    #方法一:
if 'javascript' in dic:
    print('存在在字典里')
else:
    print('不存在在字典里')    #不存在在字典里

    #方法二:
    print(dic.get('javascript','不存在'))  #不存在

#   g. 获得字典里所有value的和
value=list(dic.values())
sum=0
for i in value:
    sum+=i;
print('字典所有value的和为',sum)   # 字典所有value的和为 283

#   h. 获取字典里最大的value
max=value[0]
for i in value[1:]:
    if i>max:
        max=i
    else:
        continue
print('字典里最大的value为',max)   #字典里最大的value为 98

#   i. 获取字典里最小的value
min=value[0]
for i in value[1:]:
    if i<min:
        min=i
    else:
        continue
print('字典里最小的value为',min)   #字典里最小的value为 90

#   j. 字典 dic1 = {'php': 97}， 将dic1的数据更新到dic中
dic1={'php':97}
dic.update(dic1)
print('更新后的字典为',dic)   #更新后的字典为 {'python': 95, 'java': 98, 'php': 97}