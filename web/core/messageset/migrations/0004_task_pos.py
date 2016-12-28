# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageset', '0003_auto_20161222_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='pos',
            field=models.PositiveIntegerField(default=0, verbose_name='\u4f4d\u7f6e'),
        ),
    ]
