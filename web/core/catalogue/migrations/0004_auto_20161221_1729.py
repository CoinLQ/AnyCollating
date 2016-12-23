# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20161221_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lqsutra',
            name='name',
            field=models.CharField(default=b'', max_length=128, verbose_name='\u540d\u79f0'),
        ),
    ]
