'''自动探测控制码，找寻规律'''
from selenium import webdriver
import pandas as pd

df_data=pd.DataFrame(pd.read_csv("/home/molamola/桌面/数据集/ecc/汉易码编码字库全集20190118.csv"))
value=df_data.values

# driver
driver = webdriver.Chrome()

driver.get("http://www.zdic.net")

for item in value:
    word=item[1]
    text_box=driver.find_element_by_id('q')
    text_box.send_keys(word)
    break