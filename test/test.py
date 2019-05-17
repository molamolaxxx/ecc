
import requests
from bs4 import BeautifulSoup

proxy={'http':'http://172.247.33.129:3148','https':'https://172.247.33.129:3148'}
url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E6%9F%A5%E7%9C%8Bip&oq=%25E7%25BB%25B4%25E5%259F%25BA%25E7%2599%25BE%25E7%25A7%2591&rsv_pq=cb89ff5300096cf7&rsv_t=01e76Ma%2Bu7YachMpsNSuHGr%2B079PAX2Yj3vJ9gxYcvbNFpsap53UfLnPRIo&rqlang=cn&rsv_enter=0&inputT=2977&rsv_sug3=109&rsv_sug1=70&rsv_sug7=100&rsv_sug2=0&rsv_sug4=2977'
url_2='http://www.google.com'

response=requests.get(url=url,proxies=proxy)

soup=BeautifulSoup(response.text,'html.parser')
s=soup.find_all('span',{'class':'c-gap-right'})

print(s)