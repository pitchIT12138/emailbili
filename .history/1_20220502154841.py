import requests
import yagmail
from datetime import datetime
yag = yagmail.SMTP(
            user='pitch_it_own1@163.com',
            password='DUVHQNYOBDLEAGAM',
            host='smtp.163.com',  # 邮局的 smtp 地址
            port='端口号',       # 邮局的 smtp 端口
            smtp_ssl=False)

yag.send(to='收件箱账号',
         subject='邮件主题',
         contents='邮件内容')
r = requests.get("https://api.bilibili.com/x/space/arc/search?mid=2019740&ps=30&tid=0&pn=1")
timevideo= datetime.fromtimestamp(r.json()["data"]["list"]["vlist"][0]["created"])
print(timevideo)