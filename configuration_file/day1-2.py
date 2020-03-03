#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2020.01.02
@author : Bert
'''
import os

print("...................................")
print(__doc__)

print("...................................")

print(__file__)
print("...................................")
print(os.path.basename(__file__))
print("...................................")
print(os.path.dirname(__file__))
print("...................................")
print(os.path.abspath(__file__))
print("...................................")
print(os.name)
print("..................................")
print(
    '''
    ==================================
    姓名: dongGe    
    QQ:xxxxxxx
    手机号:131xxxxxx
    公司地址:北京市xxxx
    ==================================
    '''
)

password = input("请输入密码:")
print("我的密码是:%s" % password)

age1 = input("请输入我的年龄：")
print("我的年龄为：", age1)
age2 = int(age1)
if age2 < 18:
    print("我未成年")
elif age2 == 18:
    print("我正好18岁")
else:
    print("我大于18岁")

'''
1、变量名字由字母、数字和下划线组成，
2、变量只能包含字母、数字和下划线且不能以数字开头。
3、 小驼峰：第一个单词首字母为小写，后面的单词首字母都是大写；大驼峰：每个单词首字母都是大写。
'''
# 4. 提示用户进行输入数据
a = int(input("请输入数字a:"))
b = int(input("请输入数字b:"))
# 获取用户的数据数据（需要获取2个）
print("用户数据a:%s\n用户数据b:%s" % (a, b))
c = a + b
print("a+b=%d" % c)
# 5. 编写程序，完成以下要求：
d = a - b
print("a-b=%d" % d)

# 6.编写程序，完成以下信息的显示:
print('=' * 20)
print("=    欢迎进入到身份认证系统V1.0")
print('= 1. 登录')
print('= 2. 退出')
print('= 3. 认证')
print('= 4. 修改密码')
print('=' * 20)

# 7. 编写程序，从键盘获取一个人的信息，然后按照下面格式显示
print('=' * 20)
print("姓名：%s" % 'dongGe')
print("QQ：%s" % '715772491')
print("手机号：%s" % '13311527869')
print("公司地址：%s" % '北京市xxx')
print('=' * 20)

# 8. 编写程序，从键盘获取用户名和密码，然后判断，如果正确就输出以下信息
userName = "baiJinTao"
password = "123456"
a = str(input("用户名："))
b = str(input("密码："))
if a == userName:
    if b == password:
        print("    亲爱的xxx，欢迎登陆 爱学习管理系统")
    else:
        print("你的密码错误")
else:
    print("你的用户名错误")

GongJiaoKaYuE = int(input("公交卡余额："))
ZuoWeiCount = int(input("剩余座位数量："))

if GongJiaoKaYuE > 2:
    print("可上车")
    if ZuoWeiCount > 0:
        print("可坐下")
    else:
        print("站着吧")
else:
    print("余额不足，请充值后上车")
