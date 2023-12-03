# 2. 怎么定义私有⽅法？
# __名字

# 3. 尝试执行以下代码，并解释错误原因：  # 需要加上self

# class C:
#     def myFun():
#         print('Hello!')
# c = C()
# c.myFun()

# 4.
""""
按照以下要求定义一个游乐园门票的类，并尝试计算2个成人+1个小孩平日票价。
要求:
1. 平日票价100元
2. 周末票价为平日的120%
3. 儿童票半价
"""

class Ticket():
# your code here
    def __init__(self, tic_ordinary, num_adult, num_child):
        self.tic_ordinary = tic_ordinary
        self.num_adult = num_adult
        self.num_child =num_child

    def calOrdinary(self):
        return self.num_adult * self.tic_ordinary + self.num_child * self.tic_ordinary / 2

    def calweekend(self):
        return self.calOrdinary() * 1.2

t = Ticket(100, 2, 1)
print(t.calOrdinary())