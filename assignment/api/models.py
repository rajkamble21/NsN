from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Artist(models.Model):
    name = models.CharField(max_length=255)
    works = models.ManyToManyField('Work')
    
    def __str__(self):
        return self.name


class Work(models.Model):
    LINK_TYPE_CHOICES = [
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('OT', 'Other'),
    ]
    link = models.CharField(max_length=255)
    link_type = models.CharField(max_length=2, choices=LINK_TYPE_CHOICES)

    def __str__(self):
        return self.link
