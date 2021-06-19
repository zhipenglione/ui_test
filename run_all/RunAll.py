# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/17 17:23
@Auth ： Dali
@QQ ：1334029448
@WeChat ：A13420113351T
"""
import os
import time
import unittest
from config.Config_path import report_path,project_path
from HTMLTestRunner import HTMLTestRunner
from public.utils.mail_new import Maile_test
#获取报告
now_time=time.strftime('%Y_%m_%d_%H_%M_%S')+'_ui_report.html'
new_report_path=os.path.join(report_path,now_time)
# print(new_report_path)

def auto_ui():
    # suit=unittest.TestSuite()#存放用例的容器
    # loader=unittest.TestLoader()#加载用例
    # suit.addTest(loader.loadTestsFromName('public.pages.LoginTest.Login_test'))
    # log_run=r'D:\class_project\pythonProject\class_23\class_23_ui_frame'

    dis_value=unittest.defaultTestLoader.discover(project_path,'Test*.py')

    with open(new_report_path,'wb') as file_wb:
        runner=HTMLTestRunner(stream=file_wb,title='自动化用例报告',verbosity=2,description='小小自动化报告')
        runner.run(dis_value)
def send_email():
    email_test=Maile_test(new_report_path)
    email_test.send_meail()
auto_ui()
# send_email()