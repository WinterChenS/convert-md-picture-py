# python3爬取网络图片
import requests
import re

# 第一个爬取网址
url = 'https://blog.winterchen.com/2021/08/03/2021-08-03-spring-cloud-hoxton-4-gateway/'

# 获得网页源码
data = requests.get(url).text
# print("网站源码", data)

# 图片正则表达式
regex = r'data-src="(.*?.jpg)"'
# re是一个列表
pa = re.compile(regex)  # 创建一个pa模板，使其符合匹配的网址
ma = re.findall(pa, data)  # findall 方法找到data中所有的符合pa的对象，添加到re中并返回
# print(ma)

# 将ma中图片网址依次提取出来
i = 0
for image in ma:
    i += 1
    image = requests.get(image).content
    print(str(i) + '.jpg 正在保存。。。')
    with open('../imgs/' + str(i) + '.jpg', 'wb') as f:  # 注意打开的是就jpg文件
        f.write(image)

print('保存完毕')