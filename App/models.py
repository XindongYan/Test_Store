from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=1000)


class Store(models.Model):
    New_Store = models.CharField(max_length=100)
    Unit = models.IntegerField()
    Images = models.FileField(upload_to='media/')


class Image(models.Model):
    images = models.CharField(max_length=1000)


class Shopping_Cart(models.Model):
    Image = models.FileField(upload_to='Shopping_Cart/')
    Store_Name = models.CharField(max_length=100)
    Unit = models.IntegerField()


class Detailed_list(models.Model):
    UserName = models.CharField(max_length=100)
    Image = models.FileField(upload_to='/Detailed_list')
    Store_Name = models.CharField(max_length=100)
    Unit = models.IntegerField()


def __unicode__(self):
    return self.name


# Create your models here.
