#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django.http import HttpResponse
from core.adminlte.models import Permission, Menu




class ApiPermissionCheck(object):
    def process_request(self, request):
        return None
        # TODO:
        # if not request.user.is_superuser and \
        #         request.path_info.startswith('/api/'):
        #     # todo: cache
        #     permissions = Permission.objects.filter(
        #         group__in=request.user.groups.all()
        #     )
        #     resources = []
        #     for p in permissions:
        #         resources.extend(p.resources.values_list('url', flat=True))
        #     print(request.path_info)
        #     if request.path_info not in resources:
        #         return HttpResponse(status=403)
        # pass


class MenuMiddleware(object):
    def process_template_response(self, request, response):
        # todo: cache
        if request.path_info.startswith('/management/') or request.path_info == '/management/':
            if request.user.is_superuser:
                page_menus = Menu.objects.filter(status=Menu.USABLE)
            else:
                groups = request.user.groups.all()
                permission = Permission.objects.filter(
                    group__in=groups
                ).first()
                page_menus = permission.menus.all()
            response.context_data['page_menus'] = page_menus
        return response