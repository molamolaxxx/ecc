from bs4 import BeautifulSoup
from urllib import request
import spiderApi as api
from selenium import webdriver
import time


content_word=['猫','狗','蛇','神','猪']
#爬虫入口函数
if __name__ == '__main__':
    # driver
    driver = webdriver.Chrome()

    driver.set_script_timeout(20)
    driver.set_page_load_timeout(20)

    try:
        driver.get('https://bihua.51240.com/')
    except:
        print("太慢，停止加载")

    for _ in range(100):
        for word in content_word:
            print(api.get_word_order_dict(driver=driver,word=word))


