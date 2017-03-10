#!/usr/bin/python
# coding=utf-8
import random
print('\n游戏开始')


def guess():
    num = random.randrange(-100, 100)
    while 1:
        input = raw_input('\n输入您猜的数值: ')
        if input == "":
            continue
        try:
            get = int(input)
        except ValueError:
            print('\n请输入数字\n')
            continue
        if get < num:
            print('猜小了')
        elif get > num:
            print('猜大了')
        else:
            print('\n恭喜你，猜对了~')
            break


if __name__ == "__main__":
    try:
        guess()
        while True:
            res = raw_input('\n是否继续游戏?[yes/no]: ')
            if res.upper() == "YES":
                guess()
            elif res.upper() == "NO":
                break
            else:
                continue
        print('\n游戏结束\n')
    except KeyboardInterrupt:
        print('\n游戏结束')
