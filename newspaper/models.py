from django.db import models

from accounts.models import Redactor


class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(Redactor, related_name="newspapers")

    def __str__(self):
        return self.title
