#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/3/20 下午3:09
# @Author   : jerry
# @File     : use_bs4_damo.py
# @Software : PyCharm


import requests
from bs4 import BeautifulSoup

url = 'https://bj.lianjia.com/zufang/'
responce = requests.get(url)
soup = BeautifulSoup(responce.text, "html.parser")
links_div = soup.find_all('div', class_="pic-panel")
links = [div.a.get('href') for div in links_div]

print links, len(links)
