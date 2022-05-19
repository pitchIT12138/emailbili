from msilib.schema import Class
from aiohttp import Payload
import yaml
import requests
from datetime import datetime
    
def getbiliItem():
    with open("./1.yaml","r",encoding="utf-8") as f:
        yamlFile = yaml.safe_load(f)
    biliItems = yamlFile["bili"]
    return biliItems
def getvideos(mid):
    payload = {"mid":mid,"ps":"30","tid":"0","pn":"1"}
    r = requests.get("https://api.bilibili.com/x/space/arc/search",params=payload)
    vlist = r.json()["data"]["list"]["vlist"]
    vitem = []
    for i in vlist:
        pic = i["pic"]
        title = i["title"]
        desc = i["description"]
        author = i["author"]
        created = i["created"]
        bvid = i["bvid"]
        vitem.append({"pic":pic,"title":title,"desc":desc,"author":author,"created":created,"bvid":bvid})
    return vitem


def getnewVideos(mid,ttamp):
    vitems = getvideos(mid)
    newvitems = [v for v in vitems if int(v["created"])>int(ttamp)]
    return newvitems
def combine(vitems):
    cons=""
    for i in vitems:
        cons=cons+"<h1>{}</h1><p>其他</p>".format(i["title"])
items=getbiliItem()
cons=""
for i in items:
    newvitems=getnewVideos(i,items[i])
    cons=cons+combine(newvitems)
