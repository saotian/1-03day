#1---石头
#2---剪刀
#3---布


import random
i = 0
j = int(input("请输入次数"))
while i <= j:

    player = int(input("请输入1=石头2=剪刀3=布"))
    computer = random.randint(1,3) 
    if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player ==3 and computer == 1):
        print("你弱爆了")
    elif player == computer:
        print("可以啊，能和我打成平手")
    else:
        print("哼,算你牛逼")



