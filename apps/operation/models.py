#encoding=utf-8
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

from users.models import UserProfile
from course.models import Course


class UserAsk(models.Model):
    #用户咨询信息
    name = models.CharField(max_length=20, verbose_name=u"姓名")
    mobile = models.CharField(max_length=11, verbose_name=u"手机号")
    course_name = models.CharField(max_length=50, verbose_name=u"课程名称")
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseComments(models.Model):
    #用户课程评论
    user = models.ForeignKey(UserProfile, verbose_name=u"评价用户")
    course = models.ForeignKey(Course, verbose_name=u"评价课程")
    comment = models.CharField(max_length=200, verbose_name=u"评论")
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程评论"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.comment


class UserFavorite(models.Model):
    #用户收藏
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0, verbose_name=u"数据id")
    fav_type = models.IntegerField(default=0,choices=((1, "课程"),
                                            (2, "机构"),
                                            (3, "讲师")),
                                   verbose_name=u"数据类型")
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    #如果为0，则是发送给所有用户的消息。不为零则是接收消息的用户id
    user = models.IntegerField(default=0, verbose_name=u"接收用户")
    message = models.CharField(max_length=500, verbose_name=u"消息内容")
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    #记录用户的学习课程
    user = models.ForeignKey(UserProfile, verbose_name=u"评价用户")
    course = models.ForeignKey(Course, verbose_name=u"评价课程")
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name
