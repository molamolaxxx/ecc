from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd

table_url="https://chinese.yabla.com/chinese-pinyin-chart.php"
audio_base_url="https://yabla.vo.llnwd.net/media.yabla.com/chinese_static/audio/alicia/"
path="/home/molamola/桌面/数据集/ecc/audio/"
#需要替换的字母
replace_word='ü'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/64.0.3282.186 Safari/537.36',
        'Connection': 'keep-alive',
    }
m_content=['dun', 'ta', 'te', 'tai', 'tei', 'tao', 'tou', 'tan', 'tang', 'teng', 'tong', 'ti', 'tiao', 'tie', 'tian', 'ting', 'tu', 'tuo', 'tui', 'tuan', 'tun', 'na', 'ne', 'nai', 'nei', 'nao', 'nou', 'nan', 'nen', 'nang', 'neng', 'nong', 'ni', 'niao', 'nie', 'niu', 'nian', 'nin', 'niang', 'ning', 'nu', 'nuo', 'nuan', 'nv', 'nve', 'la', 'le', 'lai', 'lei', 'lao', 'lou', 'lan', 'lang', 'leng', 'long', 'li', 'lia', 'liao', 'lie', 'liu', 'lian', 'lin', 'liang', 'ling', 'lu', 'luo', 'luan', 'lun', 'lv', 'lve', 'ga', 'ge', 'gai', 'gei', 'gao', 'gou', 'gan', 'gen', 'gang', 'geng', 'gong', 'gu', 'gua', 'guo', 'guai', 'gui', 'guan', 'gun', 'guang', 'ka', 'ke', 'kai', 'kei', 'kao', 'kou', 'kan', 'ken', 'kang', 'keng', 'kong', 'ku', 'kua', 'kuo', 'kuai', 'kui', 'kuan', 'kun', 'kuang', 'ha', 'he', 'hai', 'hei', 'hao', 'hou', 'han', 'hen', 'hang', 'heng', 'hong', 'hu', 'hua', 'huo', 'huai', 'hui', 'huan', 'hun', 'huang', 'za', 'ze', 'zi', 'zai', 'zei', 'zao', 'zou', 'zan', 'zen', 'zang', 'zeng', 'zong', 'zu', 'zuo', 'zui', 'zuan', 'zun', 'ca', 'ce', 'ci', 'cai', 'cao', 'cou', 'can', 'cen', 'cang', 'ceng', 'cong', 'cu', 'cuo', 'cui', 'cuan', 'cun', 'sa', 'se', 'si', 'sai', 'sao', 'sou', 'san', 'sen', 'sang', 'seng', 'song', 'su', 'suo', 'sui', 'suan', 'sun', 'zha', 'zhe', 'zhi', 'zhai', 'zhei', 'zhao', 'zhou', 'zhan', 'zhen', 'zhang', 'zheng', 'zhong', 'zhu', 'zhua', 'zhuo', 'zhuai', 'zhui', 'zhuan', 'zhun', 'zhuang', 'cha', 'che', 'chi', 'chai', 'chao', 'chou', 'chan', 'chen', 'chang', 'cheng', 'chong', 'chu', 'chua', 'chuo', 'chuai', 'chui', 'chuan', 'chun', 'chuang', 'sha', 'she', 'shi', 'shai', 'shei', 'shao', 'shou', 'shan', 'shen', 'shang', 'sheng', 'shu', 'shua', 'shuo', 'shuai', 'shui', 'shuan', 'shun', 'shuang', 're', 'ri', 'rao', 'rou', 'ran', 'ren', 'rang', 'reng', 'rong', 'ru', 'rua', 'ruo', 'rui', 'ruan', 'run', 'ji', 'jia', 'jiao', 'jie', 'jiu', 'jian', 'jin', 'jiang', 'jing', 'jiong', 'ju', 'jue', 'juan', 'jun', 'qi', 'qia', 'qiao', 'qie', 'qiu', 'qian', 'qin', 'qiang', 'qing', 'qiong', 'qu', 'que', 'quan', 'qun', 'xi', 'xia', 'xiao', 'xie', 'xiu', 'xian', 'xin', 'xiang', 'xing', 'xiong', 'xu', 'xue', 'xuan', 'xun']

def get_audio_name():
    '''获得读音的名称'''

    #请求图表内容
    res=requests.get(url=table_url,headers=headers)
    html_doc=res.text

    #化为soup文件
    soup=BeautifulSoup(html_doc,'html.parser')
    #print(soup)

    #找到表格
    td_s=soup.find_all('td',{'class':'val'})

    audio_content=[]
    for td in td_s:

        audio_name=td.text
        audio_name=audio_name.replace(replace_word,'v')
        #print(audio_name)
        audio_content.append(audio_name)

    return audio_content

def download_audio(audio_content):

    '''下载音频,保存'''
    for audio_name in audio_content:

        for i in range(4):
            i+=1

            #文件名称
            file_name=audio_name+str(i)+'.mp3'
            file_path=path+file_name

            #获得音频的url
            audio_url=audio_base_url+file_name
            audio=requests.get(audio_url,headers=headers)
            print(len(audio.content))

            #保存到文件
            with open(file_path,'wb') as f:
                f.write(audio.content)

            print(file_name+":完成")

def get_content():
    '''平均分，多进程爬虫'''
    print("请输入部分：")
    part=input()
    part=int(part)

    part_content=[]

    for i in range(30):
        i=part*30+i
        try:
            part_content.append(m_content[i])
        except:
            break

    print(part_content)
    return part_content

if __name__ == '__main__':

    #获得拼音名称
    #download_audio(get_content())
    #print(get_audio_name())
    get_content()