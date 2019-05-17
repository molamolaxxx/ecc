import pandas as pd
import requests
from time import sleep

content=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
         'r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
if __name__ == '__main__':

    for i in content:
        command="e4a"+"c9"+i

        # 获得url
        url = "https://bihua.51240.com/" + command + "__bihuachaxun/"
        try:
            res=requests.get(url)
            print(res.content)
        except Exception as err:
            print("failed")
            print(err)
        else:
            print("success:" + str(i))

        sleep(3)
