# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/17 14:11
@Auth ： Dali
@QQ ：1334029448
@WeChat ：A13420113351T
"""
'''封装元素定位的方法'''
import time
import unittest
from selenium import webdriver
from public.pages.PageElement import Page_element as pe
class Base_pages(unittest.TestCase):
    @classmethod
    def set_driver(cls,driver):#设置浏览器驱动
        cls.driver=driver

    @classmethod
    def get_driver(cls):#获取驱动----单例模式
        return cls.driver


    # '''调试'''
    # driver=webdriver.Chrome()
    # username = ('id', 'ls_username')

    @classmethod
    def find_element(cls,element):
        '''封装元素定位的方法'''
        elem_type=element[0]
        elem_value=element[1]
        try:
            if elem_type in['id','ID','Id']:
                elem=cls.driver.find_element_by_id(elem_value)
            elif elem_type in['name','NAME','Name']:
                elem=cls.driver.find_element_by_name(elem_value)
            elif elem_type in ['class', 'CLASS', 'Class']:
                elem=cls.driver.find_element_by_class_name(elem_value)
            elif elem_type in ['link', 'LINK', 'Link']:
                elem=cls.driver.find_element_by_link_text(elem_value)
            elif elem_type in ['xpath', 'XPATH', 'Xpath']:
                elem=cls.driver.find_element_by_xpath(elem_value)
            elif elem_type in ['css', 'CSS', 'Css']:
                elem=cls.driver.find_element_by_css_selector(elem_value)
            else:
                raise NameError('请输入正确的参数')
        except Exception as e:
            print(e,'这个元素不存在',element)
        return elem


    @classmethod
    def get_send_keys(cls,elemt,text):
        '''封装输入文本内容'''
        elemt.send_keys(text)

    @classmethod
    def get_click(cls,elem):
        '''封装输入内容'''
        elem.click()


    @classmethod
    def get_quit(cls):
        cls.driver.quit()

    @classmethod
    def go_home(cls):
        lunt=Base_pages.find_element(pe.luntang)
        Base_pages.get_click(lunt)

    @classmethod
    def get_title(cls):
        title=cls.driver.title
        return title

    @classmethod
    def get_text(cls,elemt):
        text = elemt.text
        return text

    @classmethod
    def get_time(cls,num):
        time.sleep(num)

# if __name__ == '__main__':
#     # Base_pages.find_element(pe.username)