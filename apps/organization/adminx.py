#encoding=utf-8
from .models import City, CourseOrg, Teacher

import xadmin


class CityXAdmin(object):
    #显示特定字段
    list_display = ["name", "desc", "add_time"]
    #设置搜索字段
    search_fields = ["name", "desc"]
    #设置过滤器
    list_filter = ["name", "desc", "add_time"]


class CourseOrgXAdmin(object):
    list_display = ["city", "name", "desc","click_num","fav_num","address", "add_time"]
    search_fields = ["city", "name", "desc","click_num","fav_num","address"]
    list_filter = ["city_name", "name", "desc","click_num","fav_num","address", "add_time"]


class TeacherXAdmin(object):
    list_display = ["org", "name", "work_year","work_company","work_position","points","click_num", "add_time"]
    search_fields = ["org", "name", "work_year","work_company","work_position","points","click_num"]
    list_filter = ["org__name", "name", "work_year","work_company","work_position","points","click_num", "add_time"]


xadmin.site.register(CourseOrg, CourseOrgXAdmin)
xadmin.site.register(City, CityXAdmin)
xadmin.site.register(Teacher, TeacherXAdmin)
