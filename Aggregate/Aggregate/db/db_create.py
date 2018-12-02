# coding:utf-8
import sqlite3


con = sqlite3.connect('./video_eval.db')
cur = con.cursor()
 
sql = 'create table video_eval_data(video_id varchar(50) primary key, title varchar(200), view integer, comment integer, mylist integer, regist_date text, upload_date text, tag varchar(100))'
cur.execute(sql)

con.commit()
con.close()