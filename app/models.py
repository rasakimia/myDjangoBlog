from django.db import models


class Article(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    #     in add thumbnail
    #     add author
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + ' ...'
