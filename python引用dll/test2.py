import clr
clr.FindAssembly('ClassLibrary1')
from ClassLibrary1 import *
ins=Class1()
print(ins.add(3,4))