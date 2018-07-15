#encoding=utf-8
from models import EmailVertifyRecord,Banner

import xadmin


class EmailVertifyRecordXAdmin(object):
    #显示特定字段
    list_display = ["code", "email", "send_type", "send_time"]
    #设置搜索字段
    search_fields = ["code", "email", "send_type"]
    #设置过滤器
    list_filter = ["code", "email", "send_type", "send_time"]


class BannerXAdmin(object):
    list_display = ["title", "url", "index", "add_time"]
    search_fields = ["title", "url", "index"]
    list_filter = ["title", "url", "index", "add_time"]



xadmin.site.register(EmailVertifyRecord, EmailVertifyRecordXAdmin)
xadmin.site.register(Banner, BannerXAdmin)
