#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Author(models.Model):
	AuthorID=models.AutoField(primary_key=True)#
	Name=models.CharField(max_length=100)#
	Age=models.IntegerField()#
	Country=models.CharField(max_length=50)#
class Book(models.Model):
	ISBN=models.CharField(max_length=20)#20
	Title=models.CharField(max_length=100)#50
	AuthorID=models.ForeignKey(Author, null=True)#
	Publisher=models.CharField(max_length=100)#
	PublishDate=models.DateField()#
	Price=models.FloatField()#

