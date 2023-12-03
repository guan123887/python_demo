import random
a=int(random.random()*100);
print('猜测一个0到100之间的整数.')
i=1
def R():  
    while i:
        print('-'*40);
        s='第%i次猜,请输入一个整形数字:'%i
        b=input(s)
        b=int(b)
        if(b>a):
            print("太大")
        elif(b<a):
            print('太小')
        else:
            print("恭喜你，猜对了")
            break;


while True:
    R();
    print('\n');
    rep=input('是否继续游戏,输入y/n:');
    if rep=='y':
        R();
    else:
        break;
    
