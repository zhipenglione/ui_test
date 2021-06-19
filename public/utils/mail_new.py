# -*- coding: utf-8 -*-
# @Author  : Dali
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


class Maile_test():
    def __init__(self,filename,smtpserver ='smtp.sina.com',
                 user ='1334029448li@sina.com',
                 password='123456Li',
                 sender='1334029448li@sina.com',
                 receiver ='1334029448@qq.com',
                 subject = '冬至吃姜饭'):

        self.mail_addr=filename #发送邮件的地址
        self.smtpserver=smtpserver#发送邮件的服务器
        self.user=user # 发送邮箱的用户/密码
        self.password=password
        self.sender=sender # 发送邮件
        self.receiver=receiver # 接受邮件的用户
        self.subject=subject # 发送邮件主题

    #把报告路径拿到，报告名称切出来
    def report_name(self):
        mail_name = str(self.mail_addr)
        repost_name1 = mail_name.split("\\")
        return repost_name1[-1]

    #发送邮件的附件
    def send_meail(self):
        sendfile = open(self.mail_addr, 'rb').read()
        att = MIMEText(sendfile, "plain", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        # att["Content-Disposition"]="attachment;filename =report_name"
        att.add_header('Content-Disposition', 'attachment', filename=self.report_name())
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = Header(self.subject, 'utf-8')
        msgRoot['From'] = Header(self.user)
        msgRoot.attach(att)

        smtp = smtplib.SMTP()
        smtp.connect(self.smtpserver)
        # 用户登录并发送邮件
        smtp.login(self.user, self.password)
        smtp.sendmail(self.sender, self.receiver, msgRoot.as_string())
        smtp.quit()


if __name__ == '__main__':
    mail_addr = r'D:\class_project\pythonProject\class_23\class_23_ui_frame\report\2021_06_17_18_02_29_ui_report.html'
    meile_test = Maile_test(mail_addr)
    meile_test.send_meail()
