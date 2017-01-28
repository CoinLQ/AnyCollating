# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0011_auto_20170125_0823'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lqsutra',
            options={'ordering': ('id',), 'verbose_name': '\u9f99\u6cc9\u7ecf\u76ee', 'verbose_name_plural': '\u9f99\u6cc9\u7ecf\u76ee'},
        ),
        migrations.AlterModelOptions(
            name='tripitaka',
            options={'ordering': ('id',), 'verbose_name': '\u7ecf\u85cf', 'verbose_name_plural': '\u7ecf\u85cf'},
        ),
        migrations.AlterModelOptions(
            name='varianttripitaka',
            options={'ordering': ('id',), 'verbose_name': '\u5b9e\u4f53\u7ecf\u85cf', 'verbose_name_plural': '\u5b9e\u4f53\u7ecf\u85cf'},
        ),
        migrations.AlterModelOptions(
            name='volume',
            options={'ordering': ('id',), 'verbose_name': '\u518c', 'verbose_name_plural': '\u518c'},
        ),
        migrations.AlterField(
            model_name='varianttripitaka',
            name='pub_version',
            field=models.CharField(max_length=32, verbose_name='\u7248\u672c\u6279\u6b21'),
        ),
    ]
