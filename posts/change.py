import os
import re
import sys
import glob
path = 'D:/2cr/temp/hugoBlog/content/temp'

for root, dirs, files in os.walk(path):
    for file in files:
        if os.path.splitext(file)[1] == '.md': # 匹配后缀名为md的文件
           
            filename = os.path.splitext(file)[0]
            comFile = os.path.join(root, file)
            # print(filename)
             # def write_file():
            # with open(file,"r+",encoding='utf-8') as f:
            #     f.seek(0)
            #     content = f.read()
            #     
            #     print(tempText)
            #     f.write(tempText)
            #     f.close()

            f = open(comFile, "r",encoding='utf-8')
            content = f.read()
            tempText = "--- \n title: "+filename+" \n date: 2020-01-01T17:11:35+08:00 \n draft: false \n tags: \n - 开发软件快捷使用 \n---\n \n" + content
            f.close()

            # 写入文件内容
            f = open(comFile, "w",encoding='utf-8')
            f.write(tempText)
            f.close()

    







