import pymysql
import numpy as np

'''项目的存储模块'''
table_name="bushou"
def connect_mysql():

    db=pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = '314', db = 'ecc')
    return db

def save_one_item(database,item_dict,index):
    item = np.array([item_dict['word'],item_dict['order'],index,item_dict['gifOrder']])
    '''保存一个item'''
    print("存储到mysql")
    # 创建游标
    cursor = database.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "insert into "+table_name+"(Word,wOrder,mindex,gifOrder) values (%s,%s,%s,%s)"
    try:

        cursor.execute(sql,[item[0],item[1],item[2],item[3]])

    except Exception as e:
        print(e)
        print("存储出错")

    database.commit()
    cursor.close()

    print("储存成功")