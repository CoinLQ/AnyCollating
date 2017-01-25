# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_auto_20161228_0652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volume',
            name='cover',
        ),
        migrations.AlterField(
            model_name='lqsutra',
            name='is_opened',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5f00\u653e\u6821\u5bf9', choices=[(0, '\u5426'), (1, '\u662f')]),
        ),
        migrations.AlterField(
            model_name='reel',
            name='start_page',
            field=models.SmallIntegerField(default=0, verbose_name='\u8d77\u59cb\u9875\u7801'),
        )
    ]
