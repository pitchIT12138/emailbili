import requests
import yagmail
from datetime import datetime
yag = yagmail.SMTP(
            user='pitch_it_own1@163.com',
            host='smtp.163.com')

yag.send(to='pitch_it_own@163.com',
         subject='sad',
         contents="email_content")
r = requests.get("https://api.bilibili.com/x/space/arc/search?mid=2019740&ps=30&tid=0&pn=1")
timevideo= datetime.fromtimestamp(r.json()["data"]["list"]["vlist"][0]["created"])
print(timevideo)