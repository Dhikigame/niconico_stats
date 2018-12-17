# coding:utf-8
from datetime import datetime, date, timedelta
import sys
sys.path.append('..')
import video_search  as vs
import sqlite3
from contextlib import closing


def db_regist(videoID):
    video_info_get = vs.Video_Eval(videoID)
    # タグを取得(list)
    video_tags = video_info_get.tag_video()
    #print(video_tags)

    # 投稿日時を取得
    video_date = video_info_get.date_video()
    # タイトルを取得
    video_title = video_info_get.title_video()
    # タイトル任意文字エスケープ
    video_title = video_title.replace("'", "")
    video_title = video_title.replace('"', '')

    # 再生数取得
    video_view = video_info_get.view_video()
    # コメント数取得
    video_comment = video_info_get.comment_video()
    # マイリスト数取得
    video_mylist = video_info_get.mylist_video()


    db = sqlite3.connect('./db/videodata.db')

    with closing(db) as con:
        c = con.cursor()
        cursor = db.cursor()

        # DBに同じ動画IDがあるかFetchする
        sql = 'select video_id from video_data where video_id == "' +  videoID + '"'
        cursor.execute("select video_id from video_data where video_id = ?", (videoID,))
        exist = cursor.fetchone()
        # DBに同じ動画IDがなければ挿入する
        if exist is None:
            sql = 'insert into video_data(video_id, title, view, comment, mylist, regist_date, upload_date'
            for i in range(0, len(video_tags)):
                sql += ', tag' + str(i+1) + ''
            sql += ') values ("' + str(videoID) + '","' + str(video_title) + '",' + str(video_view) + ',' + str(video_comment) + ',' + str(video_mylist) + ',"' + str(datetime.today()) + '","' + str(video_date) + '"' 
            for i in range(0, len(video_tags)):
                video_tags[i] = video_tags[i].replace("'", "")
                video_tags[i] = video_tags[i].replace('"', '')
                sql += ', "' + str(video_tags[i]) + '"'
            sql += ')' 
            print(sql)
            cursor.execute(sql)
            con.commit()
            print("insert:{0}".format(videoID))
        # DBに同じ動画IDがあれば最新の情報に更新する
        else:
            sql = 'update video_data set title="' + str(video_title) + '", view=' + str(video_view) + ", comment=" + str(video_comment) + ", mylist=" + str(video_mylist) + ", regist_date='" + str(datetime.today()) + "', upload_date='" + str(video_date) + "'" #, tag1=?, tag2=?, tag3=?, tag4=?, tag5=?, tag6=?, tag7=?, tag8=?, tag9=?, tag10=?, tag11=? where video_id = ' + videoID + "'"
            for i in range(0, len(video_tags)):
                video_tags[i] = video_tags[i].replace("'", "")
                video_tags[i] = video_tags[i].replace('"', '')
                sql += ", tag" + str(i+1) + '= "' + str(video_tags[i]) + '"'
            sql += " where video_id = '" + videoID + "'"
            print(sql)
            cursor.execute(sql)
            con.commit()
            print("update:{0}".format(videoID))

"""
def position_videoid_regist(videoID):
    db = sqlite3.connect('./db/videodata.db')

    with closing(db) as con:
        c = con.cursor()
        cursor = db.cursor()
        sql = "update videoID_position set position_videoid='" + str(videoID) + "'"
        cursor.execute(sql)
        con.commit()
"""