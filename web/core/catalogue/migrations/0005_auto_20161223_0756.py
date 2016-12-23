# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_auto_20161221_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='varianttripitaka',
            name='cover',
            field=models.ImageField(upload_to=b'cover', null=True, verbose_name='\u5c01\u9762\u4fe1\u606f', blank=True),
        ),
        migrations.AlterField(
            model_name='varianttripitaka',
            name='volumes_count',
            field=models.SmallIntegerField(default=1, verbose_name='\u603b\u518c\u6570'),
        ),
    ]
