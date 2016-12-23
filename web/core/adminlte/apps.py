# coding=utf-8
from django.apps import AppConfig




class AdminLteAppConfig(AppConfig):
    name = "core.adminlte"
    verbose_name = u"系统管理"

    def ready(self):
        import serializers
        import core.catalogue.serializers
        pass
