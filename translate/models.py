from django.db import models


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
    name_org = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    text_ukr = models.TextField()
    text_org = models.TextField()

    def __unicode__(self):
        return self.name


