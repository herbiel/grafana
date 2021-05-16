#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/15 上午10:23
# @Author  : herbiel8800@gmail.com
# @Site    : 
# @File    : index.py
# @Software: PyCharm
import time
from datetime import datetime

from bottle import (Bottle, HTTPResponse, request, response, run, json_dumps as dumps)

from getData import getDataSync

app = Bottle()


def get_rows(data_list):
    rows = []
    for data in data_list['stats']:
        if data['sent'] != 0:
            success_per = "%.2f%%" % (data['sent_ok'] / data['sent'] * 100)
        else:
            success_per = "0%"
        row = [data['port'], data['sent'], data['sent_failed'], data['sent_ok'], data['unsent'], success_per]
        rows.append(row)
    return rows


@app.hook('after_request')
def enable_cors():
    print(request.json)
    print("after_request hook")
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = \
        'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


@app.route("/", method=['GET', 'OPTIONS'])
def index():
    return "UP"


@app.post('/search')
def search():
    return HTTPResponse(body=dumps(
        ['pool1', 'pool2', 'pool3', 'pool4', 'pool5']),
        headers={'Content-Type': 'application/json'})


@app.post('/query')
def query():
    body = []
    all_data_1 = getDataSync(9000)
    all_data_2 = getDataSync(8015)
    all_data_3 = getDataSync(10029)
    all_data_4 = getDataSync(10250)
    all_data_5 = getDataSync(38080)
    time_stamp = int(round(time.time() * 1000))
    if request.json['targets'][0]['type'] == 'table':
        pool_1_rows = get_rows(all_data_1)
        pool_2_rows = get_rows(all_data_2)
        pool_3_rows = get_rows(all_data_3)
        pool_4_rows = get_rows(all_data_4)
        pool_5_rows = get_rows(all_data_5)
        bodies = {'pool1': [{
            "columns": [
                {"text": "端口", "type": "name"},
                {"text": "发送量", " type": "sent"},
                {"text": "发送失败", " type": "sent_failed"},
                {"text": "发送成功", "type": "sent_ok"},
                {"text": "待发送", "type": "unsent"},
                {"text": "成功率", "type": "successper"}
            ],
            "rows": pool_1_rows,
            "type": "table"
        }],
            'pool2': [{
                "columns": [
                    {"text": "端口", "type": "name"},
                    {"text": "发送量", " type": "sent"},
                    {"text": "发送失败", " type": "sent_failed"},
                    {"text": "发送成功", "type": "sent_ok"},
                    {"text": "待发送", "type": "unsent"},
                    {"text": "成功率", "type": "successper"}
                ],
                "rows": pool_2_rows,
                "type": "table"
            }],
            'pool3': [{
                "columns": [
                    {"text": "端口", "type": "name"},
                    {"text": "发送量", " type": "sent"},
                    {"text": "发送失败", " type": "sent_failed"},
                    {"text": "发送成功", "type": "sent_ok"},
                    {"text": "待发送", "type": "unsent"},
                    {"text": "成功率", "type": "successper"}
                ],
                "rows": pool_3_rows,
                "type": "table"
            }],
            'pool4': [{
                "columns": [
                    {"text": "端口", "type": "name"},
                    {"text": "发送量", " type": "sent"},
                    {"text": "发送失败", " type": "sent_failed"},
                    {"text": "发送成功", "type": "sent_ok"},
                    {"text": "待发送", "type": "unsent"},
                    {"text": "成功率", "type": "successper"}
                ],
                "rows": pool_4_rows,
                "type": "table"
            }],
            'pool5': [{
                "columns": [
                    {"text": "端口", "type": "name"},
                    {"text": "发送量", " type": "sent"},
                    {"text": "发送失败", " type": "sent_failed"},
                    {"text": "发送成功", "type": "sent_ok"},
                    {"text": "待发送", "type": "unsent"},
                    {"text": "成功率", "type": "successper"}
                ],
                "rows": pool_5_rows,
                "type": "table"
            }]
        }

        series = request.json['targets'][0]['target']
        body = dumps(bodies[series])
    return HTTPResponse(body=body, headers={'Content-Type': 'application/json'})


if __name__ == '__main__':
    run(app=app, host='0.0.0.0', port=8000)
