import requests
import pandas as pd

#保存部首src集合，用来查重
src_dict=[]
#src_cont=pd.read_csv("/home/molamola/桌面/数据集/ecc/img_status.csv").values
#print("cont"+src_cont)

#图片保存的地址
save_url="/home/molamola/桌面/数据集/ecc/ecc-dataset/img/"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                      'AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/64.0.3282.186 Safari/537.36',
        'Connection': 'keep-alive',
    }

def get_image_by_url(url):

    '''通过url获得部首的图片'''
    img=requests.get(url,headers=headers)

    #抛出响应结果
    img.raise_for_status()
    return img

def run_getter(img_content,flag):

    '''外部函数调用的接口'''
    for img_info in img_content:

        src=img_info['src']
        url="http:"+src
        #获得单张图片
        if not is_same_img_exist(img_info):
            #如果没有重复,抓取保存图片
            #img=get_image_by_url(url)

            #提取path
            path=save_url+img_info['alt']+'.gif'

            print(path)

            # 保存图片
            #save(img,path)

            #加入部首字典
            src_dict.append(img_info)

            #保存状态
            save_img_status(flag)

def save(img,path):

    with open(path,'wb') as f:
        f.write(img.content)
    '''将图片保存在指定文件夹'''

def is_same_img_exist(src):

    '''查询数据库或内存中有没有相同的部首
        有，返回False
        没有，返回true'''

    if src in src_dict:
        #在
        return True
    else:
        #不在
        return False

def save_img_status(flag):

    img_df=pd.DataFrame(src_dict)

    img_df.to_csv("/home/molamola/桌面/数据集/ecc/img_status_"+flag+".csv")

if __name__ == '__main__':

    status_df=pd.read_csv("/home/molamola/桌面/数据集/ecc/ecc-dataset/img_status.csv")

    status=status_df['src'].values

    for s in  status:
        url="http:"+s
        print(url)
        path=save_url+s.split('/')[-1]

        print(path)

        #下载并保存

        save(get_image_by_url(url),path)