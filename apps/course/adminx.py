# -*- coding:utf-8 -*-
from course.models import Course,Time

import xadmin
# Register your models here.

class CourseAdmin(object):
    list_display = ['course_number','course_name','nature','credit','hour','teacher','place']
    search_fields = ['course_number','course_name','nature','credit','hour','teacher','place']
    list_filter = ['course_number','course_name','nature','credit','hour','teacher','place']
    model_icon = 'fa fa-bookmark'
class TimeAdmin(object):
    list_display = ['course','lesson','weekday']
    search_fields = ['course__course_name','lesson','weekday']
    list_filter = ['course__course_name','lesson','weekday']
    model_icon = 'fa fa-clock-o'

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Time,TimeAdmin)