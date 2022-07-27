
from operator import mod
from django.db import models

# Create your models here.
class LoginPage(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    username.primary_key
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.username
    variable = models.Manager()
    objects = models.Manager()


class BookInfo(models.Model):
    bookname = models.CharField(max_length=20,primary_key=True)
    bookname.primary_key
    bookprice = models.CharField(max_length=20)
    #bookurl = models.URLField(max_length=200)
    def __str__(self):
        return self.bookname
    variable = models.Manager()
    objects = models.Manager()

class BookInfoo(models.Model):
    bookname = models.CharField(max_length=20,primary_key=True)
    bookname.primary_key
    bookprice = models.CharField(max_length=20)
    bookurl = models.URLField(max_length=200)
    def __str__(self):
        return self.bookname
    variable = models.Manager()
    objects = models.Manager()




