# coding:utf-8
import sqlite3
import analysis.stats as stats
import analysis.db as db
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        pass
    def show(self):
        stats_data = stats.Statistics()
        view_list = stats_data.view_list()
        view_list.sort()
        view_list.reverse()

        plt.title("NICONICO VIEW RANKING")
        plt.xlabel("rank")
        plt.ylabel("view")
        plt.plot(view_list)
        plt.show()

    def show_onehundredthousand(self):
        onehundred_data = db.DB()

        view_list = onehundred_data.viewtotal_videonum_sql(100000, 1)
        view_list.sort()
        view_list.reverse()

        plt.title("NICONICO VIEW RANKING (view <= 100000)")
        plt.xlabel("rank")
        plt.ylabel("view")
        plt.plot(view_list)
        plt.show()

    def show_alltag_median(self, median_list):

        label = ["アニメ", "ゲーム", "実況プレイ動画", "東方", "アイドルマスター", "ラジオ", "描いてみた", "TRPG", "エンターテイメント", "音楽", "歌ってみた", "演奏してみた", "踊ってみた", "VOCALOID", "ニコニコインディーズ", "ASMR", "MMD", "バーチャル", "動物", "料理", "自然", "旅行", "スポーツ", "ニコニコ動画講座", "車載動画", "歴史", "鉄道", "科学", "ニコニコ技術部", "ニコニコ手芸部", "作ってみた", "政治", "例のアレ", "その他", "日記", "カテゴリタグなし"]
        x = list()
        for i in range(len(label)):
            x.append(i + 1)
        #print(median_list)
        #print(x)

        #x_width = 1.0
        #x_loc = np.array(range(len(median_list))) + x_width

        plt.title("NICONICO CATEGORYTAG MEDIAN VIEW")        
        plt.xlabel("category tag")
        plt.ylabel("view")
        plt.bar(x, median_list, width=0.3, tick_label=label, align="center")
        plt.figure(figsize=(2, 6), dpi=40)
        #plt.xticks(x_loc, label) 
        plt.show()
        """
        keyword_set = "アニメ OR ゲーム OR 実況プレイ動画 OR 東方 OR アイドルマスター OR ラジオ OR 描いてみた OR TRPG OR\
                エンターテイメント OR 音楽 OR 歌ってみた OR 演奏してみた OR 踊ってみた OR VOCALOID OR ニコニコインディーズ OR ASMR OR MMD OR バーチャル OR\
                動物 OR 料理 OR 自然 OR 旅行 OR スポーツ OR ニコニコ動画講座 OR 車載動画 OR 歴史 OR 鉄道 OR\
                科学 OR ニコニコ技術部 OR ニコニコ手芸部 OR 作ってみた OR\
                政治 OR\
                例のアレ OR その他 OR 日記"
        """