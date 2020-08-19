import random
import tweepy
import time
import glob

consumer_key = "54Xe634pzhdYJs3IDT9HnnJj4"
consumer_secret = "5Q6NIBRg0ZLafOAazEKl5vu5xhURRWnn6RxuYAdJIkqayN1YbR"
access_key = "1094575017679962112-h62W0c2XHQ6cBm44zKZiVwE7kqhpAG"
access_secret = "tFq5I9UjuUMqbVv0ZvI3c6UnyxER2wqkAtAu4ZP01H43f"
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def change_icon():

    while True:

        icons = [r.split('/')[-1] for r in glob.glob('*.jpg')]
        icon = random.choice(icons)
        api.update_profile_image(icon)
        time.sleep(600)

change_icon()
