# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageset', '0009_auto_20170125_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='task',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='taskpage',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='taskpage',
            name='page',
        ),
        migrations.RemoveField(
            model_name='taskpage',
            name='task',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='TaskPage',
        ),
    ]
