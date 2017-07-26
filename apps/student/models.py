# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html
# Create your models here.


class Department(models.Model):
    department_id = models.AutoField(primary_key = True)
    department_number = models.CharField(max_length = 20,verbose_name = "学院编号")
    department_name = models.CharField(max_length = 20,verbose_name = "学院名称")
    class Meta:
        verbose_name = "学院"
        verbose_name_plural = verbose_name
        ordering = ['department_number']
    def __unicode__(self):
        return self.department_name
class Major(models.Model):
    major_id = models.AutoField(primary_key = True)
    major_number = models.CharField(max_length = 20,verbose_name = "专业编号")
    major_name = models.CharField(max_length = 20,verbose_name = "专业名称")
    class Meta:
        verbose_name = "专业"
        verbose_name_plural = verbose_name
        ordering = ['major_number']
    def __unicode__(self):
        return self.major_name
class UserProfile(AbstractUser):
    student_number = models.CharField(max_length = 20,verbose_name = "学号",null=True,blank=True)
    student_name = models.CharField(max_length = 20,verbose_name = "学生姓名",null=True,blank=True)
    phone = models.CharField(max_length=20,blank = True,null = True,verbose_name = "电话")
    department = models.ForeignKey(Department,verbose_name = "学院名称",default="",null=True,blank=True)
    major = models.ForeignKey(Major,verbose_name = "专业名称",default="",null=True,blank=True)
    classes = models.CharField(max_length = 20, verbose_name = "班级",null=True,blank=True)
    class Meta:
        verbose_name = "学生"
        verbose_name_plural = verbose_name
        ordering = ['student_number']
    def __unicode__(self):
        return unicode(self.student_name)

