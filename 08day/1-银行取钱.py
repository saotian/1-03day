account = "123456"
pwd = "123456"
money = 999999

i_acc = input("请输入账号")
i_pwd = input("请输入密码")

if i_acc == account and i_pwd == pwd:
	i_money = float(input("请输入取款金额"))

	if money >= i_money:
		print("取了%.02f元,剩余%.02f"%(i_money,money-i_money))
	elif money < i_money:
		print("账户余额不足")
else:
	print("账户登录失败")



