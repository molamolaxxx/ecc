import pymysql
import numpy as np

'''项目的存储模块'''
table_name="word2phrase"
def connect_mysql():

    db=pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = '314', db = 'ecc')
    return db

def save_one_item(database,item_dict):
    item = np.array([item_dict['id'],item_dict['word'],item_dict['sim'],item_dict['trad']])
    '''保存一个item'''
    print("存储到mysql")
    # 创建游标
    cursor = database.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "insert into "+table_name+"(m_index,keyword,sim,trad) values (%s,%s,%s,%s)"
    try:

        cursor.execute(sql,[item[0],item[1],item[2],item[3]])

    except Exception as e:
        print(e)
        print("存储出错")

    database.commit()
    cursor.close()

    print("储存成功")

def save_phrase(database,phrase,table_name):
    # 创建游标
    cursor = database.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "insert into " + table_name + "(phrase) values (%s)"
    try:

        cursor.execute(sql, [phrase])

    except Exception as e:
        print(e)
        print("存储出错")

    database.commit()
    cursor.close()

    print("储存成功")

def save_phrase_info(database,item_dict):
    item = np.array([item_dict['sim'], item_dict['tone'], item_dict['eng'], item_dict['trad']])
    '''保存词组的具体信息'''
    # 创建游标
    cursor = database.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "insert into phraseinfo (phrase,tone,eng,trad) values (%s,%s,%s,%s)"
    try:

        cursor.execute(sql, [item[0],item[1],item[2],item[3]])

    except Exception as e:
        print(e)
        print("存储出错")

    database.commit()
    cursor.close()

    print("储存成功")

def save_sentence_info(database, item_dict):
    item = np.array([item_dict['sentence'], item_dict['English']])
    '''保存句子的具体信息'''
    # 创建游标
    cursor = database.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "insert into sentenceinfo (sentence,eng) values (%s,%s)"
    try:

        cursor.execute(sql, [item[0], item[1]])

    except Exception as e:
        print(e)
        print("存储出错")

    database.commit()
    cursor.close()

    print("储存成功")