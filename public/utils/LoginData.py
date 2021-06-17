# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/17 11:15
@Auth ： Dali
@QQ ：1334029448
@WeChat ：A13420113351T
"""
from public.utils.ReadExcel import Read_excel
class Login_Data():
    def __init__(self):
        self.read_excel=Read_excel('Data.xlsx','Sheet1')
    def get_url(self):
        url=self.read_excel.read_value(1,0)
        return url
    def get_user(self):
        user=self.read_excel.read_value(1,1)
        return user
    def get_password(self):
        password=self.read_excel.read_value(1,2)
        return int(password)
if __name__ == '__main__':
    login_data=Login_Data()
    print(login_data.get_url())
    print(login_data.get_user())
    print(login_data.get_password())