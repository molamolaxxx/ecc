'''单独声母和韵母的mp3'''
import requests
from bs4 import BeautifulSoup

base_url="http://www.maxmandarin.com/lesson.php?lesson=pinyin0"
def get_audio_content():

    content=[]
    for i in range(1,8):

        i=str(i)
        #get
        response=requests.get(base_url+i)
        #print(response.text)

        #get soup
        soup=BeautifulSoup(response.text,'html.parser')
        #print(soup)

        href_list=soup.find_all('strong',{'style':"font-family: Verdana, Geneva, Tahoma, sans-serif"})

        for href in href_list:
            str_=href.text
            str_=str_.replace('ü','v')
            content.append(str_)

    print(content)
    return content

if __name__ == '__main__':

    path="/home/molamola/桌面/数据集/ecc/audio-data/shengmu-yunmu/"
    for i in get_audio_content():

        url = "http://www.maxmandarin.com/audio/pinyin_" + i + ".mp3"
        # 文件名称
        file_name = i+ '.mp3'
        file_path = path + file_name

        # 获得音频的url
        audio = requests.get(url)
        print(len(audio.content))

        # 保存到文件
        with open(file_path, 'wb') as f:
            f.write(audio.content)

        print(file_name + ":完成")
