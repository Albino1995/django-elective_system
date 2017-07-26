from django.conf.urls import url
from operation.views import MessageView, MessageDetailView

urlpatterns = [
    url(r'^detail/(?P<message_id>\d+)/$', MessageDetailView.as_view(),name="detail"),
    url(r'^$', MessageView.as_view(),name="notice"),
]