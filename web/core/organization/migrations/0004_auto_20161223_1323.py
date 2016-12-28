# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20161218_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='user',
            field=annoying.fields.AutoOneToOneField(related_name='staff_of', verbose_name='\u767b\u5f55\u8d26\u53f7', to=settings.AUTH_USER_MODEL),
        ),
    ]
