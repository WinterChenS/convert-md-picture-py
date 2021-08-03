# -*-coding:utf-8-*-


import os
import re
#D:\private\study\project\blog-back\source\_posts
g = os.walk(r"/Users/winterchen/IdeaProjects/blog-back/source/_posts")


reg = re.compile('http?:*.*.(?:jpg|png)', re.S)


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
        print("this is markdown file or json file")
        with open(file_path, 'r+', encoding='utf-8') as f:
            for line in f.readlines():
                print(line)
                if re.match(reg, line):
                            m1 = reg.findall(line)
                            print(m1[0])
                else:
                            print("data Not match .")




def run():
    select_md_file_from_dir()
    





if __name__ == '__main__':
    print("=============")
    run()
