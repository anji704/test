#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# 51memo.py
# A memo demo 51备忘录, 使用函数+正则进行优化
# author: xiaoning

"""
场景1：根据已有数据：统计本月共多少人面试，整理手机号列表
data = '''
○ 4.1日，共有4人面试，手机号分别是13812345678，15112345678，13812345678，15112345678
○ 4.5日，共有6人面试 13812345678，15112345678，13812345678，15112345678，13812345678，15112345678
○ 4.7日，共有3人面试13812345678，15112345678，13812345678
○ 4.8日，共有5人面试 15112345678，13812345678，15112345678，13812345678，15112345678
○ 4.30日，共有6人面试13812345678，15112345678，13812345678，15112345678，13812345678，15112345678
'''

# 思考：
# 1 如果只统计某个网段的手机号呢，比如138..
# 2 或者只统计真实存在的网段手机号呢，比如138，151，180类似这种真实有人用的网段[123xx|146xx]

- 场景2：有如下的多条备忘记录，请完成后续功能开发
memo_text = '''
1.1 去找小8写个程序
1.2 记一下王总的电话 139-1234-5678
1.3 修改Python程序的bug
1.4 路上买二斤西红柿，遇见卖鸡蛋的就买一斤
1.5 事情太多，忘了今天要干啥
'''
修改里面的日期格式为几月几日，比如1.1  改为 1月1日

- 场景3：
添加登陆验证功能，只限于个人使用
"""


import re
data = '''
○ 4.1日，共有4人面试，手机号分别是13812345678，15112345678，13912345678，17112345678
○ 4.5日，共有6人面试 13712345678，15712345678，13812345678，15112345678，18612345678，18912345678
○ 4.7日，共有3人面试13812345678，15112345678，13712345678
○ 4.8日，共有5人面试 18912345678，15812345678，15112345678，13812345678，18512345678
○ 4.30日，共有6人面试15112345678，13112345678，13112345678，15112345678，15812345678，15112345678
'''

memo_text = '''
1.1 去找小8写个程序
1.2 记一下王总的电话 139-1234-5678
1.3 修改Python程序的bug
1.4 路上买二斤西红柿，遇见卖鸡蛋的就买一斤
1.5 事情太多，忘了今天要干啥
11.25 看书看书看书
'''

re_user = re.compile(r'^[\u4e00-\u9fa5]|[a-zA-Z0-9]{1,10}$') #验证输入用户名 (中文-所有字母-数字) 1-10之间

re_pwd=re.compile(r'^\w{6,17}$')#验证密码 （中文-所有字母-数字） 6-17之间

re_people=re.compile(r'有(\d+)人')

# re_phone = re.compile(r'1\d{10}') #统计所有电话号码

re_phone = re.compile(r'138\d{8}') # 只统计138开头的电话号码

# re_phone = re.compile(r'138\d{8}|151\d{8}|137\d{8}|156\d{8}|189\d{8}|186\d{8}|157\d{8}|131\d{8}') #只统计真实存在的网段手机号比如138，151，180开头的号码

re_data= re.compile(r'(\d+)\.(\d+)')#把1.1换成1月1日，替换的话，就使用括号分组 \.转义成.符号，而不是正则表达式.

def ren_data(memo_text):
    re_data.findall(memo_text)
    rename = re_data.sub(r'\1月\2日',memo_text)
    #替换成月日，1，2表示正则表达式的位置，\1指(|d+),\2指(\d+)
    print(rename)

def stat_phone(data):#查找所有电话号码
    print(re_phone.findall(data))

def sum_peopel(data):#所有面试的人数
    count = 0
    for x in re_people.findall(data):
        count+=int(x)
    print(f'来面试的人数一共有{count}个人')

def verify_pwd(re_obj,username):
    #判断用户名和密码是否正确
    if re_obj.match(username):
        return True
    else:
        return False

def login():#输入用户名和密码
    login = '登陆界面'.center(40,'-')
    print(login)

    username=input(f'请输入你的用户名：')
    print('用户名是否输入正确？',verify_pwd(re_user, username))

    password=input(f'请输入你的密码：')
    print('密码是否输入正确？',verify_pwd(re_pwd, password))

def main():
    login()
    sum_peopel(data)
    stat_phone(data)
    ren_data(memo_text)
if __name__ == "__main__":
    main()