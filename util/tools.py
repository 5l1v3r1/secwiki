#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 17:05
# @Author  : Y4er
# @Site    : http://Y4er.com
# @File    : tools.py

import random
import hashlib


def randomua():
    uas = []
    with open(r'util/ua.txt', 'r') as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            uas.append(line)
    headers = {
        'User-Agent': random.choice(uas)
    }
    return headers


def md5(string):
    md = hashlib.md5()
    md.update(string.encode(encoding='utf-8'))
    return md.hexdigest()
