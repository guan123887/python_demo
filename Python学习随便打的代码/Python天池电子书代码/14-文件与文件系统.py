#coding:utf-8
"""
1. 打开文件
1. open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
Open file and return a stream. Raise OSError upon failure.
a. file : 必需，文件路径（相对或者绝对路径）。
b. mode : 可选，文件打开模式
c. buffering : 设置缓冲
d. encoding : 一般使用utf8
e. errors : 报错级别
f. newline : 区分换行符

常见的mode 如下表所示：
'r' 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
'w'
打开一个文件只用于写入。
如果该文件已存在则打开文件，并从开头开始编辑。
即原有内容会被删除。
如果该文件不存在，创建新文件。
'x' 写模式，新建一个文件，如果该文件已存在则会报错。
'a'
追加模式，打开一个文件用于追加。
如果该文件已存在，文件指针将会放在文件的结尾。
也就是说，新的内容将会被写入到已有内容之后。
如果该文件不存在，创建新文件进行写入。
'b' 以二进制模式打开文件。一般用于非文本文件，如：图片。
't' 以文本模式打开（默认）。一般用于文本文件，如：txt。
'+' 可读写模式（可添加到其它模式中使用）
"""

f = open('将进酒.txt', mode='r',encoding='UTF-8')
print(f)  # <_io.TextIOWrapper name='将进酒.txt' mode='r' encoding='UTF-8'>
for each in f:
    print(each)

"""
2. 文件对象方法
"""
# 1. fileObject.close() 用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作， 否则会触发ValueError错误。
f = open('将进酒.txt', 'r')
print('FileName:', f.name) # FileName: 将进酒.txt
f.close()

# 2. fileObject.read([size]) 用于从文件读取指定的字符数，如果未给定或为负则读取所有。
f = open('将进酒.txt', 'r', encoding='utf-8')
line = f.read(20)
print("读取的字符串: %s" % line)  # 读取的字符串: 君不见，黄河之水天上来，奔流到海不复回。
f.close()

# 3. fileObject.readline() 读取整行，包括 "\n" 字符。
f = open('将进酒.txt', 'r', encoding='utf-8')
line = f.readline()
print("读取的字符串: %s" % line)  # 读取的字符串: 君不见，黄河之水天上来，奔流到海不复回。
f.close()

# 4. fileObject.readlines() 用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。
f = open('将进酒.txt', 'r', encoding='utf-8')
lines = f.readlines()
print(lines)

"""
['君不见，黄河之水天上来，奔流到海不复回。\n', '君不见，高堂明镜悲白发，朝如青丝暮成雪。\n', '人生得意须尽欢，莫使金樽空对月。\n', '天生我材必有用，千金散尽还复来。\n', '烹羊宰牛且为乐，会须一饮三百杯。\n', '岑夫子，丹丘生，将进酒，杯莫停。\n', '与君歌一曲，请君为我倾耳听。\n', '钟鼓馔玉不足贵，但愿长醉不复醒。\n', '古来圣贤皆寂寞，惟有饮者留其名。\n', '陈王昔时宴平乐，斗酒十千恣欢谑。\n', '主人何为言少钱，径须沽取对君酌。\n', '五花马，千金裘，呼儿将出换美酒，与尔同销万古愁。']
君不见，黄河之水天上来，奔流到海不复回。
"""

for each in lines:
    each.strip()  # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
    print(each)

f.close()

# 5.fileObject.tell() 返回文件的当前位置，即文件指针当前位置。
f = open('将进酒.txt', 'r', encoding='utf-8')
line = f.readline()
print(line)
pos = f.tell()
print(pos)  # 62  中文字符*3(包括逗号) 结尾\r\n 2个 20*3+2=62
f.close()


# 6.fileObject.seek(offset[, whence]) 用于移动文件读取指针到指定位置。
"""
# a. offset ：开始的偏移量，也就是代表需要移动偏移的字节数，如果是负数表示从倒数第几位开始。
# b. whence ：可选，默认值为 0。给 offset 定义一个参数，表示要从哪个位置开始偏移；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。
"""
f = open('将进酒.txt', 'r', encoding='utf-8')
line = f.readline()
print(line)  # 君不见，黄河之水天上来，奔流到海不复回。

line = f.readline()
print(line)  # 君不见，高堂明镜悲白发，朝如青丝暮成雪。

f.seek(0, 0)  # 第一个参数：move to the 1st character from the start of the file(-表示从最后移动)  第二个参数为移动到参考点位置
line = f.readline()  # 君不见，黄河之水天上来，奔流到海不复回。
print(line)

f.close()

# 7.fileObject.write(str) 用于向文件中写入指定字符串，返回的是写入的字符长度。

f = open('workfile.txt', 'wb+')
print(f.write(b'0123456789abcdef'))  # 16
print(f.seek(5))  # 5
print(f.read(1))    # b'5'
print(f.seek(-3,2)) # 13
print(f.read(1))    # b'd'

"""
在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。
如果文件打开模式带b ，那写入文件内容时， str （参数）要用encode 方法转为bytes 形式，否则报
错： TypeError: a bytes-like object is required, not 'str' 。
"""

str = '...'  #  文本 = Unicode字符序列  相当于 string 类型

str = b'...'  #  文本 = 八位序列(0到255之间的整数)  字节文字总是以‘b’或‘B’作为前缀；它们产生一个字节类型的实例，而不是str类型。  相当于 byte[]


f = open('将进酒.txt', 'r+', encoding='UTF-8')
str = '\n作者: 李白'
f.seek(0, 2)  # 2表示从文件末尾算起。
line = f.write(str)
f.seek(0,0)
for each in f:
    print(each)
f.close()

# 8.with语句
"""
一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。
关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行它的清理方法。
"""

# 以下代码执行完毕后，就算在处理过程中出问题了，文件 f 总是会关闭。
# try:
#     f = open('myfile.txt', 'w')
#     for line in f:
#         print(line)
# except OSError as error:
#     print('出错啦!%s'% str(error))
# finally:
#     f.close()

# try:
#     with open('myfile.txt', 'w') as f:
#         for line in f:
#             print(line)
# except OSError as error:
#     print('出错啦!%s' %str(error))


"""
9. OS模块中关于文件、目录常用的函数
我们所知道常用的操作系统就有：Windows，Mac OS，Linu，Unix等，这些操作系统底层对于文件系统的访问工作原理是
不一样的，因此你可能就要针对不同的系统来考虑使用哪些文件系统模块……，这样的做法是非常不友好且麻烦的，因为
这样就意味着当你的程序运行环境一改变，你就要相应的去修改大量的代码来应对。
有了OS（Operation System）模块，我们不需要关心什么操作系统下使用什么模块，OS模块会帮你选择正确的模块并调
用。
"""

# 1. os.getcwd() 用于返回当前工作目录。
# 2. os.chdir(path) 用于改变当前工作目录到指定的路径。

import os
path = 'C:\\'
print('当前的工作目录: %s' % os.getcwd())  # 当前的工作目录:F:\C盘迁移\AI\AI_demo\python_demo\Python学习随便打的代码
os.chdir(path)
print('目录修改成功: %s' % os.getcwd()) # 目录修改成功:C:\

# 3.listdir (path='.') 返回path 指定的文件夹包含的文件或文件夹的名字的列表。
dirs = os.listdir()
for item in dirs:
    print(item)

"""
结果为：
$AV_AVG
$Recycle.Bin
$WINDOWS.~BT
$Windows.~WS
$WinREAgent
6EE00B91B1F2
AMD
AMTAG.BIN
aow_drv.log
AppData
applog
Documents and Settings
DumpStack.log
DumpStack.log.tmp
ESD
hiberfil.sys
HP_LaserJet_200_color_M251
Intel
logs
MSOCache
OneDriveTemp
PerfLogs
Program Files
Program Files (x86)
ProgramData
Python27
Recovery
sparkraw.log
swapfile.sys
SYSTAG.BIN
System Volume Information
System.sav
Users
Windows
"""

# 4. os.mkdir(path) 创建单层目录，如果该目录已存在抛出异常。
# isdir() 函数被用来检查指定路径是否存在，该方法遵循符号链接，这意味着如果指定的路径是指向一个目录的符号链接，那么该方法将返回True。

if os.path.isdir(r'.\b') is False: # 路径不存在时
    os.mkdir(r'.\B')
    os.mkdir(r'.\B\A')

# os.mkdir(r'.\c\A') # FileNotFoundError: [WinError 3] 系统找不到指定的路径。: '.\\c\\A'

# 5. os.makedirs(path) 用于递归创建多层目录，如果该目录已存在抛出异常。
import shutil
shutil.rmtree(r'.\E\A')
os.makedirs(r'.\E\A')

# 6.os.remove(path) 用于删除指定路径的文件。如果指定的路径是一个目录，将抛出 OSError 。
## 首先创建.\E\A\text.txt 文件，然后进行删除。
os.mkdir(r'.\E\A\test.txt')
print('目录为: %s' % os.listdir(r'.\E\A'))
os.remove(r'.\E\A\test.txt')
print('目录为: %s' % os.listdir(r'\E\A'))

# 7. os.rmdir(path) 用于删除单层目录。仅当这文件夹是空的才可以, 否则, 抛出 OSError.
## 首先创建.\E\A 目录，然后进行删除。
print("目录为: %s" % os.listdir(r'.\E'))
os.rmdir(r'.\E\A')
print("目录为: %s" % os.listdir(r'.\E'))

# 8.os.removedirs(path) 递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常。
## 首先创建.\E\A 目录，然后进行删除
print("目录为: %s" % os.listdir(os.getcwd()))
os.removedirs(r'.\E\A') # 先删除A 然后删除E
print("目录为: %s" % os.listdir(os.getcwd()))

# 9.os.rename(src, dst) 方法用于命名文件或目录，从 src 到 dst ，如果 dst 是一个存在的目录, 将抛出OSError.
## 把test.txt文件重命名为test2.txt。
print("目录为: %s" % os.listdir(os.getcwd()))
os.rename("test.txt", "test2.txt")
print("重命名成功。")
print("目录为: %s" % os.listdir(os.getcwd()))

# 10.os.system(command) 运行系统的shell命令（将字符串转化成命令）
# ## 先自行创建一个a.py的文件，然后由shell命令打开。
#
# path = os.getcwd() + '\\a.py'
# a = os.system(r'python %s' % path)  # 用shell打开a.py文件
os.system('calc') # 打开计算器

"""
1. os.curdir 指代当前目录（ . ）
2. os.pardir 指代上一级目录（ .. ）
3. os.sep 输出操作系统特定的路径分隔符（win下为\\ ，Linux下为/ ）
4. os.linesep 当前平台使用的行终止符（win下为\r\n ，Linux下为\n ）
5. os.name 指代当前使用的操作系统（包括：'mac'，'nt'）
"""

print(os.curdir) # .
print(os.pardir) # ..
print(os.sep) # \
print(os.linesep)
print(os.name) # nt

"""
1. os.path.basename(path) 去掉目录路径，单独返回文件名
2. os.path.dirname(path) 去掉文件名，单独返回目录路径
3. os.path.join(path1[, path2[, ...]]) 将 path1 ， path2 各部分组合成一个路径名
4. os.path.split(path) 分割文件名与路径，返回(f_path,f_name) 元组。如果完全使用目录，它会将最后一个目
录作为文件名分离，且不会判断文件或者目录是否存在。
5. os.path.splitext(path) 分离文件名与扩展名，返回(f_path,f_name) 元组。
"""

# 返回文件名
print(os.path.basename(r'C:\test\lsgo.txt')) # lsgo.txt
# 返回目录路径
print(os.path.dirname(r'C:\test\lsgo.txt')) # C:\test
# 将目录和文件名合成一个路径
print(os.path.join('C:\\', 'test', 'lsgo.txt')) # C:\test\lsgo.txt
# 分割文件名与路径
print(os.path.split(r'C:\test\lsgo.txt')) # ('C:\\test', 'lsgo.txt')
# 分离文件名与扩展名
print(os.path.splitext(r'C:\test\lsgo.txt')) # ('C:\\test\\lsgo', '.txt')

"""
1. os.path.getsize(file) 返回指定文件大小，单位是字节。
2. os.path.getatime(file) 返回指定文件最近的访问时间
3. os.path.getctime(file) 返回指定文件的创建时间
4. os.path.getmtime(file) 返回指定文件的最新的修改时间
5. 浮点型秒数，可用time模块的gmtime() 或localtime() 函数换算
"""

import os
import time
file = r'.\lsgo.txt'
print(os.path.getsize(file)) # 30
print(os.path.getatime(file)) # 1565593737.347196
print(os.path.getctime(file)) # 1565593737.347196
print(os.path.getmtime(file)) # 1565593797.9298275
print(time.gmtime(os.path.getctime(file)))
# time.struct_time(tm_year=2019, tm_mon=8, tm_mday=12, tm_hour=7, tm_min=8, tm_sec=57, tm_wday=0,tm_yday=224, tm_isdst=0)
print(time.localtime(os.path.getctime(file)))
# time.struct_time(tm_year=2019, tm_mon=8, tm_mday=12, tm_hour=15, tm_min=8, tm_sec=57, tm_wday=0,tm_yday=224, tm_isdst=0)

"""
1. os.path.exists(path) 判断指定路径（目录或文件）是否存在
2. os.path.isabs(path) 判断指定路径是否为绝对路径
3. os.path.isdir(path) 判断指定路径是否存在且是一个目录
4. os.path.isfile(path) 判断指定路径是否存在且是一个文件
5. os.path.islink(path) 判断指定路径是否存在且是一个符号链接
6. os.path.ismount(path) 判断指定路径是否存在且是一个悬挂点
7. os.path.samefile(path1,path2) 判断path1和path2两个路径是否指向同一个文件
"""
print(os.path.ismount('D:\\'))  # True
print(os.path.ismount('D:\\Test')) # False
