import tweepy
import config
import requests
import json
import datetime

auth = tweepy.OAuthHandler(config.CK, config.CS)
auth.set_access_token(config.AT, config.ATS)
api = tweepy.API(auth)

class HelloTweet():

    def GetWeather():
        endpoint = "https://www.jma.go.jp/bosai/forecast/data/overview_forecast/130000.json"
        res = requests.get(endpoint).json()
        head_line_text = res["headlineText"]
        if len(head_line_text) < 100:
            return head_line_text + "(気象庁)"
        else:
            return "文字数の都合により省略"

    def GetDate():
        now = datetime.datetime.now()
        now_text = str(now.month) + "月" + str(now.day) + "日" + str(now.hour) + "時" + str(now.minute) + "分"
        return now_text

tweet_content = "こんにちは！\n現在は{}です。\n\n[気象情報]\n{}".format(HelloTweet.GetDate(),HelloTweet.GetWeather())

api.update_status(tweet_content)