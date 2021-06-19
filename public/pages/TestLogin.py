# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/17 15:07
@Auth ： Dali
@QQ ：1334029448
@WeChat ：A13420113351T
"""
import unittest
from selenium import webdriver
from public.pages.BasePages import Base_pages#二次封装的方法
from public.pages.PageElement import Page_element as pe#元素定位内容
from public.utils.LoginData import Login_Data
from public.utils.logger import trace_log

url=Login_Data().get_url()
user=Login_Data().get_user()
password=Login_Data().get_password()
class Login_test(Base_pages):
    @classmethod
    def setUpClass(cls):
        driver=webdriver.Chrome()
        Base_pages.set_driver(driver)

    @classmethod
    def tearDownClass(cls):
        Base_pages.get_time(2)
        Base_pages.go_home()
    @trace_log
    def test_001_login(self):
        driver=Base_pages.get_driver()
        '''打开浏览器'''
        driver.get(url)
        '''输入用户名'''
        username=Base_pages.find_element(pe.username)
        Base_pages.get_send_keys(username,user)

        '''输入密码'''
        password_elem=Base_pages.find_element(pe.password)
        Base_pages.get_send_keys(password_elem,password)

        '''点击登录'''
        click_login=Base_pages.find_element(pe.click_login)
        Base_pages.get_click(click_login)
        #断言
        self.assertEqual(Base_pages.get_title(),'论坛 - Powered by Discuz!')
if __name__ == '__main__':
    unittest.main()
