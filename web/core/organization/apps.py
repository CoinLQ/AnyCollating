# coding=utf-8

from django.apps import AppConfig




class OrganizationAppConfig(AppConfig):
    name = "core.organization"
    verbose_name = u"组织机构"

    def ready(self):
        import serializers
        pass


