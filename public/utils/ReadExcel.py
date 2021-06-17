# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/17 10:24
@Auth ： Dali
@QQ ：1334029448
@WeChat ：A13420113351T
"""
'''
读物excel表格 pip install xlrd==1.1.0
'''
import os
import xlrd
from config.Config_path import data_path
class Read_excel():
    '''读取excel的工具类'''
    def __init__(self,filename,sheetname):
        Data_adspath=os.path.join(data_path,filename)
        #打开excle 报告
        self.workbook=xlrd.open_workbook(Data_adspath)
        #打开某个页签
        self.sheet_value=self.workbook.sheet_by_name(sheetname)

    def read_value(self,row,col):
        '''读取单元格'''
        value=self.sheet_value.cell_value(row,col)
        return (value)
if __name__ == '__main__':
    readexcel=Read_excel('Data.xlsx','Sheet1')
    print(readexcel.read_value(1,0))