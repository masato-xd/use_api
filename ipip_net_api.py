# coding: utf-8

import requests

filename = '22_00_yd'

# with open(filename) as ips:
# for ip in ips:
ipip_net_url = 'http://freeapi.ipip.net/218.102.155.183'
r = requests.get(ipip_net_url)
print r.content
