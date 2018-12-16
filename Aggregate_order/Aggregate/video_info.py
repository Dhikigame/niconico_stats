# coding: utf-8
import video_parse

"""
動画IDから動画情報取得し、リストで返す
@param {str} videoID ランダムな動画ID
@returns {list} 動画情報リスト
"""
def video_info(videoID):
    # XML形式からreadできる形式に変換
    xml_video = video_parse.XML_VideoData("http://ext.nicovideo.jp/api/getthumbinfo/", str(videoID))
    root = xml_video.video_parse()
    
    video_info = list()   
    # タイトル
    video_info.append(str(root[0][1].text))
    # 動画ID
    video_info.append(root[0][0].text)

    return video_info