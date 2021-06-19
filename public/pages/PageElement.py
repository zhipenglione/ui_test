# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/17 11:39
@Auth ： Dali
@QQ ：1334029448
@WeChat ：A13420113351T
"""
'''
存放元素定位
PO 设计模式
1、元素，定位方法，用例，进行分离
2、代码维护起来方便，容易，扩展性很强
3、代码的耦合度减低
单例模式

'''
class Page_element():
    '''定位元素'''

    #登录
    username=('id','ls_username')
    password=('id','ls_password')
    click_login=('xpath','//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button')

    #设置
    setting_value=('link','设置')
    #修改头像断言
    header_value=('xpath','//*[@id="ct"]/div[2]/div/ul/li[1]/a')

    #论坛主页
    luntang=('id','mn_forum')
