# coding=utf-8

from django.conf.urls import url
from apps.tasks.views import SelectTaskView, StartTaskView, start


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/select$', SelectTaskView.as_view(), name='select-task'),
    url(r'^start$', start, name='start-task'),
]