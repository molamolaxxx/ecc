'''获取对应词组的句子/获取词组的读音'''
import pandas as pd
import phrase.saver as saver
from phrase import phrasespider
import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/64.0.3282.186 Safari/537.36',
        'Connection': 'keep-alive',
    }
proxy={'http':'http://172.247.33.129:3148','https':'https://172.247.33.129:3148'}
table_name="phrase2sentence"

#词组的地址
phrase_path="/home/molamola/桌面/数据集/ecc/ecc-dataset-2/data/phrase.csv"
#读音的url
tone_url="https://www.archchinese.com/getSimpSentenceWithPinyin6"
#句子的url
sentence_url="https://www.archchinese.com/getExampleAudio3"

#获得词组读音,和释义
def get_info(phrase):
    '''
    :param phrase: 需要获取读音的词组
    请求使用post 参数
    1.unicode: 732b, 5934, 9e70,
    2.offset: 0
    3.limit: 2
    :return:
    '''
    #unicode
    phrase_unicode=""
    for s in phrase:
        if s=='.':
            continue
        phrase_unicode+=phrasespider.get_unicode(s)+','
    #print(phrase_unicode)
    #网络请求
    response = requests.post(tone_url, data={'unicode': phrase_unicode,'offset':0,'limit':25},
                             headers=headers, timeout=1.5,proxies=proxy
                             )
    response_html=response.text
    #print(response_html)

    #将解释区分以&区分
    info_list=response_html.split('&')
    return info_list

def get_sentence(phrase):
    '''
    :param phrase: 需要获取句子的词组
    请求使用post 参数
    1.unicode: 732b, 5934, 9e70,
    2.offset: 0
    3.limit: 2
    :return:
    '''
    # unicode
    phrase_unicode = ""
    for s in phrase:
        if s == '.':
            continue
        phrase_unicode += phrasespider.get_unicode(s) + ','
    # print(phrase_unicode)
    # 网络请求
    response = requests.post(sentence_url, data={'unicode': phrase_unicode, 'offset': 0, 'limit': 60},
                             headers=headers, timeout=1.5,proxies=proxy
                             )
    response_html = response.text
    #按～划分句子
    sentence_list=response_html.split('~')
    #构造句子词典
    sentence_dicts=[]
    #对其中的每一句话进行提取
    for sent_content in sentence_list:
        if sent_content=='':
            continue
        index=0
        index_list=[0]
        for s in sent_content:
            if s=='^':
                #print(index)
                index_list.append(index)
            index+=1
        #print(index_list)
        sentence_dicts.append(
            {
                'sentence':sent_content[index_list[0]:index_list[1]].replace('\r',''),
                'English':sent_content[index_list[5]+1:index_list[6]].replace('\r','')
             })
    return sentence_dicts


def get_info_dict(info_list,phrase):
    '''获得词组的information dict
    1.词组名
    2.繁体
    3.注音
    4.英文释义'''

    for info in info_list:

        list=info.split('@')

        # 如果内容为空
        if list[0]=='' or list[0]!=phrase:
            continue
        else:
            return {'sim':list[0].replace('\r',''),'trad':list[1].replace('\r',''),'tone':list[2].replace('\r',''),'eng':list[3].replace('\r','')}

if __name__ == '__main__':

    #获得词组的df
    phrases_df=pd.DataFrame(pd.read_csv(phrase_path))

    #获得词组集合
    phrases=phrases_df['phrase'].values

    print("总共有"+str(len(phrases))+"条数据")
    #控制码
    print("请输入开始的index")
    start_pos=input()
    start_pos=int(start_pos)
    print("请输入结束的index")
    end_pos=input()
    end_pos=int(end_pos)
    while True:
        if start_pos==end_pos:
            print("结束啦>.<")
            break
        print("index:"+str(start_pos))
        #获取对应词组
        phrase=phrases[start_pos]
        print("对应词组:"+phrase)
        try:

            #获得词语字典
            dict=get_info_dict(get_info(phrase),phrase)
            #获取句子
            sentences=get_sentence(phrase)

        except Exception as err:
            print(err)
        else:
            if dict !=None:
                #字典入库
                db=saver.connect_mysql()
                saver.save_phrase_info(db,dict)
                print(dict)
            else:
                print("词语字典为空")

            if sentences==[]:
                print("不存在句子!")
            else:
                for sentence in sentences:
                    print(sentence)
                    #句子入库
                    saver.save_sentence_info(db,sentence)
            start_pos+=1


