# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/17 17:52
@Auth ： Dali
@QQ ：1334029448
@WeChat ：A13420113351T
"""
from public.pages.PageElement import Page_element as pe
from public.pages.BasePages import Base_pages

class Test_setting(Base_pages):
    @classmethod
    def setUpClass(cls):
        Base_pages.get_time(2)

    @classmethod
    def tearDownClass(cls):
        Base_pages.get_time(10)
        Base_pages.get_quit()


    def test_002_setting(self):

        setting_value=Base_pages.find_element(pe.setting_value)
        Base_pages.get_click(setting_value)

        #断言
        element=Base_pages.find_element(pe.header_value)
        # text_value=Base_pages.get_text(element)
        # self.assertEqual(text_value,'头像')

        self.assertEqual(element.text,'修改头像')
        self.assertEqual(Base_pages.get_title(),'论坛 - Powered by Discuz!')
