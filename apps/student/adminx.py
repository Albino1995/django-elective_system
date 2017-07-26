# -*- coding:utf-8 -*-
from student.models import Department,Major
import xadmin
from xadmin import views
# Register your models here.
# class UserProfileAdmin(object):
#     list_display = ['student_number','student_name','department','major','classes']
#     search_fields = ['student_number','student_name','department__department_name','major__major_name','classes']
#     list_filter = ['student_number','student_name','department__department_name','major__major_name','classes']
class DepartmentAdmin(object):
    list_display = ['department_number','department_name']
    search_fields = ['department_number','department_name']
    list_filter = ['department_number','department_name']
    model_icon = 'fa fa-building-o'
class MajorAdmin(object):
    list_display = ['major_number','major_name']
    search_fields = ['major_number','major_name']
    list_filter = ['major_number','major_name']
    model_icon = 'fa fa-book'
class BaseSettings(object):
    # 设置base_site.html的Title
    # 启用主题功能
    enable_themes = True
    # 使用基于bootstrapop其他主题
    use_bootswatch = True
class GlobalSettings(object):
    site_title = '选课系统后台管理'
    # 设置base_site.html的Footer
    site_footer = '2016 elective system'
    # 左侧选项卡是否收缩
    menu_style = 'accordion'

xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Department,DepartmentAdmin)
xadmin.site.register(Major,MajorAdmin)