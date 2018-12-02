# coding:utf-8
import sqlite3
import analysis.db as db
import analysis.stats as stats
import analysis.graph as graph

if __name__ == "__main__":
    
    stats_data = stats.Statistics()
    stats_data.view_list()
    stats_data.comment_list()
    stats_data.mylist_list()

    ## 動画統計 ##
    db_data = db.DB()
    million = db_data.viewtotal_videonum_sql(1000000)
    print("1000000再生以上：" + str(million) + ", per:" + str(round(stats_data.percentage(million), 2)))
    onehundredthousand = db_data.viewtotal_videonum_sql(100000)
    print("100000再生以上：" + str(onehundredthousand) + ", per:" + str(round(stats_data.percentage(onehundredthousand), 2)))
    tenthousand = db_data.viewtotal_videonum_sql(10000)
    print("10000再生以上：" + str(tenthousand) + ", per:" + str(round(stats_data.percentage(tenthousand), 2)))
    thousand = db_data.viewtotal_videonum_sql(1000)
    print("1000再生以上：" + str(thousand) + ", per:" + str(round(stats_data.percentage(thousand), 2)))
    hundred = db_data.viewtotal_videonum_sql(100)
    print("100再生以上：" + str(hundred) + ", per:" + str(round(stats_data.percentage(hundred), 2)))
    print("動画総数：" + str(stats_data.num()))

    # 平均値、中央値、標準偏差
    avarage = stats_data.avarage()
    print("avarage:" + "再生数" + str(avarage[0]) + "コメント数" + str(avarage[1]) + "マイリスト数" + str(avarage[2]))
    median = stats_data.median()
    print("median:" + "再生数" + str(median[0]) + "コメント数" + str(median[1]) + "マイリスト数" + str(median[2]))
    std = stats_data.std()
    print("std:" + "再生数" + str(std[0]) + "コメント数" + str(std[1]) + "マイリスト数" + str(std[2]))

    ## グラフ出力 ##
    graph_data = graph.Graph()
    graph_data.show()

    graph_data.show_onehundredthousand()

