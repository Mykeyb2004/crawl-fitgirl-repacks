#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '1.0.0'
__author__ = '张奇进'

from requests_html import HTMLSession
import csv
import os

url_root = 'http://fitgirl-repacks.site/all-my-repacks-a-z/'


def get_pagelist(url):
    session = HTMLSession()
    response = session.get(url)
    # response.encoding = response.apparent_encoding

    # url_title,存储所有要跳转的url以及对应标题
    url_title = {}
    # for element in response.html.xpath('//div[@class="postlist"]//ul[@id="pins"]//span/a'):
    for element in response.html.xpath('//*[@id="lcp_instance_0"]/li/a'):
        url = element.attrs["href"]
        title = element.text
        url_title[title] = url
    # 设置表头信息
    list = [['title', 'URL']]
    for k, v in url_title.items():
        list.append([k, v])

    session.close()
    return list


def save_csv_file(data, filename, encoding='UTF-8'):
    # 判断待保存的文件是否存在
    is_newfile = not os.access(filename, os.X_OK)

    with open(filename, "a+", newline='', encoding=encoding) as file:
        csv_file = csv.writer(file)
        for i, row in enumerate(data):
            if is_newfile:
                csv_file.writerow(row)
            else:
                if i != 0:
                    csv_file.writerow(row)


if __name__ == '__main__':
    # 设置文件保存位置
    file = (os.path.join(os.getcwd(), 'gamelist.csv'))

    # 解析根链接上所有的翻页链接
    session = HTMLSession()
    response = session.get(url_root)

    for html in response.html:
        url = html.base_url  # 根据根链接获取全部（翻页）链接
        print("Saving", url)
        list = get_pagelist(url)
        save_csv_file(list, file)
    print("gamelist.csv saved.")
