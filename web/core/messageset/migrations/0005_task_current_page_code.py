# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageset', '0004_task_pos'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='current_page_code',
            field=models.CharField(max_length=20, null=True, verbose_name='\u5f53\u524d\u9875\u7f16\u7801', blank=True),
        ),
    ]
