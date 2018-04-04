acc = "123456"
pwd = "123456"
count = 1
while True:
i_acc = int(input("请输入你的账号"))
i_pwd = int(input("请输入你的密码"))
if acc == i_acc and pwd == i_pwd:
    print("登陆成功")
a = int(input("0 = ADC 1 = 肉 3 = 法师"))
    if a == 0:
        print("鲁班大师")
    elif a == 1:
        pring("肉")
    elif a == 2:
        print("王绍军")
    brea
else:
    print("错误%d次"%count)
    count+=1
    if count == 4:
        print("登陆限制")
        break
