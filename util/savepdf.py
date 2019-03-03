#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 21:35
# @Author  : Y4er
# @Site    : http://Y4er.com
# @File    : savepdf.py

"""Download a webpage as a PDF."""

from selenium import webdriver


def savepdf(url, target_path):
    try:
        driver = webdriver.PhantomJS('phantomjs')
        driver.get(url)
        driver.implicitly_wait(3)
        if driver.current_url == 'about:blank':
            return True

        def execute(script, args):
            driver.execute('executePhantomScript',
                           {'script': script, 'args': args})

        driver.command_executor._commands['executePhantomScript'] = ('POST', '/session/$sessionId/phantom/execute')
        page_format = 'this.paperSize = {format: "A3", orientation: "portrait" };'
        execute(page_format, [])

        render = '''this.render("{}")'''.format(target_path)
        execute(render, [])
        return True
    except Exception as e:
        print(e)
        driver.save_screenshot(target_path + '.png')
    finally:
        driver.quit()


if __name__ == '__main__':
    url = 'https://www.chabug.org/web/637.html'
    savepdf(url, "1.pdf")
