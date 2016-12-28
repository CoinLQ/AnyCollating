# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_auto_20161224_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='code',
            field=models.CharField(null=True, default=b'', max_length=20, blank=True, unique=True, verbose_name='\u7f16\u7801'),
        ),
        migrations.AlterField(
            model_name='reel',
            name='code',
            field=models.CharField(default=b'', unique=True, max_length=16, verbose_name='\u7f16\u7801'),
        ),
    ]
