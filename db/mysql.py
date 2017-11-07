'''
SQLAlchemy-ORM框架库
pymysql-python3.+ mysql连接库
'''
import time

import pymysql

conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='', db='test', charset='utf8')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS promotion_code")
sql_create = """CREATE TABLE promotion_code (
         id  INT AUTO_INCREMENT,
         code  CHAR(20) NOT NULL,
         time CHAR(100),
         PRIMARY KEY ( `id` ))"""
cursor.execute(sql_create)

try:
    for i in range(0, 200):
        cursor.execute('insert into promotion_code(code,time) values("%s", "%s")' %
                       (str(i), time.time()))
    conn.commit()
except Exception as ex:
    conn.rollback()

cursor.close()
conn.close()
