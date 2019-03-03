#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 19:16
# @Author  : Y4er
# @Site    : http://Y4er.com
# @File    : xianzhi.py

import requests
from bs4 import BeautifulSoup
from util.tools import randomua


def run():
    url = 'https://xz.aliyun.com'
    html = requests.get(url, headers=randomua()).text
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.select('table')[0]
    trs = table.select('tr')
    posts = []
    for tr in trs:
        title = tr.select('a', {'class': 'topic-title'})[1].text.replace('\n', '').strip()
        allurl = tr.select('a')[1].get('href')
        info = tr.select('p')[-1].text.replace('\n', '').replace(' ', '').split('/')
        cate = info[1]
        date = info[2][:-1]
        post = {
            'date': date,
            'title': title,
            'url': url + allurl,
            'cate': cate
        }
        posts.append(post)
    return posts


if __name__ == '__main__':
    run()
