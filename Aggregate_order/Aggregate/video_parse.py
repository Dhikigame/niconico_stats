# coding:utf-8
import urllib.request
import urllib.parse
import json
import xml.etree.ElementTree as ET

"""
ニコニコ動画のWeb APIから動画情報をパースできる形式に変換
@param {str} url WebAPIのURL
@param {str} videoID 動画ID
@returns {list} - 動画情報をパースしたリスト
"""
class Json_VideoData:
    def __init__(self, url):
        self.url = url
    def video_parse(self):
        # JSON形式からreadしたものを返す
        readopen = urllib.request.urlopen(self.url)
        response = readopen.read()
        json_video_data = json.loads(response)

        return json_video_data

class XML_VideoData(Json_VideoData):
    def __init__(self, url, videoID):
        super().__init__(url)
        self.videoID = videoID
    def video_parse(self):
        # XML形式からreadし、タグ先頭の情報(動画ID,タイトル)を返す
        try:
            req = urllib.request.Request(self.url + self.videoID)
            with urllib.request.urlopen(req) as response:
                XmlData = response.read()
                root = ET.fromstring(XmlData)
            return root
        except RemoteDisconnected:
            print("ERROR：" + self.videoID)
            root = [["novideo"]]
            return root
