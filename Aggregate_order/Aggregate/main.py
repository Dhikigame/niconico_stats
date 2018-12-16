# coding:utf-8
import video_search
from db.db_insert import db_regist

if __name__ == "__main__":
    while True:
        # 現在投稿されている動画から、動画IDを古い動画から順に取得
        video_search.video_search(video_search.new_video_search())