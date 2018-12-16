# coding:utf-8
import sqlite3
from contextlib import closing
"""
DBから最新の情報に更新した日時が一番新しい動画IDを取得する
@returns {str} 更新した日時が一番新しい動画ID
"""
def new_videoid_select():
    db = sqlite3.connect('./db/videodata.db')

    with closing(db) as con:
        c = con.cursor()
        cursor = db.cursor()
        sql = "select video_id from video_data ORDER BY regist_date DESC"
        cursor.execute(sql)
        print(str(cursor.fetchone())[2:-3])
        video_id = str(cursor.fetchone())[4:-3]
        con.commit()
        return video_id