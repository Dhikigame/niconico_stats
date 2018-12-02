# coding:utf-8
import sqlite3
import analysis.db as db
import analysis.stats as stats
import analysis.graph as graph
import analysis.output as out

if __name__ == "__main__":

    # タグごとの各中央値再生数のインスタンス保存
    median_list = list()

    ## タグ別のリストと動画総数のインスタンス生成 ##
    stats_anime = stats.Statistics()
    stats_anime.view_taglist("アニメ")
    stats_anime.comment_taglist("アニメ")
    stats_anime.mylist_taglist("アニメ")
    median = stats_anime.median()
    median_list.append(median[0])
    db_anime = db.DB()
    num_anime = db_anime.tag_videonum_sql("アニメ")
    # 平均値、中央値、標準偏差
    out.stats("アニメ", stats_anime, num_anime)

    stats_game = stats.Statistics()
    stats_game.view_taglist("ゲーム")
    stats_game.comment_taglist("ゲーム")
    stats_game.mylist_taglist("ゲーム")
    median = stats_game.median()
    median_list.append(median[0])
    db_game = db.DB()
    num_game = db_game.tag_videonum_sql("ゲーム")
    # 平均値、中央値、標準偏差
    out.stats("ゲーム", stats_game, num_game)

    stats_realplay = stats.Statistics()
    stats_realplay.view_taglist("実況プレイ動画")
    stats_realplay.comment_taglist("実況プレイ動画")
    stats_realplay.mylist_taglist("実況プレイ動画")
    median = stats_realplay.median()
    median_list.append(median[0])
    db_realplay = db.DB()
    num_realplay = db_realplay.tag_videonum_sql("実況プレイ動画")
    # 平均値、中央値、標準偏差
    out.stats("実況プレイ動画", stats_realplay, num_realplay)

    stats_touhou = stats.Statistics()
    stats_touhou.view_taglist("東方")
    stats_touhou.comment_taglist("東方")
    stats_touhou.mylist_taglist("東方")
    median = stats_touhou.median()
    median_list.append(median[0])
    db_touhou = db.DB()
    num_touhou = db_touhou.tag_videonum_sql("東方")
    # 平均値、中央値、標準偏差
    out.stats("東方", stats_touhou, num_touhou)

    stats_idolmaster = stats.Statistics()
    stats_idolmaster.view_taglist("アイドルマスター")
    stats_idolmaster.comment_taglist("アイドルマスター")
    stats_idolmaster.mylist_taglist("アイドルマスター")
    median = stats_idolmaster.median()
    median_list.append(median[0])
    db_idolmaster = db.DB()
    num_idolmaster = db_idolmaster.tag_videonum_sql("アイドルマスター")
    # 平均値、中央値、標準偏差
    out.stats("アイドルマスター", stats_idolmaster, num_idolmaster)

    stats_radio = stats.Statistics()
    stats_radio.view_taglist("ラジオ")
    stats_radio.comment_taglist("ラジオ")
    stats_radio.mylist_taglist("ラジオ")
    median = stats_radio.median()
    median_list.append(median[0])
    db_radio = db.DB()
    num_radio = db_radio.tag_videonum_sql("ラジオ")
    # 平均値、中央値、標準偏差
    out.stats("ラジオ", stats_radio, num_radio)

    stats_draw = stats.Statistics()
    stats_draw.view_taglist("描いてみた")
    stats_draw.comment_taglist("描いてみた")
    stats_draw.mylist_taglist("描いてみた")
    median = stats_draw.median()
    median_list.append(median[0])    
    db_draw = db.DB()
    num_draw = db_draw.tag_videonum_sql("描いてみた")
    # 平均値、中央値、標準偏差
    out.stats("描いてみた", stats_draw, num_draw)

    stats_trpg = stats.Statistics()
    stats_trpg.view_taglist("TRPG")
    stats_trpg.comment_taglist("TRPG")
    stats_trpg.mylist_taglist("TRPG")
    median = stats_trpg.median()
    median_list.append(median[0]) 
    db_trpg = db.DB()
    num_trpg = db_trpg.tag_videonum_sql("TRPG")
    # 平均値、中央値、標準偏差
    out.stats("TRPG", stats_trpg, num_trpg)

    stats_entertainment = stats.Statistics()
    stats_entertainment.view_taglist("エンターテイメント")
    stats_entertainment.comment_taglist("エンターテイメント")
    stats_entertainment.mylist_taglist("エンターテイメント")
    median = stats_entertainment.median()
    median_list.append(median[0]) 
    db_entertainment = db.DB()
    num_entertainment = db_entertainment.tag_videonum_sql("エンターテイメント")
    # 平均値、中央値、標準偏差
    out.stats("エンターテイメント", stats_entertainment, num_entertainment)

    stats_music = stats.Statistics()
    stats_music.view_taglist("音楽")
    stats_music.comment_taglist("音楽")
    stats_music.mylist_taglist("音楽")
    median = stats_music.median()
    median_list.append(median[0]) 
    db_music = db.DB()
    num_music = db_music.tag_videonum_sql("音楽")
    # 平均値、中央値、標準偏差
    out.stats("音楽", stats_music, num_music)

    stats_sing = stats.Statistics()
    stats_sing.view_taglist("歌ってみた")
    stats_sing.comment_taglist("歌ってみた")
    stats_sing.mylist_taglist("歌ってみた")
    median = stats_sing.median()
    median_list.append(median[0]) 
    db_sing = db.DB()
    num_sing = db_sing.tag_videonum_sql("歌ってみた")
    # 平均値、中央値、標準偏差
    out.stats("歌ってみた", stats_sing, num_sing)

    stats_play = stats.Statistics()
    stats_play.view_taglist("演奏してみた")
    stats_play.comment_taglist("演奏してみた")
    stats_play.mylist_taglist("演奏してみた")
    median = stats_play.median()
    median_list.append(median[0])     
    db_play = db.DB()
    num_play = db_play.tag_videonum_sql("演奏してみた")
    # 平均値、中央値、標準偏差
    out.stats("演奏してみた", stats_play, num_play)

    stats_dance = stats.Statistics()
    stats_dance.view_taglist("踊ってみた")
    stats_dance.comment_taglist("踊ってみた")
    stats_dance.mylist_taglist("踊ってみた")
    median = stats_dance.median()
    median_list.append(median[0])     
    db_dance = db.DB()
    num_dance = db_dance.tag_videonum_sql("踊ってみた")
    # 平均値、中央値、標準偏差
    out.stats("踊ってみた", stats_dance, num_dance)

    stats_vocaloid = stats.Statistics()
    stats_vocaloid.view_taglist("VOCALOID")
    stats_vocaloid.comment_taglist("VOCALOID")
    stats_vocaloid.mylist_taglist("VOCALOID")
    median = stats_vocaloid.median()
    median_list.append(median[0])     
    db_vocaloid = db.DB()
    num_vocaloid = db_vocaloid.tag_videonum_sql("VOCALOID")
    # 平均値、中央値、標準偏差
    out.stats("VOCALOID", stats_vocaloid, num_vocaloid)

    stats_indies = stats.Statistics()
    stats_indies.view_taglist("ニコニコインディーズ")
    stats_indies.comment_taglist("ニコニコインディーズ")
    stats_indies.mylist_taglist("ニコニコインディーズ")
    median = stats_indies.median()
    median_list.append(median[0])      
    db_indies = db.DB()
    num_indies = db_indies.tag_videonum_sql("ニコニコインディーズ")
    # 平均値、中央値、標準偏差
    out.stats("ニコニコインディーズ", stats_indies, num_indies)

    stats_asmr = stats.Statistics()
    stats_asmr.view_taglist("ASMR")
    stats_asmr.comment_taglist("ASMR")
    stats_asmr.mylist_taglist("ASMR")
    median = stats_asmr.median()
    median_list.append(median[0])    
    db_asmr = db.DB()
    num_asmr = db_asmr.tag_videonum_sql("ASMR")
    # 平均値、中央値、標準偏差
    out.stats("ASMR", stats_asmr, num_asmr)

    stats_mmd = stats.Statistics()
    stats_mmd.view_taglist("MMD")
    stats_mmd.comment_taglist("MMD")
    stats_mmd.mylist_taglist("MMD")
    median = stats_mmd.median()
    median_list.append(median[0])
    db_mmd = db.DB()
    num_mmd = db_mmd.tag_videonum_sql("MMD")
    # 平均値、中央値、標準偏差
    out.stats("MMD", stats_mmd, num_mmd)

    stats_virtual = stats.Statistics()
    stats_virtual.view_taglist("バーチャル")
    stats_virtual.comment_taglist("バーチャル")
    stats_virtual.mylist_taglist("バーチャル")
    median = stats_virtual.median()
    median_list.append(median[0])    
    db_virtual = db.DB()
    num_virtual = db_virtual.tag_videonum_sql("バーチャル")
    # 平均値、中央値、標準偏差
    out.stats("バーチャル", stats_virtual, num_virtual)

    stats_animal = stats.Statistics()
    stats_animal.view_taglist("動物")
    stats_animal.comment_taglist("動物")
    stats_animal.mylist_taglist("動物")
    median = stats_animal.median()
    median_list.append(median[0])      
    db_animal = db.DB()
    num_animal = db_animal.tag_videonum_sql("動物")  
    # 平均値、中央値、標準偏差
    out.stats("動物", stats_animal, num_animal)

    stats_cook = stats.Statistics()
    stats_cook.view_taglist("料理")
    stats_cook.comment_taglist("料理")
    stats_cook.mylist_taglist("料理")
    median = stats_cook.median()
    median_list.append(median[0])    
    db_cook = db.DB()
    num_cook = db_cook.tag_videonum_sql("料理")
    # 平均値、中央値、標準偏差
    out.stats("料理", stats_cook, num_cook)

    stats_nature = stats.Statistics()
    stats_nature.view_taglist("自然")
    stats_nature.comment_taglist("自然")
    stats_nature.mylist_taglist("自然")
    median = stats_nature.median()
    median_list.append(median[0])    
    db_nature = db.DB()
    num_nature = db_nature.tag_videonum_sql("自然")
    # 平均値、中央値、標準偏差
    out.stats("自然", stats_nature, num_nature)

    stats_travel = stats.Statistics()
    stats_travel.view_taglist("旅行")
    stats_travel.comment_taglist("旅行")
    stats_travel.mylist_taglist("旅行")
    median = stats_travel.median()
    median_list.append(median[0])     
    db_travel = db.DB()
    num_travel = db_travel.tag_videonum_sql("旅行")
    # 平均値、中央値、標準偏差
    out.stats("旅行", stats_travel, num_travel)

    stats_sport = stats.Statistics()
    stats_sport.view_taglist("スポーツ")
    stats_sport.comment_taglist("スポーツ")
    stats_sport.mylist_taglist("スポーツ")
    median = stats_sport.median()
    median_list.append(median[0])    
    db_sport = db.DB()
    num_sport = db_sport.tag_videonum_sql("スポーツ")
    # 平均値、中央値、標準偏差
    out.stats("スポーツ", stats_sport, num_sport)

    stats_lecture = stats.Statistics()
    stats_lecture.view_taglist("ニコニコ動画講座")
    stats_lecture.comment_taglist("ニコニコ動画講座")
    stats_lecture.mylist_taglist("ニコニコ動画講座")
    median = stats_lecture.median()
    median_list.append(median[0])     
    db_lecture = db.DB()
    num_lecture = db_lecture.tag_videonum_sql("ニコニコ動画講座")
    # 平均値、中央値、標準偏差
    out.stats("ニコニコ動画講座", stats_lecture, num_lecture)

    stats_vehicle = stats.Statistics()
    stats_vehicle.view_taglist("車載動画")
    stats_vehicle.comment_taglist("車載動画")
    stats_vehicle.mylist_taglist("車載動画")
    median = stats_vehicle.median()
    median_list.append(median[0])     
    db_vehicle = db.DB()
    num_vehicle = db_vehicle.tag_videonum_sql("車載動画")
    # 平均値、中央値、標準偏差
    out.stats("車載動画", stats_vehicle, num_vehicle)

    stats_history = stats.Statistics()
    stats_history.view_taglist("歴史")
    stats_history.comment_taglist("歴史")
    stats_history.mylist_taglist("歴史")
    median = stats_history.median()
    median_list.append(median[0])    
    db_history = db.DB()
    num_history = db_history.tag_videonum_sql("歴史")
    # 平均値、中央値、標準偏差
    out.stats("歴史", stats_history, num_history)

    stats_railway = stats.Statistics()
    stats_railway.view_taglist("鉄道")
    stats_railway.comment_taglist("鉄道")
    stats_railway.mylist_taglist("鉄道")
    median = stats_railway.median()
    median_list.append(median[0])     
    db_railway = db.DB()
    num_railway = db_railway.tag_videonum_sql("鉄道")
    # 平均値、中央値、標準偏差
    out.stats("鉄道", stats_railway, num_railway)

    stats_science = stats.Statistics()
    stats_science.view_taglist("科学")
    stats_science.comment_taglist("科学")
    stats_science.mylist_taglist("科学")
    median = stats_science.median()
    median_list.append(median[0])     
    db_science = db.DB()
    num_science = db_science.tag_videonum_sql("科学")
    # 平均値、中央値、標準偏差
    out.stats("科学", stats_science, num_science)

    stats_technology = stats.Statistics()
    stats_technology.view_taglist("ニコニコ技術部")
    stats_technology.comment_taglist("ニコニコ技術部")
    stats_technology.mylist_taglist("ニコニコ技術部")
    median = stats_technology.median()
    median_list.append(median[0])    
    db_technology = db.DB()
    num_technology = db_technology.tag_videonum_sql("ニコニコ技術部")
    # 平均値、中央値、標準偏差
    out.stats("ニコニコ技術部", stats_technology, num_technology)

    stats_handicraft = stats.Statistics()
    stats_handicraft.view_taglist("ニコニコ手芸部")
    stats_handicraft.comment_taglist("ニコニコ手芸部")
    stats_handicraft.mylist_taglist("ニコニコ手芸部")
    median = stats_handicraft.median()
    median_list.append(median[0])    
    db_handicraft = db.DB()
    num_handicraft = db_handicraft.tag_videonum_sql("ニコニコ手芸部")
    # 平均値、中央値、標準偏差
    out.stats("ニコニコ手芸部", stats_handicraft, num_handicraft)

    stats_create = stats.Statistics()
    stats_create.view_taglist("作ってみた")
    stats_create.comment_taglist("作ってみた")
    stats_create.mylist_taglist("作ってみた")
    median = stats_create.median()
    median_list.append(median[0])    
    db_create = db.DB()
    num_create = db_create.tag_videonum_sql("作ってみた")
    # 平均値、中央値、標準偏差
    out.stats("作ってみた", stats_create, num_create)

    stats_government = stats.Statistics()
    stats_government.view_taglist("政治")
    stats_government.comment_taglist("政治")
    stats_government.mylist_taglist("政治")
    median = stats_government.median()
    median_list.append(median[0])    
    db_government = db.DB()
    num_government = db_government.tag_videonum_sql("政治")
    # 平均値、中央値、標準偏差
    out.stats("政治", stats_government, num_government)

    stats_example = stats.Statistics()
    stats_example.view_taglist("例のアレ")
    stats_example.comment_taglist("例のアレ")
    stats_example.mylist_taglist("例のアレ")
    median = stats_example.median()
    median_list.append(median[0])    
    db_example = db.DB()
    num_example = db_example.tag_videonum_sql("例のアレ")
    # 平均値、中央値、標準偏差
    out.stats("例のアレ", stats_example, num_example)

    stats_other = stats.Statistics()
    stats_other.view_taglist("その他")
    stats_other.comment_taglist("その他")
    stats_other.mylist_taglist("その他")
    median = stats_other.median()
    median_list.append(median[0])    
    db_other = db.DB()
    num_other = db_other.tag_videonum_sql("その他")
    # 平均値、中央値、標準偏差
    out.stats("その他", stats_other, num_other)

    stats_diary = stats.Statistics()
    stats_diary.view_taglist("日記")
    stats_diary.comment_taglist("日記")
    stats_diary.mylist_taglist("日記")
    median = stats_diary.median()
    median_list.append(median[0])
    db_diary = db.DB()
    num_diary = db_diary.tag_videonum_sql("日記")
    # 平均値、中央値、標準偏差
    out.stats("日記", stats_diary, num_diary)

    stats_nocategory = stats.Statistics()
    stats_nocategory.view_taglist("No category")
    stats_nocategory.comment_taglist("No category")
    stats_nocategory.mylist_taglist("No category")
    median = stats_nocategory.median()
    median_list.append(median[0])
    db_nocategory = db.DB()
    num_nocategory = db_diary.tag_videonum_sql("No category")
    # 平均値、中央値、標準偏差
    out.stats("No category", stats_nocategory, num_nocategory)


    ## グラフ出力 ##
    graph_data = graph.Graph()
    graph_data.show_alltag_median(median_list)


    """
    keyword_set = "アニメ OR ゲーム OR 実況プレイ動画 OR 東方 OR アイドルマスター OR ラジオ OR 描いてみた OR TRPG OR\
                エンターテイメント OR 音楽 OR 歌ってみた OR 演奏してみた OR 踊ってみた OR VOCALOID OR ニコニコインディーズ OR ASMR OR MMD OR バーチャル OR\
                動物 OR 料理 OR 自然 OR 旅行 OR スポーツ OR ニコニコ動画講座 OR 車載動画 OR 歴史 OR 鉄道 OR\
                科学 OR ニコニコ技術部 OR ニコニコ手芸部 OR 作ってみた OR\
                政治 OR\
                例のアレ OR その他 OR 日記"
    """