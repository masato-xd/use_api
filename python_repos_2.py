# coding: utf-8

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
# print dir(r)
print "Status code:", r.status_code

# 将api响应存储在一个变量中
response_dict = r.json()
print "Total repositories:", response_dict['total_count']

# 探索有关仓库的信息
repo_dicts = response_dict['items']


names, stars = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])


	# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45 			# 绕x轴旋转45度
my_config.show_legend = False				# 不显示图例
my_config.title_font_size = 24				# 标题大小
my_config.label_font_size = 24				# 标签大小
my_config.major_label_font_size = 18		# 主要标签字体大小
my_config.truncate_label = 12				# 截断(鼠标悬浮显示全部名称) 15个字符, -1: 不截断
my_config.show_y_guides = False				# 不显示y轴水平说明
my_config.width = 1000



chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')



