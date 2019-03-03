#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 19:03
# @Author  : Y4er
# @Site    : http://Y4er.com
# @File    : main.py
import os
import importlib as imp
from util.savepdf import savepdf
from util.tools import md5

if __name__ == '__main__':
    path = os.path.split(os.path.realpath(__file__))[0]
    plugins = os.listdir(path + '/plugin/')
    try:
        for plugin in plugins:
            if '__' in plugin:
                continue
            module = imp.import_module('plugin.' + plugin[:-3])
            posts = module.run()

            for post in posts:
                url = post['url']
                path = 'out' + '/' + post['cate'] + '/' + post['title'] + ' ' + post['date'] + '.pdf'
                with open('md5.txt', 'r') as f:
                    if md5(path) in f.read().splitlines():
                        print(path + "已存在,跳过.")
                        continue
                print(path, url)
                savepdf(url, path)
                with open('md5.txt', 'a') as f:
                    f.write(md5(path) + '\n')
    except Exception as e:
        if 'please use headless' not in e:
            print(e)
    finally:
        f.close()
