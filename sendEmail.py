from globalVar import Var
from globalVar import config
import smtplib
from email.mime.text import MIMEText
import datetime


def send_email():
    # 获取年月日
    today = datetime.datetime.today()
    today_str = f"{today.year}年{today.month}月{today.day}日"

    # 设置邮件参数
    sender = config['email']['sender']
    receiver = config['email']['receiver']
    subject = f"{today_str}|作业完成情况"
    body = Var.sendemail_info
    host = config['email']['host']
    port = config['email']['port']
    user = config['email']['user']
    password = config['email']['password']

    # 创建邮件对象
    msg = MIMEText(body, "plain", "utf-8")
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    # 发送邮件
    try:
        smtp = smtplib.SMTP_SSL(host, port)
        smtp.login(user, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print("邮件发送成功")
    except Exception as e:
        print("邮件发送失败")
        print(e)
