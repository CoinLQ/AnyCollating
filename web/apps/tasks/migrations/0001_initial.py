# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import core.adminlte.constants


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0014_auto_20170202_0810'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('percent', models.PositiveIntegerField(default=0, verbose_name='\u8fdb\u5ea6')),
                ('pos', models.PositiveIntegerField(default=0, verbose_name='\u4f4d\u7f6e')),
                ('status', models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38(\u8fdb\u884c\u4e2d)'), (2, '\u5b8c\u6210'), (1, '\u5df2\u5c31\u7eea'), (99, '\u5220\u9664')])),
                ('task_type', models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='\u7c7b\u578b', choices=[(0, '\u6821\u5bf9'), (1, '\u6821\u52d8')])),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name='\u5f00\u59cb\u65f6\u95f4', null=True)),
                ('end_time', models.DateTimeField(null=True, verbose_name='\u7ed3\u675f\u65f6\u95f4', blank=True)),
                ('object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('content_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u4e2a\u4eba\u4efb\u52a1',
                'verbose_name_plural': '\u4e2a\u4eba\u4efb\u52a1',
            },
            bases=(models.Model, core.adminlte.constants.TaskStatus),
        ),
        migrations.CreateModel(
            name='TaskPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('code', models.CharField(default=b'', max_length=20, blank=True, null=True, verbose_name='\u7f16\u7801', db_index=True)),
                ('text_content_trad', models.TextField(default=b'', null=True, verbose_name='\u9875\u6587\u672c\uff08\u7e41\u4f53\uff09', blank=True)),
                ('status', models.PositiveSmallIntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')])),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('page', models.ForeignKey(related_name='content_pages', verbose_name='\u6240\u5c5e\u9875\u9762', to='catalogue.Page', null=True)),
                ('task', models.ForeignKey(related_name='task_pages', verbose_name='\u6240\u5c5e\u4efb\u52a1', to='tasks.Task', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
