# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20161218_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='lqsutra',
            name='is_opened',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5f00\u653e\u6821\u5bf9'),
        ),
        migrations.AddField(
            model_name='lqsutra',
            name='reels_count',
            field=models.SmallIntegerField(default=1, verbose_name='\u603b\u5377\u6570'),
        ),
        migrations.AlterField(
            model_name='sutra',
            name='reels_count',
            field=models.SmallIntegerField(default=1, verbose_name='\u603b\u5377\u6570'),
        ),
    ]
