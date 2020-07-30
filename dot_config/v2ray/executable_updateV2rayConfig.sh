#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import time
import os
import re 
from bs4 import BeautifulSoup

url = "https://github.com/Alvin9999/new-pac/wiki/v2ray%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

switch = {1:"address",2:"port",3:"id",4:"alterId"}
switch1 = {1:38,2:39,3:42,4:43}

# 爬取内容
def get_proxy_datas():
    r = requests.get(url,headers=headers)
    content = r.content
    soup = BeautifulSoup(content,'lxml')
    params = soup.find_all('p')
    # ports = soup.find_all('p',attrs={'data-title':'PORT'})
    print('开始写入代理配置......')
    i = 1
    flist = read_config()
    for param in params:
        param = param.string
        if param != '[]':
            param = regular_deal(param)
            if len(param) > 0 and i <= 4:
                param = param[0]
                valueStr = ''
                if i%2 == 0:
                    valueStr = "\""+switch[i]+"\":"+param+","
                else:
                    valueStr = "\""+switch[i]+"\":\""+param+"\","
                update_config(flist,switch1[i],valueStr)
		# write_conf(param)
                i=i+1
    write_config(flist)
    print("代理配置写入完成，将退出......")

# 正则处理文本
def regular_deal(pStr):
    return re.findall(".+?:\s*?([^\s]+)",str(pStr))

# 写入文件
def write_conf(param):
    with open('/home/yujia/test.conf','a+') as f:
        f.write('%s\n'%param)

# 读取配置
def read_config():
    f=open('/home/yujia/.config/v2ray/config.json','r+')
    flist=f.readlines()
    f.close()
    return flist
    
def update_config(flist,lineNum,str):    
    flist[lineNum-1]=str+"\n"

def write_config(flist):
    f=open('/home/yujia/.config/v2ray/config.json','w+')
    f.writelines(flist)
    f.close()

get_proxy_datas()
