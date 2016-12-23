# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20161213_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='cellphone',
            field=models.CharField(max_length=11, null=True, verbose_name='\u624b\u673a', blank=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='job_status',
            field=models.IntegerField(default=1, verbose_name='\u72b6\u6001', choices=[(1, '\u6709\u6548'), (2, '\u65e0\u6548')]),
        ),
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.PositiveSmallIntegerField(default=0, null=True, verbose_name='\u804c\u4f4d', blank=True, choices=[(0, '\u4e49\u5de5'), (1, '\u4e49\u5de5\u7ec4\u957f'), (2, '\u7ba1\u7406\u5458'), (3, '\u6cd5\u5e08')]),
        ),
    ]
