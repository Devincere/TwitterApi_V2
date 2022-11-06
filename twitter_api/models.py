from django.db import models

# Create your models here.

class Tweet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    tweet_id = models.CharField(max_length=255, null=True, blank=True)
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.CharField(max_length=280)
    user = models.CharField(max_length=280)
    is_active = models.BooleanField(default=True)
    
    def _str_(self):
        return self.text