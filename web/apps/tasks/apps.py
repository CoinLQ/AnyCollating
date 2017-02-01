# coding=utf-8
from django.apps import AppConfig

class TaskAppConfig(AppConfig):
    name = "apps.tasks"
    verbose_name = u"任务中心"

    def ready(self):
        import serializers
        pass