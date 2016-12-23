# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organization',
            options={'verbose_name': '\u7ec4\u7ec7', 'verbose_name_plural': '\u7ec4\u7ec7'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': '\u4e49\u5de5', 'verbose_name_plural': '\u4e49\u5de5'},
        ),
        migrations.AlterField(
            model_name='department',
            name='organization',
            field=models.ForeignKey(related_name='departments', default=None, blank=True, to='organization.Organization', null=True, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe7\xbb\x84\xe7\xbb\x87'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(unique=True, max_length=200, verbose_name='\u7ec4\u7ec7\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='organization_children', verbose_name='\u4e0a\u7ea7\u7ec4\u7ec7', blank=True, to='organization.Organization', null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(verbose_name='\u6240\u5728\u5c0f\u7ec4', to='organization.Department'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.PositiveSmallIntegerField(default=0, null=True, verbose_name='\u804c\u4f4d', blank=True, choices=[(0, '\u4e49\u5de5'), (1, '\u4e49\u5de5\u7ec4\u957f'), (2, '\u4e49\u5de5\u90e8\u7ec4\u957f'), (3, '\u6cd5\u5e08')]),
        ),
    ]
