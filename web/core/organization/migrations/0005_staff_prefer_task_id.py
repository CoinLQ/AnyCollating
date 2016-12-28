# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20161223_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='prefer_task_id',
            field=models.IntegerField(default=0, verbose_name='\u9996\u9009\u4efb\u52a1ID'),
        ),
    ]
