#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/15 上午10:23
# @Author  : herbiel8800@gmail.com
# @Site    : 
# @File    : index.py
# @Software: PyCharm
import json
import time

import requests


def get_header():
    '''get header
    :return: header
    '''
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Host': 'interface.sina.cn',
        'Referer': 'https://news.sina.cn/zt_d/yiqing0121',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    return headers
def req_get(headers, url, query):
    '''GET method
    :param headers: header
    :param url:  url
    :return: json result
    '''
    resp = requests.get(url, headers=headers,params=query)
    return resp


def getDataSync(number):
    '''GET sync data
    :return: data
    '''
    headers = get_header()
    query = {'username': 'sms', 'password': 'pesoq2018'}
    url = 'http://161.49.197.35:{port}/goip_get_sms_stat.html?'.format(
        port=number)
    result = req_get(headers, url, query)
    return result.json()

if __name__ == '__main__':
    print(getDataSync())