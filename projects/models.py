from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/projects')
    alttxt = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    technologies = models.CharField(max_length=200)

    def __str__(self):
        return self.title
