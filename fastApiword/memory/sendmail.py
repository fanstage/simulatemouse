import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def sendmail():
    msg = MIMEText('收到新的单词书', 'plain', 'utf-8')
    msg['From'] = formataddr(["单词书", '2243366238@qq.com'])
    msg['Subject'] = "单词书"

    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.login("2243366238@qq.com", "zmhpjkxgklebeadj")
    server.sendmail("2243366238@qq.com", "czh18460092659@163.com", msg.as_string())
    server.quit()

