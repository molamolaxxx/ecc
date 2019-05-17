#爬取代理ip
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/64.0.3282.186 Safari/537.36',
        'Connection': 'keep-alive',
    }
base_url="https://www.xicidaili.com/wn/"
connect_url="http://www.zdic.net/z/28/js/9AB7.htm"
def get_ip_and_port():
    '''爬虫爬取代理ip网页并查询可用代理'''

    # 存储ip和端口的集合
    ip_addresses = []
    for index in range(4):
        #获得页面
        index=index+1
        #获取网页的doc
        response=requests.get(url=base_url+str(index),headers=headers)
        html_doc=response.text

        #html转化成soup结构
        soup=BeautifulSoup(html_doc,'html.parser')
        #print(soup)

        ips = soup.find_all('tr')
        ips.remove(ips[0])
        #print(len(ips))

        #找到ip和端口号
        for ip in ips:
            tds=ip.select('td')
            #print(tds[1].text,tds[2].text)
            ip_address=tds[1].text+":"+tds[2].text
            ip_addresses.append(ip_address)

    return ip_addresses
def test_connection(ips):
    '''测试爬取ip的可连接性'''
    useful_ip = []
    for ip in  ips:
        print(ip)
        proxies={'https':'https://'+ip}
        try:
            response = requests.get(url=connect_url, proxies=proxies,timeout=3.5)
        except Exception as err:
            #失败
            print("代理不可用")
            print(err)
        else:
            print("代理可用")
            useful_ip.append(ip)
    return useful_ip

def refresh_proxies():
    ips=get_ip_and_port()
    print(len(ips))
    useful_ip=test_connection(ips)

    #pandas存储
    useful_ip_df=pd.DataFrame(useful_ip)
    useful_ip_df.to_csv("/home/molamola/桌面/数据集/ecc/proxies.csv")

    return useful_ip



