# -*- coding:utf-8 -*-
from django.db import models
from datetime import datetime
from student.models import UserProfile
from course.models import Course
# Create your models here.

class Stucourse(models.Model):
    student = models.ForeignKey(UserProfile,verbose_name="学生姓名")
    course = models.ForeignKey(Course,verbose_name="课程名称")
    grade = models.DecimalField(max_digits=4,decimal_places=1,verbose_name="成绩",null=True,blank=True)
    class Meta:
        verbose_name="成绩录入"
        verbose_name_plural = verbose_name
        ordering = ['course']
    def __unicode__(self):
        return unicode(self.student)
class Message(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="发布时间")
    class Meta:
        verbose_name="发布信息"
        verbose_name_plural = verbose_name
        ordering = ['-add_time']
    def __unicode__(self):
        return self.title