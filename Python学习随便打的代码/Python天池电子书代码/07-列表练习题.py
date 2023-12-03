import math
x=[2,5,6,7,8,9,2,9,9];
#末尾添加一个元素
x.append(15)
print(x)

#向中间位置添加元素
length=len(x);
middle=math.ceil(length/2)
x.insert(middle,20)
print(x)
#将列表[2, 5, 6]合并到lst中
x.extend([2,5,6])
print(x)

# 移除列表中索引为3的元素
x.pop(3)
print(x)

#翻转列表里的所有元素
x.reverse()
print(x)

#对列表里的元素进行排序，从小到大一次，从大到小一次

x.sort(reverse=False)
print(x)
x.sort(reverse=True)
print(x)

#请将列表里所有数字修改成原来的两倍
y=[1,[4, 6],True]
y[0]=y[0]*2
y[1][0]=y[1][0]*2
y[1][1]=y[1][1]*2
print(y)

#顶峰索引

#获取顶峰之前元素
def GetPre(A):
    pre=A[0]
    for index,value in enumerate(A[1:]):
        if(value>pre):
            pre=value;
        else:
            return index
#获取顶峰之后元素
def GetLater(Later_A):
    pre=Later_A[0];
    length=len(Later_A)
    for value in Later_A[1:]:
        if(value<pre):
            pre=value;
        else:
            return -1;
    
class Solution:
    def __init__(self,A):
        self.A=A;
    def peakIndexMountainArray(self):
        pre_index=GetPre(self.A);
        Pre_A=self.A[:pre_index-1];
        Later_A=self.A[pre_index:]
        later_index=GetLater(Later_A);
        if(later_index==-1 or pre_index<=0):
            print('不符合山脉数组要求')
        else:
            print('顶峰索引为:',pre_index);
        
Solu=Solution([8,7,6,5,4,3,2]);
result=Solu.peakIndexMountainArray()
