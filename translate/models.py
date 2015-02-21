from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name


class Band(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=128, unique=True)
    def __unicode__(self):
        return self.name


class Song(models.Model):
    band = models.ForeignKey(Band)
    name = models.CharField(max_length=128)
    name_ukr = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    text_ukr = models.TextField()
    text_org = models.TextField()
    is_verified = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class NewSong(models.Model):
    band = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    name_ukr = models.CharField(max_length=128)
    text_ukr = models.TextField()
    text_org = models.TextField()
    user = models.ForeignKey(User)

    def verify_link(self):
        return '<a href="/verify-song?id=%d">Verify song</a>' % self.pk
    verify_link.allow_tags = True



