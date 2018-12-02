# coding:utf-8
import sqlite3
import analysis.db as db
import analysis.stats as stats
import analysis.graph as graph

def stats(title, stats_data, num=1):
    print("【" + title + "】")
    # 動画総数
    print("動画総数：" + str(num))
    # 平均値、中央値、標準偏差
    avarage = stats_data.avarage()
    print("avarage:" + "再生数" + str(avarage[0]) + "コメント数" + str(avarage[1]) + "マイリスト数" + str(avarage[2]))
    median = stats_data.median()
    print("median:" + "再生数" + str(median[0]) + "コメント数" + str(median[1]) + "マイリスト数" + str(median[2]))
    std = stats_data.std()
    print("std:" + "再生数" + str(std[0]) + "コメント数" + str(std[1]) + "マイリスト数" + str(std[2]))
