from rest_framework import serializers
from tweet.models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    text = serializers.CharField(required=True, allow_blank=False, max_length=280)
    user = serializers.CharField(required=True, allow_blank=False, max_length=280)
    