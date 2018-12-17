# coding:utf-8
import urllib.parse
import video_parse
import random
#import datetime
#from db.db_insert import 
from datetime import datetime, date, timedelta
import pytz
from xml.etree import ElementTree
from db.db_select import new_videoid_select
from db.db_insert import db_regist

"""
現在新しく投稿されている動画IDを取得する(smXXXXXXXX,soXXXXXXXX,nmXXXXXXXX)
@returns {str} - 最新の動画ID
"""
def new_video_search():
        keyword_set = "アニメ OR ゲーム OR 実況プレイ動画 OR 東方 OR アイドルマスター OR ラジオ OR 描いてみた OR TRPG OR\
                    エンターテイメント OR 音楽 OR 歌ってみた OR 演奏してみた OR 踊ってみた OR VOCALOID OR ニコニコインディーズ OR ASMR OR MMD OR バーチャル OR\
                    動物 OR 料理 OR 自然 OR 旅行 OR スポーツ OR ニコニコ動画講座 OR 車載動画 OR 歴史 OR 鉄道 OR\
                    科学 OR ニコニコ技術部 OR ニコニコ手芸部 OR 作ってみた OR\
                    政治 OR\
                    例のアレ OR その他 OR 日記"
        # カテゴリタグから最新の動画をJSON形式で取得
        new_video_url = 'http://api.search.nicovideo.jp/api/v2/video/contents/search?q=' + urllib.parse.quote(keyword_set) + '&targets=tagsExact&fields=contentId&_sort=' + urllib.parse.quote("-") + 'startTime&_limit=100'
        # JSON形式からreadできる形式に変換
        json_video = video_parse.Json_VideoData(new_video_url)
        json_video_data = json_video.video_parse()
        # parseして動画IDを返す
        return json_video_data['data'][0]['contentId']


"""
最新動画IDから動画IDを順序通りに取得する(smXXXXXXXX,soXXXXXXXX,nmXXXXXXXX)
@param {str} videoID 動画ID
"""
def video_search(videoID, new_regist_videoid=0):
    while True:
        # 動画IDの形式(sm,so,nm)を切り取る
        videoID = videoID[2:]
        if new_regist_videoid == 0:
            # 更新した日時が一番新しい動画IDを取得する
            new_regist_videoid = new_videoid_select()
        # new_regist_videoidに動画IDの情報があればそのIDから取得開始、なければ動画ID1から取得開始
        if new_regist_videoid == '':
            for i in range(1, int(videoID)):
                format_rand_videoID = format_video_search(i)

                if format_rand_videoID == "novideo":
                    continue
                else:
                    print ("------------------------------")
                    print(format_rand_videoID + str(i))
                    # 動画ID取得したらDBに登録
                    db_regist(format_rand_videoID + str(i))
            new_regist_videoid = 1
        else:    
            for i in range(int(new_regist_videoid), int(videoID)):
                format_rand_videoID = format_video_search(i)

                if format_rand_videoID == "novideo":
                    continue
                else:
                    print ("------------------------------")
                    print(format_rand_videoID + str(i))
                    # 動画ID取得したらDBに登録
                    db_regist(format_rand_videoID + str(i))
            new_regist_videoid = 1

"""
動画IDから形式を取得する(sm,so,nm)
@param {str} videoID 形式を省いた動画ID
@returns {str} 取得した形式(取得できなかったら消去・非公開にされているため、"novideo"を返す)
"""
def format_video_search(videoID):
    # 形式がsmか判定
    # XML形式からreadできる形式に変換
    xml_video = video_parse.XML_VideoData("http://ext.nicovideo.jp/api/getthumbinfo/sm", str(videoID))
    root = xml_video.video_parse()

    if "sm" in str(root[0][0].text):
        return "sm"
    # 形式がsoか判定
    else:
        # XML形式からreadできる形式に変換
        xml_video = video_parse.XML_VideoData("http://ext.nicovideo.jp/api/getthumbinfo/so", str(videoID))
        root = xml_video.video_parse()

        if "so" in str(root[0][0].text):
            return "so"
        # 形式がnmか判定
        else:
            # XML形式からreadできる形式に変換
            xml_video = video_parse.XML_VideoData("http://ext.nicovideo.jp/api/getthumbinfo/nm", str(videoID))
            root = xml_video.video_parse()

            if "nm" in str(root[0][0].text):
                return "nm"

            else:
                return "novideo"


class Video_Eval:
    def __init__(self, videoID):
        # XML形式からreadできる形式に変換
        xml_video = video_parse.XML_VideoData("http://ext.nicovideo.jp/api/getthumbinfo/", str(videoID))
        xml = xml_video.video_parse()
        #tree = ElementTree.parse(xml)
        #root = xml.getroot()
        #self.root = root
        self.xml = xml

    def date_video(self):
        # XML形式から取得した投稿日付を日付型に変換 (xml[0][4].text: %Y-%m-%dT%H:%M:%S+09:00 -> %Y-%m-%d %H:%M:%S)
        date = self.xml[0][4].text
        date = date[:-6]
        date = date.replace('T', ' ') 
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        return date
    def view_video(self):
        # XML形式から再生数取得する
        view = int(self.xml[0][9].text)
        return view
    def comment_video(self):
        # XML形式から再生数取得する
        comment = int(self.xml[0][10].text)
        return comment
    def mylist_video(self):
        # XML形式から再生数取得する
        mylist = int(self.xml[0][11].text)
        return mylist
    def tag_video(self):
        video_tags = list()
        if self.xml[0][17] is None:
            tmp_tag = "No category"
            video_tags.append(str(tmp_tag))
            return video_tags
        else:
            for i in range(0, len(self.xml[0][17])):
                tmp_tag = self.xml[0][17][i].text
                video_tags.append(str(tmp_tag))
            return video_tags
    def title_video(self):
        return self.xml[0][1].text