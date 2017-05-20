# coding: utf-8

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS, Style


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
# print dir(r)
print "Status code:", r.status_code

# 将api响应存储在一个变量中
response_dict = r.json()
print "Total repositories:", response_dict['total_count']

# 探索有关仓库的信息,反馈一个列表
repo_dicts = response_dict['items']


names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    if repo_dict['description'] is None:
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': 'No Description',
        }
        plot_dicts.append(plot_dict)

    else:
        plot_dict = {
            'value': repo_dict['stargazers_count'],     # 图像块上的值
            'label': repo_dict['description'],          # 显示的文本
            'xlink': repo_dict['html_url']              # 块的超链接
        }
        plot_dicts.append(plot_dict)

    # 可视化
my_style = Style()
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 12               # 标题大小
my_style.label_font_size = 8                # 标签大小
my_style.major_label_font_size = 10         # 主要标签字体大小
my_style.tooltip_font_size = 10             # 提示工具的大小
# my_style.value_font_size = 5


my_config = pygal.Config()
my_config.x_label_rotation = 45             # 绕x轴旋转45度
my_config.show_legend = False               # 不显示图例
my_config.truncate_label = 12               # 截断(鼠标悬浮显示全部名称) 15个字符, -1: 不截断
my_config.show_y_guides = True              # 不显示y轴水平说明
my_config.width = 1000                      # 宽度, 更适配浏览器


chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

# chart = pygal.Bar(print_values=True, style=DefaultStyle(
#                   value_font_family='googlefont:Raleway',
#                   value_font_size=10,
#                   value_colors=('white',)))
# chart.add('line', [0, 12, 31, 8, -28, 0])
# chart.render_to_file('python_repos.svg')
