2016 12-29
使用git_api
转移到windows

2016 12-30

```python
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS, Style
```

##### 样式设置
```
my_style = Style()
my_style = LS('#333366', base_style=LCS)
```

##### 主要参数
```
my_style.title_font_size = 12				# 标题大小
my_style.label_font_size = 8 				# 标签大小
my_style.major_label_font_size = 10			# 主要标签字体大小
my_style.tooltip_font_size = 5				# 提示工具的大小
plot_dict = {
    'value': repo_dict['stargazers_count'],		# 图像块上的值
    'label': repo_dict['description'],			# 显示的文本
    'xlink': repo_dict['html_url']				# 块的超链接
}
```

##### 配置设置
```
my_config = pygal.Config()
my_config.x_label_rotation = 45 			# 绕x轴旋转45度
my_config.show_legend = False				# 不显示图例
my_config.truncate_label = 12				# 截断(鼠标悬浮显示全部名称) 15个字符, -1: 不截断
my_config.show_y_guides = True				# 不显示y轴水平说明
my_config.width = 1000					# 宽度, 更适配浏览器
```

##### 添加到svg文件, 在浏览器显示
```
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
```