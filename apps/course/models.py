#encoding=utf-8
from datetime import datetime

from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"课程名称")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = models.TextField(verbose_name="课程详情")
    degree = models.CharField(choices=(("cj", u"初级"), ("zj", u"中级"), ("gj", u"高级")),
                              verbose_name=u"课程等级", max_length=20)
    learn_time = models.IntegerField(default=0, verbose_name=u"学习时长")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_num = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name=u"封面图")
    click_num = models.IntegerField(default=0, verbose_name=u"点击量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"对应课程")
    name = models.CharField(max_length=20, verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"对应章节")
    name = models.CharField(max_length=20, verbose_name=u"视频名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"对应课程")
    name = models.CharField(max_length=20, verbose_name=u"章节名")
    download = models.FileField(upload_to="course/resource/%Y/%m",
                                max_length=20, verbose_name=u"资源文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程视频资源"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
