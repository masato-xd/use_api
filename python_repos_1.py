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
chart = pygal.Bar(style=my_style, x_label_rotation=40, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')




# print "Repositories returned:", len(repo_dicts)


# print "\nSelected information about first repository:"
# for repo_dict in repo_dicts:
# 	print "\nName:", repo_dict['name']				# 项目名称
# 	print "Owner:", repo_dict['owner']['login']		# 所有者
# 	print "stars:", repo_dict['stargazers_count']	# 星级
# 	print "repository:", repo_dict['html_url']		# url地址
# 	print "description:", repo_dict['description']	# 描述





# 研究第一个仓库
# repo_dict = repo_dicts[0]

# print "\nSelected information about first repository:"
# print "Name:", repo_dict['name']				# 项目名称
# print "Owner:", repo_dict['owner']['login']		# 所有者
# print "stars:", repo_dict['stargazers_count']	# 星级
# print "repository:", repo_dict['html_url']		# url地址
# print "created:", repo_dict['created_at']		# 创建时间
# print "updated:", repo_dict['updated_at']		# 更新时间
# print "description:", repo_dict['description']	# 描述

# print '\nKeys:', len(repo_dict)

# for key in sorted(repo_dict.keys()):
#     print key

# 处理结果
# print(response_dict.keys())
