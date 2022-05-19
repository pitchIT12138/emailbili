from msilib.schema import Class
import yaml
import requests
from datetime import datetime
    
def getbiliItem():
    with open("./1.yaml","r",encoding="utf-8") as f:
        yamlFile = yaml.safe_load(f)
    biliItems = yamlFile["bili"]
    return biliItems
def getvideos():
    r = requests.get("https://api.bilibili.com/x/space/arc/search?mid=2019740&ps=30&tid=0&pn=1")
    timevideo= datetime.fromtimestamp(r.json()["data"]["list"]["vlist"][0]["created"])
def getnewVideos(mid):
