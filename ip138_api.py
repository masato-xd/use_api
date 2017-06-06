#!/usr/bin/python
# -*- coding: utf-8 -*-
# python3
import httplib2
import urllib
from bs4 import BeautifulSoup

params = urllib.urlencode({'ip': '212.198.109.142', 'datatype': 'xml', 'callback': 'find'})
url = 'http://api.ip138.com/query/?' + params
headers = {"token": "9ececf18f701f399a09b5e4ad6e1b39c"}  # token为示例
http = httplib2.Http()
response, content = http.request(url, 'GET', headers=headers)

soup = BeautifulSoup(content, 'xml')

print(soup.country.string)
