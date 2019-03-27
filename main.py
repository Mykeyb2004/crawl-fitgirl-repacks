#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '1.0.0'
__author__ = '张奇进'

from requests_html import HTMLSession

url_base = 'http://fitgirl-repacks.site/all-my-repacks-a-z/'


def get_pagelist(url):
    r = session.get(url)
    page_list = r.html.xpath('//*[@id="lcp_instance_0"]')


    game = ''
    for i in page_list:
        game += i.text
        print(i.text)
        print(i.links)


    list = game.split('\n')
    return list


if __name__ == '__main__':
    session = HTMLSession()
    r = session.get(url_base)

    url = url_base
    page_list = []
    game_list = []

    get_pagelist(url)

    # for html in r.html:
    #     print(url)
    #     page_list = get_pagelist(url)
    #     game_list.extend(page_list)
    #     url = html.next()
