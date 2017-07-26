# -*- coding:utf-8 -*-
from .models import Stucourse,Message

import xadmin
# Register your models here.
class StucourseAdmin(object):
    list_display = ['course','student','grade']
    search_fields = ['course__course_name','student__student_name','grade']
    list_filter = ['course__course_name','student__student_name','grade']
    list_editable = ['grade']
    model_icon = 'fa fa-bar-chart-o'

class MessageAdmin(object):
    list_display = ['title','add_time']
    search_fields = ['title','add_time']
    list_filter = ['title','add_time']
    model_icon = 'fa fa-comment-o'

xadmin.site.register(Stucourse,StucourseAdmin)
xadmin.site.register(Message,MessageAdmin)