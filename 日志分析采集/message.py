# -*- coding: utf-8 -*-
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from config import *

class em:
    mail_host = ""  # 设置服务器
    mail_user = ""  # 用户名
    mail_pass = ""  # 口令
    def __init__(self, mail_host,mail_user,mail_pass):
        self.mail_host = mail_host;
        self.mail_user = mail_user;
        self.mail_pass = mail_pass;

    def _format_addr(self,s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def send(self,addr,content='邮件正文',from_user='发件人',to_user='收件人',title='服务器日志通知'):
        if addr=='':
            print("请输入收件地址")
            return ;
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = self._format_addr(from_user+' <%s>' % self.mail_user)
        message['To'] = self._format_addr(to_user+' <%s>' % addr)
        message['Subject'] = Header(title, 'utf-8').encode()
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465);
            s.login(self.mail_user, self.mail_pass)
            s.sendmail(self.mail_user, addr.split(','), message.as_string())
            print("邮件发送成功")
            s.quit()
        except (BaseException, ValueError) as info:
            print(info)
            print("无法发送邮件")



if __name__=='__main__':
    pass;
    # line = '\u0004\u0004ip\u001a192.168.1.227\u0012timestamp\u001a1522380514404\u0000\u000eerror11'
    # b = line.split('\u0000\u000e')
    # a = '\r\n '.join(b)
    # em(mail["mail_host"], mail["mail_user"], mail["mail_pass"]).send('1628359000@qq.com',a);
