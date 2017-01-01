# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogue', '0008_auto_20161228_0652'),
        ('messageset', '0005_task_current_page_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('code', models.CharField(default=b'', max_length=20, blank=True, null=True, verbose_name='\u7f16\u7801', db_index=True)),
                ('text_content_trad', models.TextField(default=b'', null=True, verbose_name='\u9875\u6587\u672c\uff08\u7e41\u4f53\uff09', blank=True)),
                ('status', models.PositiveSmallIntegerField(default=1, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')])),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('page', models.ForeignKey(related_name='content_pages', verbose_name='\u6240\u5c5e\u9875\u9762', to='catalogue.Page', null=True)),
                ('task', models.ForeignKey(related_name='page_tasks', verbose_name='\u6240\u5c5e\u4efb\u52a1', to='messageset.Task', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
