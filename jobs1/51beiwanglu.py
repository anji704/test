'''
完善51备忘录程序
1，使用字典和列表嵌套结构表示多条记录
2，添加信息是，直接输入一句话，进行解析拆解，记录时间和事件
3，不同信息采用不同颜色输出
'''
from color_me import ColorMe
# s=ColorMe('哈哈哈哈哈').blue()
# print(s)
__author__ = '主人'
desc = '51备忘录'.center(40, '-')
print(desc)
welcome = 'welcome'
print(f'{welcome}', __author__)
print('主人请输入你的备忘录信息：')

# 添加dict保存一个字典
"""
{
    'time':30
    'thing':'python',
    
}
"""

all_memo = []  
is_add = True
all_time = 0  

while(is_add):  # 这是个循环输入
    s = input('想在什么时间做什么事：')
    one = {}
    if s.find('点')==True:
        one['时间']=s[s.find('点')-1:s.find('点')+1]
       
        one['事件']=s[s.find('点')+1:]
      
    else:
        one['时间']=s[s.find('点')-2:s.find('点')+1]
      
        one['事件']=s[s.find('点')+1:]
    
    print('待办列表记录'.center(40, '-'))
    # for self in range(1,5):
    #     aa=s
    #     aa=ColorMe(s).color_str
    #     print(aa)
    #     break
 

    aa=ColorMe(s).red()
    print(aa)

    all_memo.append(one)
    num = 0
    for m in all_memo:
        num += 1
        print(f'{num},{m}')
        
    print(f'共{len(all_memo)}条待办事项')
    print('（y：继续添加，n: 退出）')
    is_add = input().strip() == 'y'