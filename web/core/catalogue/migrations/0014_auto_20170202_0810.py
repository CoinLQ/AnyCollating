# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0013_auto_20170201_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='lqsutra',
            name='can_collated',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u53ef\u6821\u582a', choices=[(False, '\u5426'), (True, '\u662f')]),
        ),
        migrations.AlterField(
            model_name='lqsutra',
            name='is_opened',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u53ef\u6821\u5bf9', choices=[(False, '\u5426'), (True, '\u662f')]),
        ),
    ]
