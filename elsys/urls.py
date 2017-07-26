"""elsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
# from elsys.settings import STATIC_ROOT
# from django.views.static import serve
import xadmin
from student.views import LoginView,LogoutView
from operation.views import IndexView,ScoreView
from course.views import TimetableView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^elective/',include('course.urls')),
    url(r'^notice/',include('operation.urls')),
    url(r'^usercenter/',include('student.urls')),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^timetable/$', TimetableView.as_view(),name="timetable"),
    url(r'^help/$', TemplateView.as_view(template_name="problemlist_base.html"),name="help"),
    url(r'^score/$', ScoreView.as_view(),name="score"),
    url(r'^$',IndexView.as_view(),name="index"),
    # url(r'^static/(?P<path>.*)$', serve, {"document_root":STATIC_ROOT}),
]

handler404 = 'student.views.page_not_found'