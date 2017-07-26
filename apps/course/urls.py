from django.conf.urls import url
from django.views.generic import TemplateView
from course.views import SelectiveView,ProfessionalView,ElectivedViews
from . import views

urlpatterns = [
    url(r'^selective/$', SelectiveView.as_view(),name="selective"),
    url(r'^professional/$',ProfessionalView.as_view(),name="professional"),
    url(r'^electived/$', ElectivedViews.as_view(),name="electived"),
]