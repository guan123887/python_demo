""""
模块
在前面我们脚本是用 Python 解释器来编程，如果你从 Python 解释器退出再进入，那么你定义的所有的方法和变量就都消
失了。
为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模
块（Module）。
模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py 。模块可以被别的程序引入，以使用该模块中的函数等
功能。这也是使用 Python 标准库的方法。
"""

"""
1. 什么是模块
    1. 容器 -> 数据的封装
    2. 函数 -> 语句的封装
    3. 类 -> 方法和属性的封装
    4. 模块 -> 程序文件
"""


"""
2. 命名空间
命名空间因为对象的不同，也有所区别，可以分为如下几种：
1. 内置命名空间（Built-in Namespaces）：Python 运行起来，它们就存在了。内置函数的命名空间都属于内置命名空
间，所以，我们可以在任何程序中直接运行它们，比如id() ,不需要做什么操作，拿过来就直接使用了。
2. 全局命名空间（Module：Global Namespaces）：每个模块创建它自己所拥有的全局命名空间，不同模块的全局命名空
间彼此独立，不同模块中相同名称的命名空间，也会因为模块的不同而不相互干扰。
3. 本地命名空间（Function & Class：Local Namespaces）：模块中有函数或者类，每个函数或者类所定义的命名空间就
是本地命名空间。如果函数返回了结果或者抛出异常，则本地命名空间也结束了。
"""

import module.hello

module.hello.hi()  # Hi erveryone, I love lsgogroup!
# hi()  # NameError: name 'hi' is not defined

"""
3. 导入模块
"""

## 1. 第一种：import 模块名
import module.TemperatureConversion
print('32摄氏度 = %.2f华氏度' % module.TemperatureConversion.c2f(32))  # 32摄氏度 = 89.60华氏度
print('99华氏度 = %.2f摄氏度' % module.TemperatureConversion.f2c(99))  # 99华氏度 = 37.22摄氏度


## 2.第二种：from 模块名 import 函数名
from module.TemperatureConversion import c2f, f2c
print('32摄氏度 = %.2f华氏度' % c2f(32))  # 32摄氏度 = 89.60华氏度
print('99华氏度 = %.2f摄氏度' % f2c(99))  # 99华氏度 = 37.22摄氏度

## 3.第三种：import 模块名 as 新名字
import module.TemperatureConversion as tc
print('32摄氏度 = %.2f华氏度' % tc.c2f(32)) # 32摄氏度 = 89.60华氏度
print('99华氏度 = %.2f摄氏度' % tc.f2c(99)) # 99华氏度 = 37.22摄氏度

## 下面方式不推荐
from module.TemperatureConversion import *
print('32摄氏度 = %.2f华氏度' % c2f(32)) # 32摄氏度 = 89.60华氏度
print('99华氏度 = %.2f摄氏度' % f2c(99)) # 99华氏度 = 37.22摄氏度

"""
4. if __name__ == '__main__'
对于很多编程语言来说，程序都必须要有一个入口，而 Python 则不同，它属于脚本语言，不像编译型语言那样先将程序
编译成二进制再运行，而是动态的逐行解释运行。也就是从脚本第一行开始运行，没有统一的入口。
"""

## 示例: 如果不加if __name__ == '__main__'  在导入const.py的.py文件里执行 module/const.py 文件,  会发现文件中的PI被打印了
## 如果加上if __name__ == '__main__'  在运行.py文件， PI则不会被打印

from module.const import PI
def calc_round_area(radius):
    return PI * (radius ** 2)
def main():
    print("round area: ", calc_round_area(2))

## 情况1：const.py不加if __name__ == '__main__' 时
main()  # PI: 3.14  round area:  12.56

## 情况2：const.py加if __name__ == '__main__' 时
main()  # round area:  12.56


## 打印__name__
print(__name__)  # __main__
print(module.const.__name__)  # moducle.const

"""
由此我们可知：如果一个 .py 文件（模块）被直接运行时，其__name__ 值为__main__ ，即模块名为__main__ 。
所以， if __name__ == '__main__' 的意思是：当 .py 文件被直接运行时， if __name__ == '__main__' 之下的代
码块将被运行；当 .py 文件以模块形式被导入时， if __name__ == '__main__' 之下的代码块不被运行。
"""

"""
5.搜索路径  当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。
"""
import sys
print(sys.path)
"""
['F:\\C盘迁移\\AI\\AI_demo\\python_demo\\Python学习随便打的代码', 'F:\\C盘迁移\\AI\\AI_demo\\python_demo', 
'D:\\miniconda\\python37.zip', 'D:\\miniconda\\DLLs', 'D:\\miniconda\\lib', 'D:\\miniconda', 
'C:\\Users\\admin\\AppData\\Roaming\\Python\\Python37\\site-packages', 'D:\\miniconda\\lib\\site-packages', 
'D:\\miniconda\\lib\\site-packages\\setuptools-33.1.1-py3.7.egg', 'D:\\miniconda\\lib\\site-packages\\pip-19.3.1-py3.7.egg', 
'D:\\miniconda\\lib\\site-packages\\win32', 'D:\\miniconda\\lib\\site-packages\\win32\\lib', 
'D:\\miniconda\\lib\\site-packages\\Pythonwin']
"""

"""
我们使用 import 语句的时候，Python 解释器是怎样找到对应的文件的呢？
这就涉及到 Python 的搜索路径，搜索路径是由一系列目录名组成的，Python 解释器就依次从这些目录中去寻找所引入的
模块。
这看起来很像环境变量，事实上，也可以通过定义环境变量的方式来确定搜索路径。
搜索路径是在 Python 编译或安装的时候确定的，安装新的库应该也会修改。搜索路径被存储在 sys 模块中的 path 变
量中。
"""


"""
6.包(package) 
包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
创建包分为三个步骤：
    1. 创建一个文件夹，用于存放相关的模块，文件夹的名字即包的名字。
    2. 在文件夹中创建一个 __init__.py 的模块文件，内容可以为空。
    3. 将相关的模块放入文件夹中。
    
关于一种可能的包结构(在分层的文件系统中)
sound/ 顶层包
    __init__.py         初始化 sound 包
    formats/           文件格式转换子包
        __init__.py
        wavread.py
        wavwrite.py
        aiffread.py
        aiffwrite.py
        auread.py
        auwrite.py
        ...
    effects/          声音效果子包
        __init__.py
        echo.py
        surround.py
        reverse.py
        ...
    filters/          filters 子包
        __init__.py
        equalizer.py
        vocoder.py
        karaoke.py
        ...
    
在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。
目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，最简单的情况，放一个空的 __init__.py 就可以
了。
"""

## 示例  这将会导入子模块 sound.effects.echo 。 他必须使用全名去访问:
# import sound.effects.echo
# sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

## 还有一种导入子模块的方法是： 这同样会导入子模块: echo，并且他不需要那些冗长的前缀，所以他可以这样使用：
# from sound.effects import echo
# echo.echofilter(input, output, delay=0.7, atten=4)

## 还有一种变化就是直接导入一个函数或者变量  同样的，这种方法会导入子模块: echo，并且可以直接使用他的 echofilter() 函数
# from sound.effects.echo import echofilter
# echofilter(input, output, delay=0.7, atten=4)

## 注意当使用 from package import item 这种形式的时候，对应的 item 既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量。

## 如果使用 from sound.effects import *
"""
Python 会进入文件系统，找到这个包里面所有的子模块，一个一个的把它们都导入进来。
导入语句遵循如下规则：如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，那么在使用
from package import * 的时候就把这个列表中的所有名字作为包内容导入。
"""

"""
这里有一个例子，在 sounds/effects/__init__.py 中包含如下代码： __all__ = ["echo", "surround", "reverse"]
这表示当你使用 from sound.effects import * 这种用法时，你只会导入包里面这三个子模块。
如果 __all__ 真的没有定义，那么使用from sound.effects import * 这种语法的时候，就不会导入包
sound.effects 里的任何子模块。他只是把包 sound.effects 和它里面定义的所有内容导入进来（可能运
行__init__.py 里定义的初始化代码）。
这会把 __init__.py 里面定义的所有名字导入进来。并且他不会破坏掉我们在这句话之前导入的所有明确指定的模块。
"""

# import sound.effects.echo
# import sound.effects.surround
# from sound.effects import *

"""
这个例子中，在执行 from...import 前，包 sound.effects 中的 echo 和 surround 模块都被导入到当前的命名空
间中了。
通常我们并不主张使用 * 这种方法来导入模块，因为这种方法经常会导致代码的可读性降低。
"""


