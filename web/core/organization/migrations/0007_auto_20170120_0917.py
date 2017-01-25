# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_auto_20161231_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.PositiveSmallIntegerField(default=0, null=True, verbose_name='\u804c\u4f4d', blank=True, choices=[(0, '\u4e49\u5de5'), (1, '\u4e49\u5de5\u7ec4\u957f'), (2, '\u7ba1\u7406\u5458'), (3, '\u90e8\u7ec4\u6cd5\u5e08')]),
        ),
    ]
