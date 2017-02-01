# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0012_auto_20170128_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reel',
            name='sutra',
            field=models.ForeignKey(related_name='reels', verbose_name='\u5b9e\u4f53\u7ecf\u672cID', to='catalogue.Sutra'),
        ),
    ]
