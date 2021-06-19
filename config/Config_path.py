# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/17 9:55
@Auth ： Dali
@QQ ：1334029448
@WeChat ：A13420113351T
"""
'''存放项目的路径'''
import os

#项目路径
project_path=r'D:\class_project\pythonProject\class_23\class_23_ui_frame'

#获取报告路径
report_path=os.path.join(project_path,'report')
# print(report_path)
#获取data
data_path=os.path.join(project_path,'data')

#用例的路径
testcase_path=os.path.join(project_path,'testcase')

#公共类的路径
pages_path=os.path.join(project_path,'public','pages')
utils_path=os.path.join(project_path,'public','utils')

#日志路径
logger_path=os.path.join(project_path,'test_logging')

