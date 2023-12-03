#一、字符串定义
#字符串类型
t1='hello world'
print(t1,type(t1))  #hello world <class 'str'>


#字符串型数字相加
print('5'+'8')  #'58'

#转义字符实现单引号或者双引号
print('let\'s go')   #let's go


#使用r实现\不转义
print(r'C:\Program Files\Intel\Wifi\Help')   #C:\Program Files\Intel\Wifi\Help

#python  三引号实现字符串跨多行
para_str="""这是一个多行字符串 实例
我们可以用三个引号
来
实现
我们想要的
换行效果

"""

print(para_str)

#二、字符串切片
#字符串切片
str1='I love LsgoGroup';
print(str1[:6]);  #I love
print(str1[5])  #e
print(str1[:6]+'插入的字符串'+str1[6:])  #I love插入的字符串 LsgoGroup



str2='python'
print(str2[2:4])  #th
print(str2[-5:-2])  #yth
print(str2[2])  #t
print(str2[-1])  #n

#三、字符串常用内置方法
#字符串常用内置方法
s='xiaoxie'
s1='DAXIE'
s2='DFHyhu'
#将第一个字符大写
print(s.capitalize())  #Xiaoxie

"""
1.lower() 转换字符串中所有大写字符为小写。
2. upper() 转换字符串中的小写字母为大写。
3. swapcase() 将字符串中大写转换为小写，小写转换为大写。
"""
print(s1.lower())   #daxie
print(s.upper())   #XIAOXIE
print(s2.swapcase())   #dfhYHU


# count(str, beg= 0,end=len(string)) 返回 str 在 string 里面出现的次数
str3 = "DAXIExiaoxie"
print(str3.count('xi')) # 2

"""
1.endswith(suffix, beg=0, end=len(string)) 检查字符串是否以指定子字符串 suffix 结束
如果是，返回True,否则返回 False。如果 beg 和 end 指定值，则在指定范围内检查
"""

str4 = "DAXIExiaoxie"
print(str4.endswith('ie')) # True
print(str4.endswith('xi')) # False

"""
2.startswith(substr, beg=0,end=len(string)) 检查字符串是否以指定子字符串 substr 开头
如果是，返回True，否则返回 False。如果 beg 和 end 指定值，则在指定范围内检查。
"""

print(str4.startswith('Da')) # False
print(str4.startswith('DA')) # True

"""
1. find(str, beg=0, end=len(string)) 检测 str 是否包含在字符串中，
如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含，
返回开始的索引值，否则返回 -1。
"""
str2 = "DAXIExiaoxie"
print(str2.find('xi')) # 5
print(str2.find('ix')) # -1


#2. rfind(str, beg=0,end=len(string)) 类似于` find() 函数，不过是从右边开始查找。
print(str2.rfind('xi')) # 9


#isnumeric() 如果字符串中只包含数字字符，则返回 True，否则返回 False。
str5='sj'
str6='1234'
print(str5.isnumeric(),str6.isnumeric(),sep=',')   #False,True

"""
1. ljust(width[, fillchar]) 返回一个原字符串左对齐，并使用 fillchar
（默认空格）填充至长度 width 的新字符串。
"""
str6='1101'
print(str6.ljust(8,'0'))  #8位左对齐，不足用0填充    #11010000


"""
2. rjust(width[, fillchar]) 返回一个原字符串右对齐，并使用 fillchar
（默认空格）填充至长度 width 的新字符串。
"""
print(str6.rjust(8,'0'))  #8位右对齐，不足用0填充    #00001101


"""
1. lstrip([chars]) 截掉字符串左边的空格或指定字符。
2. rstrip([chars]) 删除字符串末尾的空格或指定字符。
3. strip([chars]) 在字符串上执行 lstrip() 和 rstrip()
"""
str7='   I love shanghai   ';
print(str7.lstrip())  #'I love shanghai'
print(str7.rstrip())  #'   I love shanghai'
print(str7.strip())   #'I love shanghai'
print(str7.lstrip().strip('I'))   # ' love shanghai'
print(str7.strip().strip('i'))   #'I love shangha'

"""
1. partition(sub) 找到子字符串sub，把字符串分为一个三元组 (pre_sub,sub,fol_sub) ，如果字符串中不包含
  sub则返回 ('原字符串','','') 。
2. rpartition(sub) 类似于 partition() 方法，不过是从右边开始查找。
"""
str8 = ' I Love LsgoGroup '
print(str8.strip().partition('o'),type(str8.strip().partition('o')))  #('I L', 'o', 've LsgoGroup') <class 'tuple'>
print(str8.strip().partition('m'))  #('I Love LsgoGroup', '', '')
print(str8.partition('m'))  #(' I Love LsgoGroup ', '', '')
print(str8.strip().rpartition('o')) #('I Love LsgoGr', 'o', 'up')
print(str8.rpartition('o')) #(' I Love LsgoGr', 'o', 'up ')

#replace(old, new [, max]) 把 将字符串中的 old 替换成 new ，如果 max 指定，则替换不超过 max 次。
str9='  I love tangjingfeng  '
print(str9.replace(' ','',3))  #替换不超过3次  #'Ilove tangjingfeng  '

"""
split(str="", num) 不带参数默认是以空格为分隔符切片字符串，如果 num 参数有设置，则仅分隔 num 个子字符
串，返回切片后的子字符串拼接的列表。
"""

st1='I love  tang';
st2='I, nihao , hello';
print(st1.split(),type(st1.split()));     #['I', 'love', 'tang'] <class 'list'>
print(st2.split(','));  #['I', ' nihao ', ' hello']

u = "www.baidu.com.cn"
print(u.split())    #['www.baidu.com.cn']
print(u.split('.')) #['www', 'baidu', 'com', 'cn']
print(u.split('.',1))   #以.分隔1次 ['www', 'baidu.com.cn']
# 分割两次，并取序列为1(第二项)的项（因为返回的是一个列表）
print((u.split(".", 2)[1])) #baidu
#解构(解包)
u1, u2, u3 = u.split(".", 2)
print(u1,u2,u3,sep=',') #www,baidu,com.cn

#去掉换行付
u2="""
say
hello
haha
"""
#提取需要的信息
print(u2.split('\n')[1:len(u2.split('\n'))-1])   #['say', 'hello', 'haha']

"""
splitlines([keepends]) 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为
False，不包含换行符，如果为 True，则保留换行符。  默认为False
"""
string='I \n Love \n LsgoGroup'
print(string.splitlines())  #['I ', ' Love ', ' LsgoGroup']
print(string.splitlines(True))  #['I \n', ' Love \n', ' LsgoGroup']


"""
1.maketrans(intab, outtab) 创建字符映射的转换表，第一个参数是字符串，表示需要转换的字符，第二个参数也
是字符串表示转换的目标。
2. translate(table, deletechars="") 根据参数 table 给出的表，转换字符串的字符，要过滤掉的字符放
到 deletechars 参数中。
"""
string1='this is string example....wow!!!'
intab='aeiou'
outtab='12345'
trantab=str.maketrans(intab,outtab);
print(trantab); #{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
print(string1.translate(trantab));  #th3s 3s str3ng 2x1mpl2....w4w!!!


#四、字符串格式化
#位置参数
sf='{0} Love {1}'.format('I','Lsgogroup');
print(sf);  #'I Love Lsgogroup'

#关键字参数
sf1="{a} Love {b}".format(a='I',b='lSGOGROUP');
print(sf1); #I Love lSGOGROUP

#位置参数要在关键字参数之前
sf2="{0} Love {b}".format('I',b='tangjingfeng');
print(sf2); #I Love tangjingfeng

#保留小数点后两位
sf3="{0:.2f}{1}".format(27.568,'GB')    #保留小数点后两位
print(sf3)  #27.57GB

print('%d'%97)  #97
print('%c %c %c'%(97,98,99))    #a b c
print('%d+%d=%d'%(4,5,9))   #4+5=9
print('我叫%s 今年%d岁'%('小明',10))   #我叫小明 今年10岁
print('%o'%10)  #12
print("%x"%10)  #a
print("%X"%10)  #A
print("%f"%27.658)  #27.658000
print("%e"%27.658)  #2.765800e+01
print("%E"%27.658)  #2.765800E+01
print("%g"%27.658)  #%g根据值的大小决定使用%f或%e  #27.658
text='I am %d years old.'%22
print('I said: %s'%text)    #'I said: I am 22 years old.
print('I said: %r'%text)   #%r格式化字符串,用rper()方法处理对象  #"I said: 'I am 22 years old.'"









