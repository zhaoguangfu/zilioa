# -*- coding: utf-8 -*-
# 发送附件
# 负责发送邮件
import smtplib
# 负责构造邮件的正文
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
 
# 发送邮箱的服务器
smtpserver = "smtp.163.com"
# smtpserver = 'smtp.qq.com'
# 发送邮箱用户、授权密码非登录密码
# user = 'xxx@163.com'
user = 'zhaowenjun19@163.com'
password = 'BVNESLINVRKMLBQT'
 
# 发送的邮箱
# sender = 'xxxx@163.com'
sender = 'zhaowenjun19@163.com'
# 接受的邮箱 多个人[]用列表数据
# receiver = '1120165256@qq.com'
receiver = '1120165256@qq.com'
 
# 发送邮件主题
subject = '测试报告'
# 发送人
name='ss'

# 发送的附件
sendfile = open(r'C:\\Users\\zhaow\\PycharmProjects\\untitled1\\测试报告\\test_case2020-08-03 17_02_40test_case.html', 'rb').read()
att = MIMEText(sendfile, 'html', 'utf-8')
att['Content-Type'] = 'text/html'
att['Content-Disposition'] = 'attachment; filename="2020-08-03 17_02_40测试报告.html"'

msgRoot = MIMEMultipart('related')
 
msgRoot['Subject'] = subject
msgRoot['from'] = user
# 发给谁
msgRoot['to'] = receiver
msgRoot.attach(att)

# smtp= smtplib.SMTP(smtpserver)
# smtp.connect(smtpserver)
smtp=smtplib.SMTP_SSL("smtp.163.com")
smtp.login(user, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
print("邮件发送成功")

'''

# 查找最新的测试报告
import os
 
# 定义文件目录
result_dir = 'E:\\workspace\\Python37\\www\\selenium\\unit_test\\report'
# 列出所有的目录和文件
lists = os.listdir(result_dir)
# 重新按照时间排序
lists.sort(key = lambda x: os.path.getmtime(result_dir+'\\'+x))
 
print(('最新的文件为：' + lists[-1]))
file = os.path.join(result_dir, lists[-1])
print(file)
'''