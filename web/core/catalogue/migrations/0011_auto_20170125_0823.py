# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0010_auto_20170120_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='status',
            field=models.SmallIntegerField(default=1, verbose_name='\u6821\u5bf9\u72b6\u6001', choices=[(0, '\u672a\u51c6\u5907\u597d'), (1, '\u5f85\u6821\u5bf9'), (3, '\u5b8c\u6210\u6821\u5bf9'), (99, '\u5df2\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='reel',
            name='status',
            field=models.SmallIntegerField(default=1, verbose_name='\u6821\u5bf9\u72b6\u6001', choices=[(0, '\u672a\u51c6\u5907\u597d'), (1, '\u5f85\u6821\u5bf9'), (3, '\u5b8c\u6210\u6821\u5bf9'), (99, '\u5df2\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='sutra',
            name='status',
            field=models.SmallIntegerField(default=0, verbose_name='\u6821\u5bf9\u72b6\u6001', choices=[(0, '\u672a\u51c6\u5907\u597d'), (1, '\u5f85\u6821\u5bf9'), (3, '\u5b8c\u6210\u6821\u5bf9'), (99, '\u5df2\u5220\u9664')]),
        ),
    ]
