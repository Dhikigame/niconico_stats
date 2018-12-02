# coding:utf-8
import twitter
import key

def tweet(video):
    api = twitter.Api(consumer_key=key.CONSUMER_KEY,
                    consumer_secret=key.CONSUMER_SECRET,
                    access_token_key=key.ACCESS_TOKEN,
                    access_token_secret=key.ACCESS_TOKEN_SECRET
                    )
    title = video[0]
    videoid = video[1]
    tweet_output = title + " nico.ms/" + videoid + " #" + videoid + " #ニコニコ動画"
    print(tweet_output)
    api.PostUpdate(tweet_output)