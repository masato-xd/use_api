# coding: utf-8

import requests
from bs4 import BeautifulSoup

infos = []

name_ids = r'D:\Users\xudeng\Documents\GitHub\use_api\id.txt'
with open(name_ids) as id_file:
    for name_id in id_file:
        name_id = name_id.strip()
        if name_id:
            # 执行API调用并存储响应
            url = "http://sso.ztgame.com/passport/syswork/base/base_ad_user_list.php?" \
                  "username=&display_name=&staff_num=%s&tel=" % name_id
            r = requests.get(url)

            # 指定要解析的格式
            soup = BeautifulSoup(r.text, 'html.parser')

            # 打印所有内容
            # print(soup.prettify())
            trs = soup.find_all('tr')
            name = trs[1].contents[3].string
            num = trs[1].contents[5].string
            phone = trs[1].contents[7].string
            zhiwu = trs[1].contents[9].get_text()
            bumen = trs[1].contents[11].get_text()
            # print(type(zhiwu))
            print("{:<5} {:<5} {:<5} {:<10} {:<20}".format(name, num, phone, zhiwu, bumen))
            # for i in trs[1].stripped_strings:
            #     print('{:^14s}'.format(i), end=' ')
        # print('')