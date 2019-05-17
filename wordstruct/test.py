from bs4 import BeautifulSoup
import requests.models
import phrase.phrasespider as spider
import pandas as pd
import wordstruct.saver as saver
base_url="http://www.zdic.net"
def get_structure(code,control):
    url=base_url+"/z/"+str(control)+"/js/"+code+".htm"
    biases=0
    try:
        response=requests.get(url)
        #print(type(response))
        #将response返回编码为utf-8
        response.encoding='utf-8'

        #print(response.text)

        soup=BeautifulSoup(response.text,"html.parser")
        #print(soup.prettify())
        #获取目标值节点(结构)
        node=soup.find('center',{}).find('a',{})
        node_text=node.text

        #获取目标值节点(部首)
        node_2=soup.find('div',{'class':'z_it2_jbs'}).find('a',{})
        node_2_text=node_2.text
    except Exception as e:
        print(str(e))
        if str(e)=="'NoneType' object has no attribute 'find'":
            return False,True
        else:
            return False,False
    else:
        return node_text,node_2_text
def get_control_code(biases):
    base_control_code_2_list=['14','15','16','17','18','19','1a','1b','1c','1d','1e','1f'\
        ,'20','21','22','23','24','25','26','27','28','29','40','e','f','10','11','12','13','14']
    base_control_code_2=base_control_code_2_list[biases]

    return base_control_code_2

def get_unicodes():

    df_data=pd.DataFrame(pd.read_csv("/home/molamola/桌面/数据集/ecc/汉易码编码字库全集20190118.csv"))
    value=df_data.values
    unicode_list=[]
    word_list=[]
    for item in value:
        word=item[1]
        unicode=item[3]
        unicode_list.append(unicode)
        word_list.append(word)
    return unicode_list,word_list

if __name__ == '__main__':
    # 加载可用代理
    ips = pd.read_csv("/home/molamola/桌面/数据集/ecc/proxies.csv")['0'].values
    proxies = []
    for ip in ips:
        proxy = {'https': 'https://' + ip}
        proxies.append(proxy)
    proxy_i=0
    #输入
    print("输入i:")
    i=int(input())
    print("输入end")
    end=int(input())

    #获得unicodes和汉字
    uni,wo=get_unicodes()

    biases=0
    while True:
        unicode=uni[i]
        word=wo[i]
        control_code=get_control_code(biases=biases)

        #获得字的结构
        structure,radicals=get_structure(unicode,control_code)
        if structure!=False:

            if i==end:
                print("end-------->")
                break

            item_dict={"word":word,"unicode":unicode,"structure":structure,"radicals":radicals}
            print("id:"+str(i))
            print("汉字:"+word)
            print("unicode:"+unicode)
            print("control_code:"+control_code)
            print("biases:" + str(biases))
            print("structure:"+str(structure))
            print("radicals:"+radicals)

            db=saver.connect_mysql()
            saver.save_one_item(db,item_dict=item_dict)
            i+=1
        else:
            if radicals==True:
                biases+=1
                print("失败！增加控制码")
            else:
                print("失败!继续")




