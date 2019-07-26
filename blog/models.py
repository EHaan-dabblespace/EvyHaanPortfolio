from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/blog')
    alttxt = models.CharField(max_length=100)
    headline = models.CharField(max_length=250)
    body = models.CharField(max_length=2000)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Blog: {self.title}>"
