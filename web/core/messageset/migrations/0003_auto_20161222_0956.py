# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('messageset', '0002_auto_20161218_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='start_app',
        ),
        migrations.AddField(
            model_name='task',
            name='content_type',
            field=models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='object_id',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='task_type',
            field=models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='\u7c7b\u578b', choices=[(0, '\u6821\u5bf9'), (1, '\u6821\u52d8')]),
        ),
    ]
