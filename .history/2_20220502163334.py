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
    pic = vlist["pic"]
    title = vlist["title"]
    desc = vlist["description"]
    author = vlist["author"]
    created = vlist["created"]
    bvid = vlist["bvid"]
    timevideo= datetime.fromtimestamp(r.json()["data"]["list"]["vlist"][0]["created"])
def getnewVideos(mid):
