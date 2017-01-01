# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_staff_prefer_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='avatar',
            field=models.ImageField(default=b'adminlte/user_avatar/xianer02.jpg', null=True, upload_to=b'adminlte/user_avatar', blank=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(default=1, verbose_name='\u6240\u5728\u5c0f\u7ec4', to='organization.Department'),
        ),
    ]
