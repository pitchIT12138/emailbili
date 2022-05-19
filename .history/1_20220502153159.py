import requests
r = requests.get("https://api.bilibili.com/x/space/arc/search?mid=2019740&ps=30&tid=0&pn=1")
print(r.json()["vlist"])