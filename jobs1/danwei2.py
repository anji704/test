'''
1，根据输入内容判断单位类型
2，完成温度互转，华氏温度与摄氏温度 
3，完成长度互转，中国与美国长度单位
4，完成货币互转，美元与人民币（汇率当天为准）
'''

caidian={
    'L':'长度转换',
    'W':'温度转换',
    'M':'货币转换'
}


while True:
    print('欢迎来到万能单位转换器'.center(30,'-'))
    for k,v in caidian.items():
        print(k,v)
    choose = input('请输入你选择的转换类型（按q退出）:')
    if choose == 'W':
        wendu = input('请输入温度（示例：1C或者1F）:')
        if wendu.endswith('C'):#判断输入的字符串最后面一位是否为C
            temp1 = float(wendu.strip('C')) #把输入的温度数后面的C和F去掉，赋值给一个新的数
        # 摄氏温度转华氏温度 Tf=(9/5)(Tc-32) 
        # 华氏温度转换摄氏温度 Tc=(5/9)(Tf-32)
            Tf = (9 / 5) * temp1 + 32
            print(Tf)
            print(f'(9 / 5) * {temp1} + 32={Tf}F')
        elif wendu.endswith('F'):
            temp2 = float(wendu.strip('F'))
            Tc=(5/9)*(temp2-32)
            print(Tc)
            print(f'(5/9)(temp2-32)={Tc}C')
        else:
            print('抱歉,你输入的单位不对！')
    elif choose == 'L':
        length = input('请输入长度（示例：1CM或者1INCH）:')#1inch=2.54cm=25.4mm
        if length.endswith('CM'):
            temp3=float(length.strip('CM'))
            INCH=temp3/2.54
            print(f'公式为：{length}/2.54={INCH}英尺')
           # print(f'{INCH}英寸')
            print('%.2f' % INCH)
        elif length.endswith('INCH'):
            temp4=float(length.strip('INCH'))
            CM=temp4 * 2.54
            print(f'公式为：{length} * 2.54={CM}厘米')
            print(f'{CM}厘米')
        else:
            print('抱歉,你输入的单位不对！')
        #  1人民币=0.1405美元    1美元=7.1154人民币  2019-9-10的汇率
    elif choose == 'M':
        huilv=input('请输入汇率（示例：1美元或者1元）：')
        if huilv.endswith('美元'):
            temp5=float(huilv.strip('美元'))
            money=temp5 * 7.1154
            print(f'公式为：{huilv} * 7.1154 ={money}元')
            print('%.2f' % money)
        elif huilv.endswith('元'):
            temp6=float(huilv.strip('元'))
            china=temp6 * 0.1405
            print(f'公式为：{huilv} * 0.1405={china}美元')
            print('%.2f' % china)
        else:
            print('抱歉,你输入的单位不对！')
    elif choose =='q':
        print('bye!')
        break
    else:
        print('抱歉，没有你想要转换的类型!')
        
