from django.conf.urls import url
from django.views.generic import TemplateView
from student.views import UserinfoView,PwdupdateView,SuccessView

urlpatterns = [
    url(r'^update_info/$',UserinfoView.as_view(),name="info"),
    url(r'^update_password/$', PwdupdateView.as_view(),name="password"),
    url(r'^success/$', SuccessView.as_view(),name="success"),
]