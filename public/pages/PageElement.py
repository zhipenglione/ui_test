# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/17 11:39
@Auth ： Dali
@QQ ：1334029448
@WeChat ：A13420113351T
"""
'''
存放元素定位

'''
class Page_element():
    '''定位元素'''

    #登录
    username=('id','ls_username')
    password=('id','ls_password')
    click_login=('xpath','//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button')

    #设置
    setting_value=('link','设置')


    #论坛主页
    luntang=('id','mn_forum')
