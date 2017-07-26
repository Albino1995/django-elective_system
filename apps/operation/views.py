#_*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from utils.mixin_utils import LoginRequiredMixin
from .models import Message, Course
from operation.models import Stucourse

# Create your views here.

#消息发布
class MessageView(LoginRequiredMixin,View):
    def get(self,request):
        #选课通知
        all_mes = Message.objects.all()
        #对选课通知进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_mes, 5, request=request)
        mes = p.page(page)
        return render(request, "notice_base.html", {
            "all_mes":mes
        })

#主页
class IndexView(LoginRequiredMixin,View):
    def get(self,request):
        show_mes = Message.objects.all()
        show_course = Stucourse.objects.filter(student=request.user)
        return render(request, "index_base.html", {
            #主页显示前8条信息
                'show_mes':show_mes[0:8],
                'show_course':show_course[0:8]
            })

#消息详情
class MessageDetailView(LoginRequiredMixin,View):
    def get(self,request,message_id):
        all_mes = Message.objects.get(id=int(message_id))
        return render(request,'details_base.html',{
            'all_mes':all_mes
        })
#成绩查询
class ScoreView(LoginRequiredMixin,View):
    def get(self,request):
        record = Stucourse.objects.filter(student=request.user)
        return render(request,'score_base.html',{
            'record':record
        })