#获取控制码
#字母数字集合
import pandas as pd
content=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
         'r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

'''控制码,第一位e，第二位4-9,
第三位a,b,8,9,第四位a-f&&0-9，
第五位a,b,8,9,第六位a---f ,0-9
控制码的三个集合'''
content_1=['4']
content_2=['a','b','8','9']
content_3=['a','b','c','d','e','f','1','2','3','4','5','6','7','8','9','0']

if __name__ == '__main__':
    #command集合
    command_content=[]
    for i1 in content_1:
        for i2 in content_2:
            for i3 in content_3:
                for i4 in content_2:
                    for i5 in content_3:
                        #获取控制码
                        command_code = 'e' + i1 + i2 + i3 + i4 + i5
                        command_content.append(command_code)
    #换成pandas模型
    command_df=pd.DataFrame(command_content)

    print(command_df)

    command_df.to_csv("/home/molamola/桌面/数据集/ecc/ecc-command-2.csv")