from globalVar import Var
import smtplib
from email.mime.text import MIMEText
import time
import datetime


def send_email():
    # 获取年月日
    today = datetime.datetime.today()
    today_str = f"{today.year}年{today.month}月{today.day}日"

    # 将程序输出重定向到字符串变量

    # 设置邮件参数
    sender = "2410419557@qq.com"
    receiver = "2859371427@qq.com"
    #receiver = "3239438965@qq.com"
    subject = f"{today_str}|作业完成情况"
    body = Var.sendemail_info

    # 创建邮件对象
    msg = MIMEText(body, "plain", "utf-8")
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    # 发送邮件
    try:
        smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
        smtp.login("2410419557@qq.com", "ottftrkinsgmdjja")
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print("邮件发送成功")
    except Exception as e:
        print("邮件发送失败")
        print(e)

# 设置定时任务
# schedule.every().day.at("10:00").do(send_email)

# while True:
# schedule.run_pending()
