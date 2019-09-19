#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# 21.py
# author: 

# 1.导入标准库
import random
# 2.第三方的库
# 3.自定义的库
"""
案例：21点
两个玩家，游戏开始先输入名字
用字典保存每个玩家信息：姓名，获胜次数
电脑随机产生2个数，每个玩家轮流猜1个数，与电脑随机两个数求和，最接近21的获胜
每轮结束显示玩家信息
"""
add=True
cis = []
user1 = input('第一个玩家请输入你的姓名：')
user2 = input('第二个玩家请输入你的姓名：')
print(f'玩家为：{user1},{user2}')
    
user_dict={
    user1:{'win':0},
    user2:{'win':0}
        }

while(add):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    
# print(f'电脑随机输出的两个数为：{num1},{num2}')
    user1_guess = input(f'{user1}猜的整数为：')
    user2_guess = input(f'{user2}猜的整数为：')
    user1_sum = int(user1_guess) + num1 + num2
    user2_sum = int(user2_guess) + num1 + num2
    print(f'{user1}输入的数与电脑随机数的和为{user1_sum}，{user2}输入的数与电脑随机数的和为{user2_sum}')

    if abs(user1_sum-21) > abs(user2_sum-21):
        print(f'{user2}赢了！')
        user_dict[user2]['win']+=1
    else:
        print(f'{user1}赢了！')
        user_dict[user1]['win']+=1
    cis.append(user_dict)
    num =0
    for m in cis:
            num += 1
           # print(f'{num},{m}')
    print(user_dict)
    print(f'电脑随机输出的两个数为：{num1},{num2}')
    print(f'（按y继续添加，按q退出）')
    add = input().strip() == 'y'