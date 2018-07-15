#encoding=utf-8
from .models import Course, Lesson, Video, CourseResource

import xadmin


class CourseXAdmin(object):
    #显示特定字段
    list_display = ["name", "desc", "detail", "degree", "students", "add_time"]
    #设置搜索字段
    search_fields = ["name", "desc", "detail", "degree", "students"]
    #设置过滤器
    list_filter = ["name", "desc", "detail", "degree", "students", "add_time"]


class LessonXAdmin(object):
    list_display = ["course", "name", "add_time"]
    search_fields = ["course", "name"]
    list_filter = ["course__name", "name", "add_time"]


class VideoXAdmin(object):
    list_display = ["lesson", "name", "add_time"]
    search_fields = ["lesson", "name"]
    list_filter = ["lesson__name", "name", "add_time"]


class CourseResourceXAdmin(object):
    list_display = ["course", "name", "add_time"]
    search_fields = ["course", "name", "add_time"]
    list_filter = ["course__name", "name", "add_time"]



xadmin.site.register(Course, CourseXAdmin)
xadmin.site.register(Lesson, LessonXAdmin)
xadmin.site.register(Video, VideoXAdmin)
xadmin.site.register(CourseResource, CourseResourceXAdmin)
