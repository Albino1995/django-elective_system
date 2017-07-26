# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class Course(models.Model):
    course_id = models.AutoField(primary_key = True)
    course_number = models.CharField(max_length = 20,verbose_name = "课程编号")
    course_name = models.CharField(max_length = 20,verbose_name = "课程名称")
    nature = models.CharField(max_length = 20,choices = (("compulsory ","必修课"),("optional","选修课")),verbose_name="课程性质")
    credit = models.SmallIntegerField(verbose_name = "学分")
    hour = models.SmallIntegerField(verbose_name = "学时")
    teacher = models.CharField(max_length = 10,verbose_name = "授课教师")
    year = models.SmallIntegerField(verbose_name = "学年")
    term = models.SmallIntegerField(verbose_name = "学期")
    start_week = models.SmallIntegerField(verbose_name = "起始周")
    end_week = models.SmallIntegerField(verbose_name = "结束周")
    content = models.SmallIntegerField(verbose_name = "容量")
    place = models.CharField(max_length=10,verbose_name="上课地点")
    class Meta:
        verbose_name="查看课程"
        verbose_name_plural = verbose_name
        ordering = ['course_number']
    def __unicode__(self):
        return self.course_name


class Time(models.Model):
    course = models.ForeignKey(Course,verbose_name = "课程名称")
    lesson = models.CharField(max_length=4,choices=(("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),("10","10"),("11","11"),("12","12"),("13","13"),("14","14")),verbose_name="节数")
    weekday = models.CharField(max_length=10,choices=(("1","星期一"),("2","星期二"),("3","星期三"),("4","星期四"),("5","星期五"),("6","星期六"),("7","星期日")),verbose_name = "时间")
    class Meta:
        verbose_name="课程时间安排"
        verbose_name_plural = verbose_name
        ordering = ['lesson']
    def __unicode__(self):
        return self.course.course_name