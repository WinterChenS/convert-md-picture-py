# -*-coding:utf-8-*-


import os
import re

regex = r".*(http.*?jpg)"
line = "http://img.winterchen.com/simon-abrams-286276-unsplash.jpg\n"
res = re.match(regex, line)
print("提取到图片地址：" + res.group(1))
print(line.replace(res.group(1),"https://img.github.com/simon-abrams-286276-unsplash.jpg"))
