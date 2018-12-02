# coding:utf-8
import statistics
import analysis.db as db

class Statistics:
    def __init__(self):
        self.view = list()
        self.comment = list()
        self.mylist = list()
    def view_list(self):
        db_data = db.DB()
        self.view = db_data.all_viewlist_sql()
        #print(self.view)
        return self.view
    def comment_list(self):
        db_data = db.DB()
        self.comment = db_data.all_commentlist_sql()
        #print(self.comment)
        return self.comment
    def mylist_list(self):
        db_data = db.DB()
        self.mylist = db_data.all_mylistlist_sql()
        #print(self.mylist)
        return self.mylist

    def view_taglist(self, tag):
        db_data = db.DB()
        self.view = db_data.tag_viewlist_sql(tag)
        #print(self.view)
        return self.view
    def comment_taglist(self, tag):
        db_data = db.DB()
        self.comment = db_data.tag_commentlist_sql(tag)
        #print(self.comment)
        return self.comment
    def mylist_taglist(self, tag):
        db_data = db.DB()
        self.mylist = db_data.tag_mylistlist_sql(tag)
        #print(self.mylist)
        return self.mylist

    def num(self):
        db_data = db.DB()
        return db_data.all_videonum_sql()
    def percentage(self, num):
        stats = Statistics()
        return num / stats.num() * 100
    # 平均値
    def avarage(self):
        mean_list = list()
        view_mean = statistics.mean(self.view)
        mean_list.append(int(view_mean))
        comment_mean = statistics.mean(self.comment)
        mean_list.append(int(comment_mean))
        mylist_mean = statistics.mean(self.mylist)
        mean_list.append(int(mylist_mean))
        return mean_list
    # 中央値      
    def median(self):
        median_list = list()
        view_median = statistics.median(self.view)
        median_list.append(int(view_median))
        comment_median = statistics.median(self.comment)
        median_list.append(int(comment_median))
        mylist_median = statistics.median(self.mylist)
        median_list.append(int(mylist_median))
        return median_list
    # 標準偏差
    def std(self):
        std_list = list()
        view_std = statistics.stdev(self.view)
        std_list.append(int(view_std))
        comment_std = statistics.stdev(self.comment)
        std_list.append(int(comment_std))
        mylist_std = statistics.stdev(self.mylist)
        std_list.append(int(mylist_std))
        return std_list