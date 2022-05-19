from msilib.schema import Class
import yaml
from aiohttp import Payload
import requests
import yagmail
from datetime import datetime
from datetime import date



def send163(contents):
    yag = yagmail.SMTP(
        user='pitch_it_own1@163.com',
        host='smtp.163.com')

    yag.send(to='pitch_it_own@163.com',
             subject=date.today().strftime("%d/%m/%Y"),
             contents=contents)
def changeTime(newTime,mid):
    with open("./1.yaml", "r", encoding="utf-8") as f:
        yamlFile = yaml.safe_load(f)
    yamlFile["bili"][mid]=str(newTime)
    with open('./1.yaml', 'w',encoding='utf-8') as file:
        yaml.dump(yamlFile, file,encoding="utf-8",allow_unicode=True)

def getbiliItem():
    with open("./1.yaml", "r", encoding="utf-8") as f:
        yamlFile = yaml.safe_load(f)
    biliItems = yamlFile["bili"]
    return biliItems


def getvideos(mid):
    payload = {"mid": mid, "ps": "30", "tid": "0", "pn": "1"}
    r = requests.get(
        "https://api.bilibili.com/x/space/arc/search", params=payload)
    vlist = r.json()["data"]["list"]["vlist"]
    vitem = []
    for i in vlist:
        pic = i["pic"]
        title = i["title"]
        desc = i["description"]
        author = i["author"]
        created = i["created"]
        bvid = i["bvid"]
        vitem.append({"pic": pic, "title": title, "desc": desc,
                      "author": author, "created": created, "bvid": bvid})
    return vitem


def getnewVideos(mid, ttamp):
    vitems = getvideos(mid)
    newvitems = [v for v in vitems if int(v["created"]) > int(ttamp)]
    # changeTime(newvitems[0]["created"],mid)
    return newvitems


def combine(vitems):
    cons = ""
    
    for i in vitems:
        videohref="https://www.bilibili.com/video/"+i["bvid"]
        cons = cons+"<h1>{}</h1><p>up主:{}</p><a href={}>链接</a><p>描述:{}</p><img src={} style='width:20%'/><hr>".format(i["title"],i["author"],videohref,i["desc"],i["pic"])
    return cons


items = getbiliItem()
cons = ""
for i in items:
    newvitems = getnewVideos(i, items[i])
    cons = cons+combine(newvitems)
send163(cons)
