# coding=utf-8

from django.conf.urls import url
from apps.tasks.views import VerifySutraView, start, select, verify_sutra_choice


urlpatterns = [

    url(r'^verify_sutra/(?P<pk>[0-9]+)/choice$', verify_sutra_choice, name='verify-sutra-choice'),
    url(r'^verify_sutra/(?P<pk>[0-9]+)$', VerifySutraView.as_view(), name='verify-sutra'),
    url(r'^start$', start, name='start-task'),
    url(r'^select/(?P<task_id>[0-9]+)$', select, name='select-task'),
]