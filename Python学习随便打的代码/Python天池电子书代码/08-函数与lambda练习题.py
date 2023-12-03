#1. 怎么给函数编写⽂档？
def MyFirstFunction(name):
    "此处name是形参,表示占据一个参数位置"
    print('传递进来的{0}为实参,因为它是具体的参数值'.format(name))
print(MyFirstFunction.__doc__)  #此处name是形参,表示占据一个参数位置
MyFirstFunction('程序员')  #传递进来的程序员为实参,因为它是具体的参数值
#2. 怎么给函数参数和返回值注解？
def Ha(a:int)->int:
    return a
print(Ha(3))    #3
#3. 闭包中，怎么对数字、字符串、元组等不可变元素更新
def A():
    x=3
    y=[4,5,6]
    z=(7,8,9)
    def B():
        nonlocal x,y
        nonlocal z
        z=list(z)
        x+=10
        print(x)    #13
        y[0]+=20
        print(y)    #
        z[1]+=30
        print(z)    #[7, 38, 9]
    B()
A()

#4. 分别根据每一行的首元素和尾元素大小对二维列表 [[6, 5], [3, 7], [2, 8]] 排序。(利用lambda表达式)
a = [[6, 5], [3, 7], [2, 8]]
sort1=sorted(a,key=lambda x:x[0])
print(sort1)    #[[2, 8], [3, 7], [6, 5]]
sort2=sorted(a,key=lambda x:x[1])
print(sort2)    #[[6, 5], [3, 7], [2, 8]]
"""
5. 利用python解决汉诺塔问题？
有a、b、c三根柱子，在a柱子上从下往上按照大小顺序摞着64片圆盘，把圆盘从下面开始按大小顺序重新摆放在c柱子
上，尝试用函数来模拟解决的过程。（提示：将问题简化为已经成功地将a柱上面的63个盘子移到了b柱）
"""
import sys
sys.setrecursionlimit(100000)   #设置递归次数为100000
def hanota(n,a,b,c):
    "实现汉诺塔"
    #如果只剩最后一个盘子,给c
    if n==1:
        print(' {0} ---> {1}'.format(a,c));
    else:
        #把n-1个盒子先从a给b
        hanota(n-1,a,c,b)
        hanota(1,a,b,c)
        #再把n-1个盒子从b给c
        hanota(n-1,b,a,c)
hanota(3,'a','b','c')
