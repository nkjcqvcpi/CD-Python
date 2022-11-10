# -*- coding: utf-8 -*-
import curses
import random
import sys
import time

if __name__ == "__main__":
    i = '无电话号码'
    flag = True
    try:
        with open(sys.argv[1], mode='r') as f:
            phone = f.readlines()
    except FileNotFoundError:
        print('文件不存在')
        exit(0)
    scr = curses.initscr()
    scr.nodelay(True)
    while flag:
        for i in phone:
            scr.addstr(0, 0, '滚动开始（输入回车，滚动停止）：')
            scr.addstr(1, 0, i)
            time.sleep(0.1)
            scr.refresh()
            if scr.getch() == 10:
                flag = False
                break
        random.shuffle(phone)

    print('中奖的号码为：' + i)
