import requests
from bs4 import BeautifulSoup
import image.getimage as im
import pandas as pd
import urllib.parse as parser

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/64.0.3282.186 Safari/537.36',
        'Connection': 'keep-alive',
    }
#字库
word_url="/home/molamola/桌面/数据集/ecc/ecc-dataset/data/ecc-data.csv"
path="/home/molamola/桌面/数据集/ecc/gif/"
word_list=[]
for w in pd.DataFrame(pd.read_csv(word_url)).values:
    word_list.append(w[0])

print("请输入开始")
'''2921 4342 6877 10224 10224'''
start=int(input())
print("请输入结束")
end=int(input())
while True:
    if start==end:
        print("结束--------->")
        break
    word=word_list[start]
    base_url='https://dictionary.writtenchinese.com/giffile.action?&localfile=true&fileName='+parser.quote(word)+'.gif'

    #下载图片
    try:
        image=im.get_image_by_url(base_url)
        save_path=path+word+".gif"
        #保存图片
        im.save(image,save_path)

        print(str(start)+":download success!")
    except Exception as e:
        print(e)

        print(base_url)
        if str(e)=="404 Client Error: Not Found for url: "+base_url:
            print(str(start)+":页面未找到！")
            start+=1
    else:
        start+=1




