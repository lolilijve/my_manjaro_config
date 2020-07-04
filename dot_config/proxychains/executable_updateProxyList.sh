#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import time
import os
from bs4 import BeautifulSoup

url = "https://www.kuaidaili.com/free/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

def get_proxy_datas():
    r = requests.get(url,headers=headers)
    content = r.content
    soup = BeautifulSoup(content,'lxml')
    ips =soup.find_all('td',attrs={'data-title':'IP'})
    ports = soup.find_all('td',attrs={'data-title':'PORT'})
    print('开始写入代理IP和端口......')
    write_conf(ips,ports)
    print("代理ID和端口写入完成，将退出......")

def write_conf(ips,ports):
    for i in range(0,len(ips)):
        print("--->IP:"+ips[i].string+"PORT:"+ports[i].string+"<---")
        time.sleep(1)
        with open('~/.config/proxychains/pachong.conf','a+') as f:
            f.write('http %s %s\n'%(ips[i].string,ports[i].string))

get_proxy_datas()
