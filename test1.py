# -*- coding = utf-8 -*-
# @Time : 2022/1/12 10:03 PM
# @Author : CZJ
# @File  :   test1.py
# @software : PyCharm
import json
import re
import sqlite3

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
    initdb(dbpath)
    #把每个job_list中的数据放入数据库中
    db = sqlite3.connect("test_job.db")
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
    job_list = []      #用来存放工作的数据
    dbpath = "test_job.db"
    html = open(r"a job.html")
    bs = bs4.BeautifulSoup(html, "html.parser")
    data = bs.find_all("script", type= "text/javascript")
    detail_link = re.compile(r'window.__SEARCH_RESULT__ = (.*?)</script>', re.S)
    json_data = re.findall(detail_link, str(data))   #整个页面的所有工作消息都存放在这个json数据中
    dic_data = json.loads(json_data[0])     #提取第一个元素，转换成字典
    for key, value in dic_data.items():
       if key == "engine_jds":   #每个工作详细数据存放在engine_jds中
           for item in value:
               job_list.append(find_data(item))
    saveData(dbpath, job_list)




# top_ads
# auction_ads
# market_ads
# engine_jds
# jobid_count
# group
# banner_ads
# is_collapseexpansion
# co_ads
# keyword_recommendation
# search_condition
# searched_condition
# curr_page
# total_page
# keyword_ads
# job_search_assistance
# seo_title
# seo_description
# seo_keywords
#




