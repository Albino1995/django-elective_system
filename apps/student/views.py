#_*_ coding:utf-8 _*_

from django.shortcuts import  render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.backends import ModelBackend
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.core.urlresolvers import reverse
from utils.mixin_utils import LoginRequiredMixin
from django.views.generic.base import View
from django.shortcuts import render_to_response

from .models import UserProfile
from .forms import LoginForm,PwdupdateForm,UserinfoForm

class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(username=username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None
#登录
class LoginView(View):
    def get(self, request):
        return render(request, "login_base.html",{})
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username","")
            pass_word = request.POST.get("password","")
            user = authenticate(username=user_name,password=pass_word)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "login_base.html",{"msg":"用户或者密码错误!"})
        else:
            return render(request, "login_base.html",{"login_form":login_form})
#登出
class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse("login"))
#修改个人信息
class UserinfoView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,"message_base.html",{})
    def post(self,request):
        userinfo_form = UserinfoForm(request.POST)
        if userinfo_form.is_valid():
            phone = request.POST.get("phone","")
            email = request.POST.get("email","")
            user = request.user
            user.phone = phone
            user.email = email
            user.save()
            return HttpResponseRedirect(reverse("success"))
        else:
            return render(request, "message_base.html", {"userinfo_form": userinfo_form})
#修改密码
class PwdupdateView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, "password_base.html",{})
    def post(self,request):
        pswupdate_form = PwdupdateForm(request.POST)
        if pswupdate_form.is_valid():
            pwd1 = request.POST.get("new_password","")
            pwd2 = request.POST.get("check_password","")
            if pwd1 != pwd2:
                return render(request, "password_base.html", {"msg": "密码不一致!"})
            user = request.user
            user.password = make_password(pwd2)
            user.save()
            return HttpResponseRedirect(reverse("success"))
        else:
            return render(request, "password_base.html",{"pswupdate_form":pswupdate_form})
#个人中心修改成功
class SuccessView(View):
    def get(self,request):
        return render(request,"success_base.html",{})
#全局404处理
def page_not_found(request):
    response = render_to_response('404_base.html',{})
    response.status_code = 404
    return response