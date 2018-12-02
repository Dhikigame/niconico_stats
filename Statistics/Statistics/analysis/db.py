# coding:utf-8
import sqlite3
#import stats

class DB:
    def __init__(self):
        self.db = sqlite3.connect('./analysis/video_eval.db')
        self.cur = self.db.cursor()
    # DBにある動画の数を取得
    def all_videonum_sql(self):
        sql = 'select * from video_eval_data'
        result = self.db.execute(sql)
        return len(result.fetchall())
    # 全ての動画の各項目を取得
    def all_viewlist_sql(self):
        self.cur.execute("""select view from video_eval_data;""")
        view_list = list()
        for view in self.cur.fetchall():
            view = str(view)[1:-2]
            view_list.append(int(view))
        return view_list
    def all_commentlist_sql(self):
        self.cur.execute("""select comment from video_eval_data;""")
        comment_list = list()
        for comment in self.cur.fetchall():
            comment = str(comment)[1:-2]
            comment_list.append(int(comment))
        return comment_list
    def all_mylistlist_sql(self):
        self.cur.execute("""select mylist from video_eval_data;""")
        mylist_list = list()
        for mylist in self.cur.fetchall():
            mylist = str(mylist)[1:-2]
            mylist_list.append(int(mylist))
        return mylist_list
    # カテゴリタグに関連した動画の各項目を取得
    def tag_viewlist_sql(self, tag):
        self.cur.execute("""select view from video_eval_data where tag == '{0}';""".format(tag))
        view_list = list()
        for view in self.cur.fetchall():
            view = str(view)[1:-2]
            view_list.append(int(view))
        return view_list
    def tag_commentlist_sql(self, tag):
        self.cur.execute("""select comment from video_eval_data where tag == '{0}';""".format(tag))
        comment_list = list()
        for comment in self.cur.fetchall():
            comment = str(comment)[1:-2]
            comment_list.append(int(comment))
        return comment_list
    def tag_mylistlist_sql(self, tag):
        self.cur.execute("""select mylist from video_eval_data where tag == '{0}';""".format(tag))
        mylist_list = list()
        for mylist in self.cur.fetchall():
            mylist = str(mylist)[1:-2]
            mylist_list.append(int(mylist))
        return mylist_list
    # 再生回数が指定数の動画を取得
    def viewtotal_videonum_sql(self, view_std, lendth=0):
        if lendth == 0:
            sql = 'select * from video_eval_data where view >= "' +  str(view_std) + '"'
            result = self.db.execute(sql)
            return len(result.fetchall())
        else:
            sql = 'select view from video_eval_data where view <= "' +  str(view_std) + '"'
            self.cur.execute(sql)
            view_list = list()
            for view in self.cur.fetchall():
                view = str(view)[1:-2]
                view_list.append(int(view))
            return view_list
    # カテゴリタグの動画数を取得
    def tag_videonum_sql(self,tag):
        sql = 'select * from video_eval_data where tag == "' + str(tag) + '"'
        result = self.db.execute(sql)
        return len(result.fetchall())
    # 再生回数のトップ10取得
    def all_viewtop_sql(self):
        self.cur.execute("""select video_id from video_eval_data order by view desc;""")
        view_list = list()
        count = 0
        for video_id in self.cur.fetchall():
            video_id = str(video_id)[1:-2]
            print(video_id)
            count += 1
            if count > 10:
                break
        #return view_list

