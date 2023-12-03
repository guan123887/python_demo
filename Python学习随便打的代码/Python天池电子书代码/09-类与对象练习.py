#1. 以下类定义中哪些是类属性，哪些是实例属性？
    #不知道,没看见以下内容

#2. 怎么定义私有⽅法？
class A:
    __x=0

#3. 尝试执行以下代码，并解释错误原因：
"""
class C:
 def myFun():
    print('Hello!')
c = C()
c.myFun()
"""
class C:
 # def myFun():   #需要改成myFun(self)
 def myFun(self):
    print('Hello!')
c = C()
c.myFun()

#4. 按照以下要求定义一个游乐园门票的类，并尝试计算2个成人+1个小孩平日票价。
"""
要求:
1. 平日票价100元
2. 周末票价为平日的120%
3. 儿童票半价
class Ticket():
# your code here
"""

class Ticket():
# your code here
    #票价
    price=100
    total = 0
    #平日
    def __init__(self,id,ch,time):
        # 成人人数
        self.id=id
        # 儿童人数
        self.ch=ch
        #时间
        self.time=time
    def SumP(self):
        self.total=self.id*self.price+self.ch*self.price*0.5
    #周末
    def SumW(self):
        self.total*=1.2
    def Panduan(self):
        if self.time=='平日':
            self.SumP();
        elif self.time=='周末':
            self.SumW();
        else:
            print('输入有误,请重新输入');
        return self.total

p=Ticket(2,1,'平日')
print(p.Panduan())  #250.0