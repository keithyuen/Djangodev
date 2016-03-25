# trips/models.py

from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/1.9/ref/models/fields/

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
	
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title