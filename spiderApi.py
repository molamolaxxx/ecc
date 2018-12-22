from bs4 import BeautifulSoup
from urllib import request
import requests
from selenium import webdriver
import time

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/64.0.3282.186 Safari/537.36',
        'Connection': 'keep-alive',
        'Cookie':'Hm_lvt_b66d1acae99e04b29d94083011e9e13c=1545142027,1545142460,1545188425,1545292984; Hm_lvt_fbe0e02a7ffde424814bef2f6c9d36eb=1545294542,1545294686,1545298203,1545375976; Hm_lpvt_fbe0e02a7ffde424814bef2f6c9d36eb=1545376019'
    }
proxies = {'http':'http://61.135.217.7:80','https':'https://60.176.37.161:8118'}

'''结合自动化driver和普通request请求的api
自动化driver：driver驱动 word关键字
普通get：url
'''
def get_word_order_dict(url=None,driver=None,word=None):

    #如果是自动化控制模式
    if driver!=None:
        #输入汉字的textbox
        text_box=driver.find_element_by_id('ss_tj_value_1')
        #清空text
        text_box.clear()
        #输入汉字
        text_box.send_keys(word)
        #点击查询
        click=driver.find_element_by_id('ss_tj_button_1')
        click.click()

        time.sleep(1)
        #模拟按下esc停止加载
        #获得源码
        html_doc = driver.page_source
    #web爬虫模式
    else:
        #get请求
        response=requests.get(url=url,headers=headers)
        html_doc=response.text

    #html_doc = my_res.read()
    # 化成树形结构
    soup = BeautifulSoup(html_doc, "html.parser")

    img_soup = soup.find_all('img', {'height': '22'})

    # 保存order的中文数组
    order = ''
    for img_tag in img_soup:
        order = order + ' '+img_tag['alt']
    order=order.strip()
    # 所选汉字
    word_soup = soup.find_all('td', {'style': 'font-size:16px;'})
    word = ""


    #提取汉字
    for w in word_soup[0].text:
        if (w == " "):
            break
        else:
            word = word + w
    #print(word)
    return {"word":word,"order":order}