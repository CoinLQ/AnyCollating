# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageset', '0007_auto_20161231_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='\u72b6\u6001', choices=[(0, '\u6b63\u5e38(\u8fdb\u884c\u4e2d)'), (2, '\u5f02\u5e38'), (1, '\u5b8c\u6210'), (99, '\u5220\u9664')]),
        ),
    ]
