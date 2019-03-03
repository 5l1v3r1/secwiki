#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 17:02
# @Author  : Y4er
# @Site    : http://Y4er.com
# @File    : secnews.py

import requests
from util.tools import randomua
from bs4 import BeautifulSoup


def run():
    url = 'http://wiki.ioin.in'
    html = requests.get(url, headers=randomua())
    soup = BeautifulSoup(html.text, 'html.parser')
    tbody = soup.select('tbody')[0]
    trs = tbody.select('tr')
    posts = []
    for tr in trs:
        date = tr.select('td')[0].text
        title = tr.select('td')[1].text.replace('\n', '').strip()
        allurl = tr.select('td')[1].find('a').get('href')
        cate = tr.select('td')[2].text
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
