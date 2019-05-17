import spiderApi as api
import pandas as pd
import saver as saver

sleep_time=0
if __name__ == '__main__':

    #计数器
    click=0
    command=pd.read_csv("/home/molamola/桌面/数据集/ecc/ecc-command-2.csv")['0'].values

    #加载可用代理
    ips=pd.read_csv("/home/molamola/桌面/数据集/ecc/proxies.csv")['0'].values
    proxies=[]
    for ip in ips:
        proxy={'https': 'https://'+ip}
        proxies.append(proxy)
    #获得控制码，进行爬取

    '''控制循环变量'''
    command_i=3200
    end_i=4096
    #记录下标志点
    flag=str(command_i)
    proxy_i=0

    #获得数据库
    db=saver.connect_mysql()
    while True:
        #获得各自的代理和控制码
        if command_i==end_i:
            #结束
            print("爬虫结束-----------------****** > . <")
            break

        command_code=command[command_i]
        proxy=proxies[proxy_i]
        #获得url
        url="https://bihua.51240.com/"+command_code+"__bihuachaxun/"
        try:
            print(url)
            item_dict=api.get_word_order_dict(url=url,proxies=proxy,flag=flag)
            print(item_dict)
        except Exception as err:
            print("failed")
            print(str(err))
            if str(err) =='list index out of range':
                # 控制码加一
                command_i += 1
            #代理加一
            proxy_i=(proxy_i+1)%len(proxies)
        else:
            print("success:"+str(command_i))
            print(proxy)
            #保存到数据库
            saver.save_one_item(database=db,item_dict=item_dict,index=command_i)

            #控制码加一
            command_i+=1

            # 代理加一
            proxy_i = (proxy_i + 1) % len(proxies)

        #api.get_word_order_dict(url="https://bihua.51240.com")
            # driver