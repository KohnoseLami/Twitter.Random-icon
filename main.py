import random
import tweepy
import time
import glob

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def change_icon():

    while True:

        icons = [r.split("/")[-1] for r in glob.glob("*.jpg")]
        icon = random.choice(icons)
        api.update_profile_image(icon)
        time.sleep(600)

change_icon()
