"""
序列化与反序列化
Python 的 pickle 模块实现了基本的数据序列和反序列化。
    1. 通过 pickle 模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
    2. 通过 pickle 模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
pickle模块中最常用的函数为：
pickle.dump(obj, file, [,protocol]) 将obj 对象序列化存入已经打开的file 中。
    1. obj ：想要序列化的obj 对象。
    2. file :文件名称。
    3. protocol ：序列化使用的协议。如果该项省略，则默认为0。如果为负值或HIGHEST_PROTOCOL ，则使用最高的协
    议版本。
"""

# pickle.load(file) 将file 中的对象序列化读出。 1. file ：文件名称。
import pickle
dataList = [[1, 1, 'yes'],
[1, 1, 'yes'],
[1, 0, 'no'],
[0, 1, 'no'],
[0, 1, 'no']]

dataDic = {0: [1, 2, 3, 4],
1: ('a', 'b'),
2: {'c': 'yes', 'd': 'no'}}

## 使用dump()将数据序列化到文件中
fw = open(r'./dataFile.pkl', 'wb')
## # Pickle the list using the highest protocol available.
pickle.dump(dataList, fw, -1)

## Pickle dictionary using protocol 0.
pickle.dump(dataDic, fw)
fw.close()


# 使用load()将数据从文件中序列化读出
fr = open('dataFile.pkl', 'rb')
data1 = pickle.load(fr)
print(data1)  # [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
data2 = pickle.load(fr)
print(data2)  # {0: [1, 2, 3, 4], 1: ('a', 'b'), 2: {'c': 'yes', 'd': 'no'}}
fr.close()