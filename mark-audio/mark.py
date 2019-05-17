'''
1.多读音同词组
2.多音字识别
'''
import jieba
from pypinyin import pinyin

#自定义词典
def self_dict():
    return
#分词
def split_word(sentence):
    word_list=jieba.cut(sentence,cut_all=False)
    return list(word_list)

def zhuyin(sentence):
    '''for seg in split_word(sentence):
        print(seg)'''

    seg_list = split_word(sentence)
    zhuyin_dict_list = []
    for seg in seg_list:
        # 获取拼音list
        pinyin_list = pinyin(seg)

        sentence_zhuyin = {"word": seg, "zhuyin": pinyin_list}
        zhuyin_dict_list.append(sentence_zhuyin)
    return {"list":zhuyin_dict_list,"sentence":sentence}


