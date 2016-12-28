# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_auto_20161223_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lqsutra',
            name='is_opened',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5f00\u653e\u6821\u5bf9', choices=[(True, '\u662f'), (False, '\u5426')]),
        ),
        migrations.AlterField(
            model_name='sutra',
            name='normal_sutra',
            field=models.ForeignKey(related_name='sutras', verbose_name='\u9f99\u6cc9\u7ecf\u76ee', to='catalogue.LQSutra'),
        ),
        migrations.AlterField(
            model_name='varianttripitaka',
            name='is_electronic',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u4e3a\u7535\u5b50\u7248', choices=[(True, '\u662f'), (False, '\u5426')]),
        ),
    ]
