# -*-coding:utf-8-*-


import os
import re
import urllib.request
import string
from urllib.parse import quote
import time


#/Users/winterchen/IdeaProjects/blog-back/source/_posts
g = os.walk(r"D:\private\study\project\material-back\source\_posts")


regex = r"(http?://.*?jpg)"
local_path = "D:\\private\\study\\project\\img\\posts\\"
new_host_name_prefix = r"https://cdn.jsdelivr.net/gh/WinterChenS/img/posts/"


def select_md_file_from_dir():
    print("Selecting")
    for path,dir_list,file_list in g: 
        for file_name in file_list:              
            file_path = os.path.join(path, file_name)
            print("===============current file path=================")
            print(file_path)
            # read md file
            read_md_file(file_path, file_name)



def read_md_file(file_path, file_name):
    if(os.path.splitext(file_name)[-1] == ".md" or os.path.splitext(file_name)[-1] == ".json"):
        new_data = ''
        print("this is markdown file or json file")
        with open(file_path, 'r', encoding='utf-8') as f:
            
            for line in f.readlines():
                print(line)
                images = re.findall(regex, line)
                if len(images) == 0:
                    print("not match")
                else:
                    try:
                        url = images[0]
                        url = quote(url, safe=string.printable)
                        print("提取到图片地址：" + url)                
                        filename = os.path.basename(url)
                        print(filename)
                        t = time.time()
                        name = str(int(round(t * 1000000))) + ".jpg"
                        local_path_filename = local_path + name 
                        # download resource to local
                        urllib.request.urlretrieve(url, local_path_filename)
                        new_url = new_host_name_prefix + name
                        print("新地址为: " + new_url)
                        url = urllib.parse.unquote(url)
                        print("替换前的URL：" + url)
                        line = re.sub(url, new_url, line)
                    except Exception as e:
                        print("报错的文件：" + file_path + "报错的行：" + line)
                new_data += line
        with open(file_path, 'w', encoding='utf-8') as f2:
            f2.write(new_data)
def run():
    select_md_file_from_dir()
    





if __name__ == '__main__':
    print("=============")
    run()
