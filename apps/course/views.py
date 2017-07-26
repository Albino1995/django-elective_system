#_*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Course,Time
from operation.models import Stucourse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from utils.mixin_utils import LoginRequiredMixin


# Create your views here.

#选修课选课
class SelectiveView(LoginRequiredMixin,View):
    def get(self,request):
        all_selective = Course.objects.filter(nature='optional')
        all_time = Time.objects.all()
        #选修课分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_selective, 10, request=request)
        sel = p.page(page)
        return render(request,'selective_base.html',{
            'all_selective':sel,
            'all_time':all_time
        })
    def post(self, request):
        course_id = request.POST.get('course_id',0)
        user_ele = Stucourse()
        user_ele.student = request.user
        user_ele.course = Course.objects.get(course_number=course_id)
        user_ele.save()
        course = Course.objects.get(course_number=course_id)
        course.content -= 1
        course.save()
        return HttpResponseRedirect(reverse("electived"))
#必修课选课
class ProfessionalView(LoginRequiredMixin,View):
    def get(self,request):
        all_professional = Course.objects.filter(nature='compulsory')
        all_time = Time.objects.all()
        #必修课分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_professional, 10, request=request)
        pro = p.page(page)
        return render(request,'professional_base.html',{
            'all_professional':pro,
            'all_time':all_time
        })
    def post(self, request):
        course_id = request.POST.get('course_id',0)
        user_ele = Stucourse()
        user_ele.student = request.user
        user_ele.course = Course.objects.get(course_number=course_id)
        user_ele.save()
        course = Course.objects.get(course_number=course_id)
        course.content -= 1
        course.save()
        return HttpResponseRedirect(reverse("electived"))
#已选课程和退选
class ElectivedViews(LoginRequiredMixin,View):
    def get(self,request):
        all_ele = Stucourse.objects.filter(student=request.user)
        return render(request,'electived_base.html',{
            'all_ele':all_ele
        })
    def post(self,request):
        course_id = request.POST.get('course_id', 0)
        record = Stucourse.objects.filter(student=request.user,course=(Course.objects.get(course_number=course_id)))
        record.delete()
        course = Course.objects.get(course_number=course_id)
        course.content += 1
        course.save()
        return HttpResponseRedirect(reverse("index"))
#查看课程表
class TimetableView(LoginRequiredMixin,View):
    def get(self,request):
        all_course = Stucourse.objects.filter(student=request.user)
        all_time = []
        for a in all_course:
            all_time += Time.objects.filter(course=a.course)
        return render(request, 'timetable_base.html', {
            'all_time':all_time
        })
            # print a.course
        # all_time = Time.objects.filter()
