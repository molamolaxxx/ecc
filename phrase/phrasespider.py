import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import saver

#base url
base_url='https://www.archchinese.com/chinese_english_dictionary.html?find='
##api url
api_url='https://www.archchinese.com/getCoreWordCompleteListByCharPinyin'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/64.0.3282.186 Safari/537.36',
        'Connection': 'keep-alive',
    }
proxy={'http':'http://172.247.33.129:3148','https':'https://172.247.33.129:3148'}

#保存所有字典的总集合
result_dict=[]
def get_word_list(char_pinyin):

    list=[]
    '''获得含有词组和字符的返回
    用正则表达式提取词组'''
    response=requests.post(api_url,data={'charpinyin':char_pinyin},headers=headers,timeout=1.5,proxies=proxy)
    #未被提取的码
    text=response.text
    #print(text)

    #找到第一个词组加入
    text='&'+text

    #找到所有的&符号，记录位置,outputisstart记录是否是输出状态
    output_is_start=False
    #记录是第几个@
    no_=1
    for s in text:
        if s=='&' or output_is_start:
            #开始输出单词
            #如果没有启动输出模式，则启动
            if not output_is_start:
                output_is_start=True
                #初始化字符串
                string=""
                continue
            #结束输出模式,第二个no
            if s=='@':
                if no_==1:
                    string=string+'/'
                    no_=2
                    continue
                output_is_start=False
                #将字符串加入list中
                list.append(string)

                no_=1
                continue
            #拼接字符
            string=string+s
    print(list)
    return list

def get_unicode(word):
    '''获得汉字的unicode'''
    str=word.encode('unicode_escape')[2:]
    return str.decode()

def get_dict(list,word,id):
    '''获得词组的字典'''
    global result_dict

    #获得数据库对象
    db=saver.connect_mysql()
    for item in list:
        sim_trad=item.split('/')
        #获得简体和繁体
        sim=sim_trad[0]
        trad=sim_trad[1]
        result_dict.append({'id':id,'word':word,'sim':sim,'trad':trad})
        #入库
        saver.save_one_item(db,item_dict={'id':id,'word':word,'sim':sim,'trad':trad})

#执行爬虫的入口
def runner(start_pos,end_pos):
    # 字集
    data_set_path = "/home/molamola/桌面/数据集/ecc/ecc-dataset/data/ecc-data.csv"
    df_wordSet = pd.DataFrame(pd.read_csv(data_set_path)).values

    while True:
        if start_pos == end_pos:
            print("结束啦>...<")
            break
        word = df_wordSet[start_pos][0]
        print(word + ":" + str(start_pos))
        # 获得词组集
        try:
            list = get_word_list(get_unicode(word))
            # 获得简繁体字典
            get_dict(list, word, start_pos)
        except Exception as err:
            print("fail")
            print(err)
        else:
            start_pos += 1
        if start_pos % 10 == 0:
            # print(result_dict)
            print("长度-------->" + str(len(result_dict)))

if __name__ == '__main__':

    #runner(20500,20695)
    #runner(20695, 20795)
    #runner(20795, 20895)
    #runner(9183, 11183)
    #runner(11183, 13183)
    #runner(13183, 15183)
    #runner(15183, 17183)
    #runner(17183, 19183)
    #runner(19183, 20500)
    list = get_word_list(get_unicode("刘"))
    # 获得简繁体字典
    get_dict(list,"刘", 20889)





