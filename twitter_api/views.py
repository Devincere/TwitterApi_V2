from django.shortcuts import render
from django.conf import settings
from requests import Response
from .models import Tweet
import tweepy
from tweepy.auth import OAuthHandler
from django.template import Context
from django.template.loader import get_template


def my_tweets():
    auth = OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    my_tweets = api.user_timeline()
    return my_tweets

def save_to_db():
    original_tweets = my_tweets()
    screen_name = "Devincere"
    # for original_tweet in original_tweets:
    #         if not Tweet.objects.filter(tweet_id=original_tweet.id):
    #             new_tweet = Tweet(tweet_id=original_tweet.id, user=screen_name, text=original_tweet.text, published_date=original_tweet.created_at, is_active=True)
    #             new_tweet.save()
    for original_tweet in original_tweets:
      if not Tweet.objects.filter(tweet_id=original_tweet.id):
        new_tweet = Tweet(tweet_id=original_tweet.id, user=screen_name, text=original_tweet.text, published_date=original_tweet.created_at, is_active=True)
        new_tweet.save()

def tweet_list(request):
    template = get_template('index.html')
    tweets = Tweet.objects.order_by('-published_date')
    return render(request, 'index.html', {'tweets': tweets})

def tweets_fetch(request):
    save_to_db()
    return tweet_list(request)