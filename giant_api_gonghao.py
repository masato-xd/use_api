# coding: utf-8

import requests
from bs4 import BeautifulSoup

infos = []

name_ids = 'id.txt'
with open(name_ids) as id_file:
    for name_id in id_file:

        # 执行API调用并存储响应
        url = "http://sso.ztgame.com/passport/syswork/base/base_ad_user_list.php?username=&display_name=&staff_num=%s&tel=" % name_id.rstrip()
        r = requests.get(url)

        # 指定要解析的格式
        soup = BeautifulSoup(r.text, 'html.parser')

        # 打印所有内容
        # print(soup.prettify())
        tds = soup.find_all('td')
        name = tds[9].get_text()
        num = tds[10].get_text()
        department = tds[13].get_text()

        print name, num, department
