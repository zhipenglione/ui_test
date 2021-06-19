# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/18 11:09
@Auth ： Dali
@QQ ：1334029448
@WeChat ：A13420113351T
"""
import logging
'''
debug : 打印全部的日志,详细的信息,通常只出现在诊断问题上
info : 打印info,warning,error,critical级别的日志,确认一切按预期运行
warning : 打印warning,error,critical级别的日志,一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来
error : 打印error,critical级别的日志,更严重的问题,软件没能执行一些功能
critical : 打印critical级别,一个严重的错误,这表明程序本身可能无法继续运行
这时候，如果需要显示低于WARNING级别的内容，可以引入NOTSET级别来显示：

'''

# logging.basicConfig(level=logging.DEBUG)
# # logging.debug('调试日志')#级别10
# # logging.info('正常消息日志')#20
# # logging.warning('警告日志')#30
# # logging.error('错误日志')#40
# # logging.critical('严重错误')#50
#
# def func_1():
#
#     print('明天去爬山')
#     logging.error('运行有问题')
#
# func_1()

logger=logging.getLogger()#实例化一个记录器对象，记录日志

#定义一个对象写入日志到某个文件
file_wenj=logging.FileHandler(r'D:\class_project\pythonProject\class_23\class_23_ui_frame\test_logging\test.log',encoding='utf-8')

#定义以一个对象，让日志在屏幕显示
keshihua=logging.StreamHandler()

#格式化输出日志内容
formatter=logging.Formatter('%(asctime)s-%(filename)s-[line:%(lineno)d]-%(levelname)s-%(module)s-%(message)s')

#设置格式
file_wenj.setFormatter(formatter)
keshihua.setFormatter(formatter)

logger.addHandler(file_wenj)#对象写入
logger.addHandler(keshihua)

#给logger对象设置一个总level
logger.setLevel(10)
file_wenj.setLevel('ERROR')
keshihua.setLevel(10)

logging.debug('调试日志')#级别10
logging.info('正常消息日志')#20
logging.warning('警告日志')#30
logging.error('错误日志')#40
logging.critical('严重错误,提示消息')#50