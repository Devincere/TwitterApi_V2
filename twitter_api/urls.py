from django.contrib import admin
from django.urls import path
#from contact.views import contact_get, contact_post
from twitter_api.views import tweets_fetch

urlpatterns = [
    #path('list/', contact_get),
    path('twitter/', tweets_fetch),
]
