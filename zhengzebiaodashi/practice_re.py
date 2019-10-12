import re

#定义表达式对象
re_practice = re.compile(r'\d{3}-\d{8}|\d{4}-\d{7}')#电话号码必备区号
re_popo = re.compile(r'1\d{10}')#手机号码   
# re_popo = re.compile(r'^1\d{10}$')# 只能规定一个手机号的格式

# re_card =re.compile(r'(\d{15}|\d{17}(\d|X))') #这个表示查找15位数的card   身份证号正则表达式：^(\d{15}|\d{17}(\d|X))$
re_card =re.compile(r'(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)')#身份证号码


re_user = re.compile(r'^[\u4e00-\u9fa5]{1,10}$') #验证输入汉字

re_pwd=re.compile(r'^[a-zA-Z]\w{7,17}$')#验证密码


def find_phone(text: str) ->list:
    "查找所有电话号码必备区号，返回列表"
    return re_practice.findall(text)
   
def find_phone2(text2: str) ->list:
    "查找所有手机号码，返回列表"
    return re_popo.findall(text2)

def find_card(card:str) ->list:
    return re_card.findall(card)

def verify_user(username):
    if re_user.match(username):
        return True
    else:
        return False

def verify_pwd(re_obj,username):
    if re_obj.match(username):
        return True
    else:
        return False

def main():
    text = '随便写几个电话号码111-12325670再来一个1234-1232456hh1223-372846264374'
    print(find_phone(text))
    text2 = '14304261998 67836782467856234 3782564836 18573324493'
    # text2 = '14304261998'
    print(find_phone2(text2))
    card = '430426199807054903dcs 678367824678562342'
    print(find_card(card))

    name = 'de8ug'
    name = '哈哈哈哈'
    print('name是否正确？',verify_pwd(re_user, name))

    password='asdfghjgfdhzjad'
    print('pwd是否正确？',verify_pwd(re_pwd, password))
    # print(verify_user(name))
if __name__ == "__main__":
    main()