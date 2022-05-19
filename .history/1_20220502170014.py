import requests
import yagmail
from datetime import datetime
def send163(contents):
    yag = yagmail.SMTP(
                user='pitch_it_own1@163.com',
                host='smtp.163.com')

    yag.send(to='pitch_it_own@163.com',
            subject='sad',
            contents=contents)