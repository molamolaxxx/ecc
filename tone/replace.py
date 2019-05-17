import pandas as pd


'''
注音原理
a
e o
i u标在后
'''
tone_path="/home/molamola/桌面/数据集/ecc/yumu-tone.csv"
raw_data=['ke3 ai4','hen3 dui4','mao1 mi1','zhi3 shi4','feng1 kuang2']
tone=[['ā','á','ǎ','à'],
      ['ō','ó','ǒ','ò'],
      ['ē', 'é', 'ě', 'è'],
      ['ī', 'í', 'ǐ', 'ì'],
      ['ū', 'ú', 'ǔ', 'ù'],
      ['ǖ', 'ǘ', 'ǚ', 'ǜ']]

def get_tone_mark(word,tone_type):
    '''获得标注的拼音'''
    word = word[0:len(word) - 1]
    word_marked=""

    if 'a' in word:
        #先标ａ
        word_marked=word.replace('a',tone[0][tone_type-1])
    elif 'e' in word or 'o' in word:
        word_marked=word.replace('o',tone[1][tone_type-1])
        word_marked=word_marked.replace('e',tone[2][tone_type-1])
    elif 'ui' in word or 'vi' in word or 'i' in word:
        word_marked = word.replace('i', tone[3][tone_type - 1])
    elif 'iu' in word or 'u' in word:
        word_marked = word.replace('u', tone[4][tone_type - 1])
    elif 'iv' in word or 'v' in word:
        word_marked = word.replace('v', tone[5][tone_type - 1])

    print(word_marked)


#读取韵母声调的csv
tone_df=pd.read_csv(tone_path)
#print(tone_df.values)

for data in raw_data:
    tone_list=data.split(' ')
    #print(tone_list)
    for word in tone_list:
        #获取读音数字
        tone_num=word[len(word)-1]
        #通过函数获取带标注的拼音
        get_tone_mark(word,int(tone_num))


