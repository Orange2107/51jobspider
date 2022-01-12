# -*- coding = utf-8 -*-
# @Time : 2022/1/12 10:03 PM
# @Author : CZJ
# @File  :   test1.py
# @software : PyCharm
import json
import re

import bs4
from bs4 import  BeautifulSoup

def find_data(dic_data2):
    for key, value in dic_data2.items():
        if key == 'job_title':
            print(value)



if __name__ == "__main__":   #当程序执行时干的事
    href = []
    name = []
    html = open(r"a job.html")
    bs = bs4.BeautifulSoup(html, "html.parser")
    data = bs.find_all("script", type= "text/javascript")
    detail_link = re.compile(r'window.__SEARCH_RESULT__ = (.*?)</script>', re.S)
    json_data = re.findall(detail_link, str(data))
    dic_data = json.loads(json_data[0])
    #print(dic_data)
    for key, value in dic_data.items():
       if key == "engine_jds":
           for item in value:
               find_data(item)








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




