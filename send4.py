import smtplib
from email.mime.text import MIMEText

# 创建一个SMTP对象
smtpObj = smtplib.SMTP('smtp.gmail.com', 465)

# 向SMTP服务器发送EHLO命令，这是SMTP协议的规定
smtpObj.ehlo()

# 开启TLS模式
smtpObj.starttls()

# 登录到你的邮箱账号
smtpObj.login('chenzy20011021@gmail.com', 'czy20011021')

# 创建一个邮件对象
msg = MIMEText('Hello, this is a message from my Python script!')
msg['Subject'] = 'Hello'
msg['From'] = 'chenzy20011021@gmail.com'
msg['To'] = '2815259424@qq.com'

# 发送邮件
smtpObj.send_message(msg)

# 关闭SMTP连接
smtpObj.quit()
