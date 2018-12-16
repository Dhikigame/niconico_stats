# coding:utf-8
import sqlite3


con = sqlite3.connect('./videodata.db')
cur = con.cursor()
 
sql = 'create table video_data(video_id varchar(50) primary key, title varchar(200), view integer, comment integer, mylist integer, regist_date text, upload_date text, tag1 varchar(100), tag2 varchar(100), tag3 varchar(100), tag4 varchar(100), tag5 varchar(100), tag6 varchar(100), tag7 varchar(100), tag8 varchar(100), tag9 varchar(100), tag10 varchar(100), tag11 varchar(100))'
cur.execute(sql)
#sql = 'create table videoID_position(new_videoid varchar(50), position_videoid varchar(50))'
#cur.execute(sql)

con.commit()
con.close()