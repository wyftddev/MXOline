#encoding=utf-8
from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse

import xadmin
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlableSetting(object):
    site_title = u"慕学后台管理平台"
    site_footer = u"慕学在线网"
    menu_style = "accordion"


class UserAskXAdmin(object):
    #显示特定字段
    list_display = ["name", "mobile", "course_name", "add_time"]
    #设置搜索字段
    search_fields = ["name", "mobile", "course_name"]
    #设置过滤器
    list_filter = ["name", "mobile", "course_name", "add_time"]


class CourseCommentsXAdmin(object):
    list_display = ["user", "course", "comment", "add_time"]
    search_fields = ["user", "course", "comment"]
    list_filter = ["user__name", "course__name", "comment", "add_time"]


class UserFavoriteXAdmin(object):
    list_display = ["user", "fav_id", "fav_type", "add_time"]
    search_fields = ["user", "fav_id", "fav_type"]
    list_filter = ["user__name", "fav_id", "fav_type", "add_time"]


class UserMessageXAdmin(object):
    list_display = ["user", "message", "has_read", "add_time"]
    search_fields = ["user", "message", "has_read"]
    list_filter = ["user", "message", "has_read", "add_time"]


class UserCourseXAdmin(object):
    list_display = ["user", "course", "add_time"]
    search_fields = ["user", "course"]
    list_filter = ["user__name", "course__name", "add_time"]



xadmin.site.register(UserAsk, UserAskXAdmin)
xadmin.site.register(CourseComments, CourseCommentsXAdmin)
xadmin.site.register(UserFavorite, UserFavoriteXAdmin)
xadmin.site.register(UserMessage, UserMessageXAdmin)
xadmin.site.register(UserCourse, UserCourseXAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlableSetting)
