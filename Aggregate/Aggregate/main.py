# coding:utf-8
import video_search
from db.db_insert import db_insert

if __name__ == "__main__":
    while True:
        # 現在投稿されている動画から、ランダムで評価すべき動画の動画IDを取得
        videoID = video_search.rand_video_search(video_search.new_video_search())
        # 動画ID取得したらDBに登録
        db_insert(videoID)