import spiderApi as api
import time

#字母数字集合
content=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
         'r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
#控制码,第一位e，第二位4-9,第三位a,b,8,9,第四位a-f&&0-9，第五位a,b,8,9,第六位a---f ,0-9
#控制码的三个集合
content_1=['5','6','7','8','9']
content_2=['a','b','8','9']
content_3=['a','b','c','d','e','f','1','2','3','4','5','6','7','8','9','0']
sleep_time=1
if __name__ == '__main__':
    #计数器
    click=0
    #五层循环控制
    for i1 in content_1:
        for i2 in content_2:
            for i3 in content_3:
                for i4 in content_2:
                    for i5 in content_3:
                        #获得控制码，进行爬取
                        command_code='e'+i1+i2+i3+i4+i5
                        #获得url
                        url="https://bihua.51240.com/"+command_code+"__bihuachaxun/"
                        try:
                            print(url)
                            print(api.get_word_order_dict(url=url))
                        except Exception as err:
                            print("failed")
                            print(err)
                            #记录错误时间点
                            print(click)
                        else:
                            print("success")
                            click+=1
                            time.sleep(sleep_time)
                        #api.get_word_order_dict(url="https://bihua.51240.com")
                            # driver