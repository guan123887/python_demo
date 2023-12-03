#一、判断是否是可变类型
"""
1. 麻烦方法：用 id(X) 函数，对 X 进行某种操作，比较操作前后的 id ，如果不一样，则 X 不可变，如果一样，则
X 可变。
2. 便捷方法：用 hash(X) ，只要不报错，证明 X 可被哈希，即不可变，反过来不可被哈希，即可变。
"""

#方法1:
i=1
print(id(i))    #1383891056
i+=2
print(id(i))    #1383891120
#两者地址不一样 证明不可变

l=[1,2]
print(id(l))    #2513615965192
l.append('Python')
print(id(l))    #2513615965192
#两者地址一样 证明可变


#方法2:
print(hash('Name')) #-8539032447825160589
print(hash((1,2,'Python'))) #-7366572263238007615
#print(hash([1,2,'Python'])) #TypeError: unhashable type: 'list'

#print(hash({1,2,3}))    #TypeError: unhashable type: 'set'

#二、创建和访问字典
brand=['李宁','耐克','阿迪达斯']
slogan=['一切皆有可能','Just do it','Impossible is nothing']
print('耐克的口号是:',slogan[brand.index('耐克')])  #耐克的口号是 Just do it

dic={'李宁':'一切皆有可能','耐克':'Just do it','阿迪达斯':'Impossible is nothing'}
print('耐克的口号是:',dic['耐克'])  #耐克的口号是:Just do it

#如果我们取的键在字典中不存在，会直接报错 KeyError
dic1={1:'one',2:'two',3:'three'}
print(dic1);    #{1: 'one', 2: 'two', 3: 'three'}
print(dic1[1])  #one
#(dic1[4])  #KeyError: 4


dic2={'rice':35,'wheat':101,'corn':67}
print(dic2);    #{'rice': 35, 'wheat': 101, 'corn': 67}
print(dic2['rice']);    #35


#通过元组作为 key 来创建字典，但一般不这样使用
dic3={(1,2,3):'Tome','Age':12,3:[3,5,7]}
print(dic3,type(dic3))  #{(1, 2, 3): 'Tome', 'Age': 12, 3: [3, 5, 7]} <class 'dict'>


#通过dict()创建一个空的字典
dic4=dict()
dic4['a']=1;
dic4[2]='b';
dic4['c']=3;
print(dic4)     #{'a': 1, 2: 'b', 'c': 3}

#修改字典值
dic4[2]='d'
print(dic4)     #{'a': 1, 2: 'd', 'c': 3}

#dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs

dict5=dict([('apple',4139),('peach',4127),('cherry',4098)])
print(dict5)    #{'apple': 4139, 'peach': 4127, 'cherry': 4098}
#也可以这样写
dict6=dict((('apple',4139),('peach',4127),('cherry',4098)))
print(dict6)    #{'apple': 4139, 'peach': 4127, 'cherry': 4098}


#dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example:
dict(one=1, two=2)

dict7=dict(name='Tom',age=18)
print(dict7,type(dict7),sep=',')    #{'name': 'Tom', 'age': 18},<class 'dict'>

#三、字典的内置方法

#   1.dict.fromkeys(seq[, value]) 用于创建一个新字典,以序列 seq 中元素做字典的键,value 为字典所有键对应的初始值
seq=('name','age','sex');
print(type(seq))    #<class 'tuple'>
dict1=dict.fromkeys(seq);
print(type(dict1),'新的字典为:  %s'%str(dict1),sep=','); #<class 'dict'>,新的字典为:  {'name': None, 'age': None, 'sex': None}

dict2=dict.fromkeys(seq,10);
print('新的字典为: %s'%str(dict2))   #新的字典为: {'name': 10, 'age': 10, 'sex': 10}

dict3=dict.fromkeys(seq,('小马','8','男'))
print('新的字典为: %s'%str(dict3))   #新的字典为: {'name': ('小马', '8', '男'), 'age': ('小马', '8', '男'), 'sex': ('小马', '8', '男')}


#   2.dict.keys() 返回一个可迭代对象，可以使用 list() 来转换为列表，列表为字典中的所有键。
dict4={'Name':'lsgogroup','Age':7}
print(dict4.keys())   #dict_keys(['Name', 'Age'])
print(list(dict4.keys()))   #['Name', 'Age']

#   3.dict.values() 返回一个迭代器，可以使用 list() 来转换为列表，列表为字典中的所有值
dict5={'Sex':'female','Age':10,'Name':'Zera'}
print('字典所有值为: ',list(dict5.values()))      #字典所有值为:  ['female', 10, 'Zera']


#   4.. dict.items() 以列表返回可遍历的 (键, 值) 元组数组
print(dict5.items())    #dict_items([('Sex', 'female'), ('Age', 10), ('Name', 'Zera')])
print(tuple(dict5.items()))     #(('Sex', 'female'), ('Age', 10), ('Name', 'Zera'))

#   5.dict.get(key, default=None) 返回指定键的值，如果值不在字典中返回默认值
dict6={'Name':'HAHAHA','Age':60}
print(dict6.get('Name'))    #HAHAHA
# print(dict6.get(Name))      #name 'Name' is not defined
print(dict6.get('Ta','不存在'))    #不存在

#   6.dict.setdefault(key, default=None) 和 get() 方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值。
print(dict6.setdefault('Ta','被添加了'))    #被添加了
print(dict6)    #{'Name': 'HAHAHA', 'Age': 60, 'Ta': '被添加了'}


#   7.key in dict in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true ，否则返回 false 。而 not in 操作符刚好相反，如果键在字典 dict 里返回 false ，否则返回 true 。
dict7={'Name':'LsGroup','Age':15}

#   in 检测键Age   是否存在
if  'Age' in dict7:
    print('键 Age 存在')   #键 Age 存在
else:
    print('键 Age 不存在')

if 'Sex' in dict7:
    print('键 Sex 存在')
else:
    print('键 Sex 不存在')  #键 Sex 不存在


# not in 检测键 Age是否存在
if 'Ta' not in dict7:
    print('键 Ta 不存在')   #键 Ta 不存在
else:
    print('键 Ta 存在')


#   8.dict.pop(key[,default]) 删除字典给定键 key 所对应的值，返回值为被删除的值。 key 值必须给出。若 key不存在，则返回 default 值
dict8={1:'a',2:[1,2]}
print(dict8.pop(1),dict8)   #   a {2: [1, 2]}
#   注意: 设置默认值，必须添加，否则报错(因为key值为3不存在，不设置默认值无法返回默认值,所以报错)
print(dict8.pop(3,'nokey'),dict8)   #nokey {2: [1, 2]}

#   9.del dict[key] 删除字典给定键 key 所对应的值。
del dict8[2]
print(dict8)    #{}

#   10.dict.popitem() 随机返回并删除字典中的一对键和值(元组)，如果字典已经为空，却调用了此方法，就报出KeyError异常。
dict9={'Name':'Tom','Age':20}
print(dict9.popitem(),dict9)  #('Age', 20) {'Name': 'Tom'}

#   11.dict.clear() 用于删除字典内所有元素
dict10={'Name':'Terry','Age':25}
dict10.clear()
print(dict10)   #{}


#   12.dict.copy() 返回一个字典的浅复制
dict11={'Name':'Jerry','Age':2}
dict12=dict11.copy()
print(dict12)   #{'Name': 'Jerry', 'Age': 2}

dict13={'Name':'Jerry','Age':40,'children':{'Name':'La','Age':1}}
dict14=dict13.copy()
#   注意:以下输出children里面的value为不拷贝，引用，和dict13共用的一个地址
print(dict14)   #{'Name': 'Jerry', 'Age': 40, 'children': {'Name': 'La', 'Age': 1}}


#   特例:直接赋值和 copy 的区别
di1={'user':'lsGogroup','num':[1,2,3]}

# 引用对象(赋值)
di2=di1
#深拷贝父对象(一级目录),子对象(二级目录)不拷贝,还是引用
di3=di1.copy()

print(id(di1),id(di2),id(di3))  #2721541968880 2721541968880 2721541968736

#修改data数据
di1['user']='root'
di1['num'].remove(2)

print(di1)  #{'user': 'root', 'num': [1, 3]}
print(di2)  #{'user': 'root', 'num': [1, 3]}
print(di3)  #{'user': 'lsGogroup', 'num': [1, 3]}



#   13.dict.update(dict2) 把字典参数 dict2 的 key:value 对 更新到字典 dict 里
di4={'Name':'LSH','Age':7}
di5={'Sex':'female','Age':10}
di4.update(di5)
print('更新字典dict4: ',di4)    #更新字典dict4:  {'Name': 'LSH', 'Age': 10, 'Sex': 'female'}

