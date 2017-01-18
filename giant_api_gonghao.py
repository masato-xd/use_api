# coding: utf-8

import requests
from bs4 import BeautifulSoup


# 执行API调用并存储响应
url = 'http://sso.ztgame.com/passport/syswork/base/base_ad_user_list.php?username=&display_name=&staff_num=10786&tel='
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
print soup.find_all('td')