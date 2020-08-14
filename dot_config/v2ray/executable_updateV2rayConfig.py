#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import os
import re
import sys
import base64
from bs4 import BeautifulSoup

url = "https://github.com/Alvin9999/new-pac/wiki/v2ray%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7"
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

# 需要获取参数的项
configItems = {"address" : "add", "port" : "port", "id": "id", "alterId" : "aid", "network" : "net", "security" : "tls", "serverName" : "host", "path" : "path", "Host" : "host"}
# json 字符串的项
jsonItems = ["address","port","id","alterId","network","security","serverName","path","Host"]
# 配置文件中各对象对应到的下标
objectItems = {"vnext" : 2, "users" : 4, "streamSettings" : 6, "tlsSettings" : 7, "wsSettings" : 8, "headers" : 9}
# 参数为数字的下标
numItems = [1,3]


# 爬取内容
def get_proxy_params(num):
    jsonStr = get_param_json(num)
    j = json.loads(jsonStr)
    # 读取配置文件
    paramsJson = read_config()
    # 修改配置
    print(paramsJson["outbounds"][0]["settings"]["vnext"][0][jsonItems[0]])
    for i in range(0, len(jsonItems)):
        p = j[configItems[jsonItems[i]]] if i not in numItems else int(j[configItems[jsonItems[i]]])
        if i < objectItems["vnext"]:
            paramsJson["outbounds"][0]["settings"]["vnext"][0][jsonItems[i]] = p
        elif i < objectItems["users"]:
            paramsJson["outbounds"][0]["settings"]["vnext"][0]["users"][0][jsonItems[i]] = p
        elif i < objectItems["streamSettings"]:
            paramsJson["outbounds"][0]["streamSettings"][jsonItems[i]] = p
        elif i < objectItems["tlsSettings"]:
            paramsJson["outbounds"][0]["streamSettings"]["tlsSettings"][jsonItems[i]] = p
        elif i < objectItems["wsSettings"]:
            paramsJson["outbounds"][0]["streamSettings"]["wsSettings"][jsonItems[i]] = p
        elif i < objectItems["headers"]:
            paramsJson["outbounds"][0]["streamSettings"]["wsSettings"]["headers"][jsonItems[i]] = p
    # 写入配置文件
    write_config(paramsJson)
    print("代理配置写入完成，将退出......")


# 获取 配置参数的 json 字符串
def get_param_json(num):
    r = requests.get(url, headers = headers)
    content = r.content
    soup = BeautifulSoup(content, 'lxml')
    params = soup.find_all('p')
    print('开始写入代理配置......')
    vmessList = []
    for param in params:
        # 提取 vmess
        paramStr = param.string
        if paramStr != '[]':
            p = regular_deal("vmess://", paramStr)
            if len(p) > 0:
                vmessList.append(p[0])
    return base64.b64decode(vmessList[num])


# 正则处理文本
def regular_deal(s, pStr):
    # 取特征值之后的数据
    pattern = re.compile("^.*?" + s + "([^\s]+)$", re.IGNORECASE)
    return pattern.findall(str(pStr))


# 读取配置
def read_config():
    with open(os.path.expanduser('~') + '/.config/v2ray/config.json','r') as load_f:
        load_dict = json.load(load_f)
    return load_dict


# 写入配置
def write_config(new_dict):
    with open(os.path.expanduser('~') + '/.config/v2ray/config.json', 'w') as f:
        json.dump(new_dict,f)


def do_main():
    num = 1 if len(sys.argv) <= 1 else sys.argv[1]
    print("获取第" + str(num) + "套配置")
    get_proxy_params(int(num) - 1)


do_main()