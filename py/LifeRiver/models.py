# -!- coding:utf-8 -!-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.


class Log(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    def getListTitle(self):
        print self.id
        return str(self.timestamp) + ' ' + self.title

    fullname = property(getListTitle)

    def __unicode__(self):
        return self.fullname


class LogList(admin.ModelAdmin):
    list_display = ('fullname', 'timestamp')


class LRPic(models.Model):
    title = models.CharField('标题', max_length=100, blank=True )
    image = models.ImageField('图片', upload_to='wechat_pic', blank=True )

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reversed('pic_upload:pic_show', args=str(self.id))

