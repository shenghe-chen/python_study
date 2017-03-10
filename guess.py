#coding=utf-8
#猜数游戏
import random
print('游戏开始\n')

def guess():
	num = random.randrange(-100,100)
	while 1:
		input = raw_input('输入您猜的数值: ')
		if input == "":
			continue
		try:
			get = int(input)
		except ValueError,e:
			print('\n________请输入数字________\n')
			continue
		if get < num:
			print('猜小了')
		elif get > num:
			print('猜大了')
		else:
			print('\n恭喜你，猜对了~')
			break

if __name__ == "__main__":
	while True:
		guess()
		res = raw_input('\n是否继续游戏?[yes/no]: ')
		if res.upper() == "YES":
			continue
		elif res.upper() == "NO":
			break
		else:
			break
