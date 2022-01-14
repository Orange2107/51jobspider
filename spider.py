# -*- coding = utf-8 -*-
# @Time : 2022/1/12 7:59 PM
# @Author : CZJ
# @File  :   spider.py
# @software : PyCharm

import json
import re
import sqlite3
import urllib.request, urllib.error #制定url，获取页面
from urllib import parse
import time, random
import bs4
from bs4 import  BeautifulSoup


def deal_salary(money):
    if money[-1] == '千':
       money2 = money[0:-1]
       money2 = money2.split("-")
       low = float(money2[0])/10
       hight = float(money2[1])/10
       middle_salary = round((hight+low)/2, 2)
    if money[-1] == '万':
        money2 = money[0:-1]
        money2 = money2.split("-")
        low = float(money2[0])
        hight = float(money2[1])
        middle_salary = round((hight + low) / 2, 2)
    return  middle_salary

def deal_salary_year(money):
    if money[-1] == '千':
       money2 = money[0:-1]
       money2 = money2.split("-")
       low = float(money2[0])/10
       hight = float(money2[1])/10
       middle_salary = round((hight+low)/24, 2)
    if money[-1] == '万':
        money2 = money[0:-1]
        money2 = money2.split("-")
        low = float(money2[0])
        hight = float(money2[1])
        middle_salary = round((hight + low) /24, 2)
    return  middle_salary

def find_data(dic_data2):
    tap = '","'
    job_data = ""
    salary = dic_data2["providesalary_text"]
    if salary[-1] == '年':
        salary = salary[0:-2]
        middle_salary = deal_salary_year(salary)
    else:
        salary = salary[0:-2]
        middle_salary = deal_salary(salary)
    print(salary)
    job_data = '"'+dic_data2["job_name"]+tap+dic_data2["company_name"]+tap+dic_data2["workarea_text"]+tap+dic_data2["companytype_text"]+tap+str(middle_salary)+'"'
    print(job_data)
    return job_data


def getData(jobPath):
   for page in range(2, 12):         #搜索多个结果页面
       jobPath2 = jobPath + str(page)+".html"
       print(jobPath2)
       time.sleep(random.random() * 3)
       html = askUrl(jobPath2)       #返回一个搜索结果页面
       #页面解析
       bs = bs4.BeautifulSoup(html, "html.parser")
       data = bs.find_all("script", type="text/javascript")
       json_data = re.findall(detail_link, str(data))   #整个页面的所有工作消息都存放在这个json数据中
       if len(json_data) != 0:
           dic_data = json.loads(json_data[0])     #提取第一个元素，转换成字典
           for key, value in dic_data.items():
               if key == "engine_jds":  #每个工作详细数据存放在engine_jds中
                   for item in value:
                       job_list.append(find_data(item))
       else:
           print("超出页面！！！")

def askUrl(jobPath):
    head = {

        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36"
    }  # 告诉豆瓣服务器，我们是什么类型的浏览器
    proxy = {'http':'111.3.118.247：30001'}
    proxy_support = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    req = urllib.request.Request(url=jobPath, headers=head)  # 构造一个对象，封装浏览器信息
    html = ""  # 字符串
    try:
        response = urllib.request.urlopen(req) #构造http请求发送给服务器
        html = response.read().decode('gbk') #返回html是一个对象
    except Exception as result:
        print(result)
    return html



def initdb(dbpath):
    db = sqlite3.connect(dbpath)
    flag = db.cursor()
    sql = '''
        create table job(
        id integer primary key autoincrement,
        job_name text not null,
        company_name text not null,
        work_area text not null,
        company_type text not null,
        provide_salary real not null
        )'''
    flag.execute(sql)
    db.commit()
    db.close()




def saveData(dbpath, job_list):
    #initdb(dbpath)
    #把每个job_list中的数据放入数据库中
    db = sqlite3.connect("51job.db")
    flag = db.cursor()
    for job_item in job_list:
        sql = '''
        insert into job(
        job_name,company_name,work_area,company_type,provide_salary)
        values (%s) '''% job_item
        flag.execute(sql)
        print("插入成功！")
    db.commit()
    flag.close()
    db.close()


if __name__ == "__main__":   #当程序执行时干的事
    page = ""
    dbpath = "51job.db"
    job_list = []  # 用来存放工作的数据
    detail_link = re.compile(r'window.__SEARCH_RESULT__ = (.*?)</script>', re.S)
    job = input("请输入你的工作类型: ")
    job = parse.quote(parse.quote(job))
    jobPath = "https://search.51job.com/list/110200,000000,0000,00,9,99,"+job+",2,"
    getData(jobPath)

    saveData(dbpath, job_list)
