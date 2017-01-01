# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageset', '0006_taskpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='current_page_code',
        ),
        migrations.AlterField(
            model_name='taskpage',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='taskpage',
            name='task',
            field=models.ForeignKey(related_name='task_pages', verbose_name='\u6240\u5c5e\u4efb\u52a1', to='messageset.Task', null=True),
        ),
    ]
