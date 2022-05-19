import requests
from datetime import datetime
r = requests.get("https://api.bilibili.com/x/space/arc/search?mid=2019740&ps=30&tid=0&pn=1")
timevideo= datetime.fromtimestamp(r.json()["data"]["list"]["vlist"][0]["created"])
print(r.json()["data"]["list"]["vlist"][0])