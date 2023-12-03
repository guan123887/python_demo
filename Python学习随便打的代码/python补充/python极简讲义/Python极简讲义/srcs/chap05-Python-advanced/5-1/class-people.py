class Person:
    height = 140    #定义类的数据成员
    #定义构造方法
    def __init__(self,name,age,weight):
        self.name = name    #定义对象的数据成员属性
        self.age = age
        #定义私有属性,私有属性在类外部无法直接进行访问
        self.__weight = weight
    def speak(self):
        print("%s 说: 我 %d 岁，我体重为 %d Kg，身高为 %d cm" %(self.name,self.age,self.__weight, Person.height))
 
# 实例化类
p1 = Person ('Alice',10,30)     # 实例化people类
p1.speak()                #引用对象中的公有方法
p1.age = 11
p1.name = 'Bob'
p1.speak()

#追加代码
p2 =  Person ('Luna',11,31)        	#创建另外一个对象p2
Person.height = 150              	#为属于类的数据成员height重新赋值
p1.speak()                      		#输出p1对象的信息
p2.speak()                      		#输出p2对象的信息

