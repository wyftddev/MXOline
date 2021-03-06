#encoding=utf-8
from datetime import datetime

from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"城市名称")
    desc = models.CharField(max_length=100, verbose_name=u"机构描述")
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    city = models.ForeignKey(City, verbose_name=u"所在城市")
    name = models.CharField(max_length=50, verbose_name=u"机构名称")
    desc = models.CharField(max_length=100, verbose_name=u"机构描述")
    click_num = models.IntegerField(default=0, verbose_name=u"机构点击数")
    fav_num = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u"机构图")
    address = models.CharField(max_length=150, verbose_name=u"机构地址")
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"机构"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")
    name = models.CharField(max_length=50, verbose_name=u"教师姓名")
    work_year = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    work_position = models.CharField(max_length=50, verbose_name=u"公司职位")
    points = models.CharField(max_length=50, verbose_name=u"教学特点")
    click_num = models.IntegerField(default=0, verbose_name=u"教师点击数")
    fav_num = models.IntegerField(default=0, verbose_name=u"教师收藏人数")
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name




