# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': '\u9875\u4fe1\u606f', 'verbose_name_plural': '\u9875\u4fe1\u606f'},
        ),
        migrations.AlterModelOptions(
            name='reel',
            options={'verbose_name': '\u5377\u4fe1\u606f', 'verbose_name_plural': '\u5377\u4fe1\u606f'},
        ),
        migrations.AlterField(
            model_name='page',
            name='code',
            field=models.CharField(null=True, default=b'', max_length=16, blank=True, unique=True, verbose_name='\u7f16\u7801'),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_num',
            field=models.SmallIntegerField(default=1, verbose_name='\u603b\u5e8f\u53f7'),
        ),
        migrations.AlterField(
            model_name='page',
            name='reel',
            field=models.ForeignKey(related_name='pages', verbose_name='\u6240\u5c5e\u5377', to='catalogue.Reel', null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='text_content_simpl',
            field=models.TextField(default=b'', verbose_name='\u9875\u6587\u672c\uff08\u7b80\u4f53\uff09'),
        ),
        migrations.AlterField(
            model_name='page',
            name='text_content_trad',
            field=models.TextField(default=b'', verbose_name='\u9875\u6587\u672c\uff08\u7e41\u4f53\uff09'),
        ),
        migrations.AlterField(
            model_name='page',
            name='volume',
            field=models.ForeignKey(related_name='pages', verbose_name='\u6240\u5c5e\u518c', to='catalogue.Volume', null=True),
        ),
        migrations.AlterField(
            model_name='sutra',
            name='author',
            field=models.CharField(default=b'', max_length=32, null=True, verbose_name='\u4f5c\u8005', blank=True),
        ),
        migrations.AlterField(
            model_name='sutra',
            name='translator',
            field=models.CharField(default=b'', max_length=32, null=True, verbose_name='\u8bd1\u8005', blank=True),
        ),
    ]
