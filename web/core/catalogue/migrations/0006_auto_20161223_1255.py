# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_auto_20161223_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_num',
            field=models.SmallIntegerField(default=1, verbose_name='\u5e8f\u53f7'),
        ),
        migrations.AlterField(
            model_name='page',
            name='text_content_simpl',
            field=models.TextField(default=b'', null=True, verbose_name='\u9875\u6587\u672c\uff08\u7b80\u4f53\uff09', blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='text_content_trad',
            field=models.TextField(default=b'', null=True, verbose_name='\u9875\u6587\u672c\uff08\u7e41\u4f53\uff09', blank=True),
        ),
        migrations.AlterField(
            model_name='reel',
            name='start_page',
            field=models.SmallIntegerField(default=0, verbose_name='\u8d77\u59cb\u518c\u7801'),
        ),
        migrations.AlterField(
            model_name='reel',
            name='text_content_simpl',
            field=models.TextField(default=b'', null=True, verbose_name='\u5377\u6587\u672c\uff08\u7b80\u4f53\uff09', blank=True),
        ),
        migrations.AlterField(
            model_name='reel',
            name='text_content_trad',
            field=models.TextField(default=b'', null=True, verbose_name='\u5377\u6587\u672c\uff08\u7e41\u4f53\uff09', blank=True),
        ),
        migrations.AlterField(
            model_name='sutra',
            name='discription',
            field=models.CharField(default=b'', max_length=512, null=True, verbose_name='\u63cf\u8ff0\u4fe1\u606f', blank=True),
        ),
        migrations.AlterField(
            model_name='sutra',
            name='normal_sutra',
            field=models.ForeignKey(verbose_name='\u9f99\u6cc9\u7ecf\u76ee', to='catalogue.LQSutra'),
        ),
        migrations.AlterField(
            model_name='sutra',
            name='start_page',
            field=models.SmallIntegerField(default=0, verbose_name='\u8d77\u59cb\u9875\u7801'),
        ),
        migrations.AlterField(
            model_name='volume',
            name='code',
            field=models.CharField(default=b'', max_length=12, verbose_name='\u7f16\u7801'),
        ),
        migrations.AlterField(
            model_name='volume',
            name='cover',
            field=models.ImageField(upload_to=b'cover', null=True, verbose_name='\u5c01\u9762\u4fe1\u606f', blank=True),
        ),
        migrations.AlterField(
            model_name='volume',
            name='end_page',
            field=models.SmallIntegerField(default=1, verbose_name='\u7ec8\u6b62\u9875\u7801'),
        ),
    ]
