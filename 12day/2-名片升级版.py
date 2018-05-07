print("名片系统v1.0版本".center(30," "))
print("1:新增名片".center(30," "))
print("2:查找名片".center(30," "))
print("3:修改名片".center(30," "))
print("4:删除名片".center(30," "))
print("5:退出系统".center(30," "))
cards = []
while True:
	fun_number = int(input("请输入功能:"))
	if fun_number == 1:
	#	print("新增")
		flag = 0
		card = {}
		name = input("请输入名字:")
		for temp in cards:
			if name == temp["name"]:
				flag = 1
				break
		if flag == 1:
			print("名字重复了,请重新输入:")
			continue
		zhiwei = input("请输入职位:")
		phone = int(input("请输入手机号:"))
		gongsi = input('请输入公司名字:')
		dizhi = input('请输入公司地址:')
		card["name"] = name
		card['zhiwei'] = zhiwei
		card['phone'] = phone
		card['gongsi'] = gongsi
		card['dizhi'] = dizhi
		cards.append(card)
		print('新增成功')




	elif fun_number == 2:
	#	print("查找")
		name = input("请输入要查找的名字")
		flag = 0
		count = 0
		for p in cards:
			count += 1
			if name  == p["name"]:
				flag = 1
				break
		if flag == 0:
				print('查无此人')
		else:
			print("姓名:%s\n职位:%s\n手机号:%s\n公司:%s\n地址:%s"%(cards[count-1]["name"],cards[count-1]["zhiwei"],cards[count-1]["phone"],cards[count-1]["gongsi"],cards[count-1]["dizhi"]))

	elif fun_number == 3:
		name = input("请输入要修改的名字")
		for temp in cards:
			if name == temp["name"]:
				print("1:修改名字".center(30," "))
				print("2:修改职位".center(30," "))
				print("3:修改手机号".center(30," "))
				print("4:修改公司名称".center(30," "))
				print("5:修改公司地址".center(30," "))
				a = int(input("请选择修改序号"))
				if a == 1:
					name = input("请输入新的名字")
					temp['name'] = name
				elif a == 2:
					name = input("请输入新的职位")
					temp['zhiwei'] = zhiwei
				elif a == 3:
					name = int(input("请输入新的手机号"))
					temp['phone'] = phone
				elif a == 4:
					name = input("请输入新的公司名称")
					temp['gongsi'] = gongsi
				elif a == 5:
					name = input("请输入新的公司地址")
					temp['dizhi'] = dizhi
				else:
					print('输入错误\n')

















	elif fun_number == 4:
		nama = input('请输入你要删除的名字')
		flag = 0
		for temp in cards:
			if name  == temp["name"]:
				flag = 1
				shifoshanchu = int(input("1确定删除　2返回"))
				if shifoshanchu == 1:
					cards.remove(temp)
					pmerint('删除成功')
				break
		if flag == 0:
			print('没有此人')
	else:
		break
			


