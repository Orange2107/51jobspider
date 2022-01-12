# -*- coding = utf-8 -*-
# @Time : 2022/1/12 7:59 PM
# @Author : CZJ
# @File  :   spider.py
# @software : PyCharm

import urllib.request, urllib.error #制定url，获取页面
import re
from bs4 import BeautifulSoup  #网页解析，获取数据

def getData(jobPath):
   for page in range(1, 2):
       jobPath = jobPath + str(page)+".html"
       html = askUrl(jobPath)
       #页面解析
       #Page = BeautifulSoup(html, "html.parser")


def askUrl(jobPath):
    head = {

        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    }  # 告诉豆瓣服务器，我们是什么类型的浏览器
    req = urllib.request.Request(url=jobPath, headers=head)  # 构造一个对象，封装浏览器信息
    html = ""  # 字符串
    try:
        response = urllib.request.urlopen(req) #构造http请求发送给服务器
        html = response.read().decode('gbk') #返回html是一个对象
        print(html)
    except Exception as result:
        print(result)
    return html



#def saveData(dbpath):


if __name__ == "__main__":   #当程序执行时干的事
    page = ""
    job = input("请输入你的工作类型")
    jobPath = "https://search.51job.com/list/110200,000000,0000,00,9,99,"+job+",2,"
    getData(jobPath)
    #saveData(dbpath)
