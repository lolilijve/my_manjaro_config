#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from os import mknod
import requests
import os
import re
import sys
import base64
from bs4 import BeautifulSoup
from pathlib import Path

url = "https://github.com/Alvin9999/new-pac/wiki/v2ray%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7"
url1 = "https://github.com/iwxf/free-v2ray"
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

# 需要获取参数的项
configItems = {
    "address": "add",
    "port": "port",
    "id": "id",
    "alterId": "aid",
    "network": "net",
    "security": "tls",
    "serverName": "host",
    "path": "path",
    "Host": "host"
}
# json 字符串的项
jsonItems = [
    "address", "port", "id", "alterId", "network", "security", "serverName",
    "path", "Host"
]
# 配置文件中各对象对应到的下标
objectItems = {
    "vnext": 2,
    "users": 4,
    "streamSettings": 6,
    "tlsSettings": 7,
    "wsSettings": 8,
    "headers": 9
}
# 参数为数字的下标
numItems = [1, 3]


# 從json中獲取參數寫入配置文件
def get_proxy_params(jsonStr):
    j = json.loads(jsonStr)
    # 读取配置文件
    paramsJson = read_config()
    # 修改配置
    print("代理ip ： " +
          paramsJson["outbounds"][0]["settings"]["vnext"][0][jsonItems[0]] +
          " =>> 變更爲 =>> " + j["add"])
    for i in range(0, len(jsonItems)):
        p = j[configItems[jsonItems[i]]] if i not in numItems else int(
            j[configItems[jsonItems[i]]])
        if i < objectItems["vnext"]:
            paramsJson["outbounds"][0]["settings"]["vnext"][0][
                jsonItems[i]] = p
        elif i < objectItems["users"]:
            paramsJson["outbounds"][0]["settings"]["vnext"][0]["users"][0][
                jsonItems[i]] = p
        elif i < objectItems["streamSettings"]:
            paramsJson["outbounds"][0]["streamSettings"][jsonItems[i]] = p
        elif i < objectItems["tlsSettings"]:
            paramsJson["outbounds"][0]["streamSettings"]["tlsSettings"][
                jsonItems[i]] = p
        elif i < objectItems["wsSettings"]:
            paramsJson["outbounds"][0]["streamSettings"]["wsSettings"][
                jsonItems[i]] = p
        elif i < objectItems["headers"]:
            paramsJson["outbounds"][0]["streamSettings"]["wsSettings"][
                "headers"][jsonItems[i]] = p
    # 写入配置文件
    write_config(paramsJson)


# 获取 配置参数的 json 字符串
def get_param_json(num):
    r = requests.get(url, headers=headers)
    content = r.content
    soup = BeautifulSoup(content, 'lxml')
    params = soup.find_all('p')
    vmessList = []
    for param in params:
        # 提取 vmess
        paramStr = param.string
        if paramStr != '[]':
            p = regular_deal("vmess://", paramStr)
            if len(p) > 0:
                vmessList.append(p[0])
    return base64.b64decode(vmessList[num])


# 获取 配置参数的 json 字符串
def get_param_json1(num):
    r = requests.get(url1, headers=headers)
    content = r.content
    soup = BeautifulSoup(content, 'lxml')
    params = soup.find_all('code')
    vmessList = []
    for param in params:
        # 提取 vmess
        paramStr = param.string
        if paramStr != '[]':
            ps = re.finditer("vmess://(.*?)\\s", paramStr)
            for p in ps:
                vmessList.append(p.group(1))
    return base64.b64decode(vmessList[num])


# 正则处理文本
def regular_deal(s, pStr):
    # 取特征值之后的数据
    pattern = re.compile("^.*?" + s + "([^\s]+)$", re.IGNORECASE)
    return pattern.findall(str(pStr))


# 读取配置
def read_config():
    config_file_path = os.path.expanduser('~') + '/.config/v2ray/config-temp.json'
    my_file = Path(config_file_path)
    if my_file.is_file() == False:
        os.mknod(config_file_path)
    with open(config_file_path, 'r') as load_f:
        load_dict = json.load(load_f)
    return load_dict


# 写入配置
def write_config(new_dict):
    config_file_path = os.path.expanduser('~') + '/.config/v2ray/config.json'
    my_file = Path(config_file_path)
    if my_file.is_file() == False:
        os.mknod(config_file_path)
    with open(config_file_path, 'w') as f:
        json.dump(new_dict, f)


def do_main():
    webNo = input(
        "請選擇v2ray配置網站： \n 1. github.com/iwxf/free-v2ray (默認) \n 2. github.com/Alvin9999/new-pac/wiki/v2ray免費帳號 \n ==> "
    )
    webNo = webNo if len(webNo) > 0 and webNo.isnumeric else 1
    num = input("請輸入v2ray配置序號：\n ==> ")
    num = num if num.isnumeric else 1
    print("获取第" + str(num) + "套配置")
    if (int(webNo) % 2).__eq__(1):
        jsonStr = get_param_json1(int(num) - 1)
    else:
        jsonStr = get_param_json(int(num) - 1)
    print('开始写入代理配置......')
    get_proxy_params(jsonStr)
    print("代理配置写入完成，将退出......")


do_main()
