# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LQSutra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(default=b'', max_length=6, verbose_name='\u7f16\u7801')),
                ('name', models.CharField(default=b'', unique=True, max_length=128, verbose_name='\u540d\u79f0')),
                ('translator', models.CharField(default=b'', max_length=32, verbose_name='\u8bd1\u8005')),
            ],
            options={
                'verbose_name': '\u9f99\u6cc9\u7ecf\u76ee',
                'verbose_name_plural': '\u9f99\u6cc9\u7ecf\u76ee',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(default=b'', unique=True, max_length=16, verbose_name='\u7f16\u7801')),
                ('page_num', models.SmallIntegerField(default=1, verbose_name='\u603b\u9875\u6570')),
                ('text_content_trad', models.TextField(default=b'', verbose_name='\u5377\u6587\u672c\uff08\u7e41\u4f53\uff09')),
                ('text_content_simpl', models.TextField(default=b'', verbose_name='\u5377\u6587\u672c\uff08\u7b80\u4f53\uff09')),
            ],
        ),
        migrations.CreateModel(
            name='Reel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reel_num', models.SmallIntegerField(default=1, verbose_name='\u5377\u5e8f\u53f7')),
                ('code', models.CharField(default=b'', unique=True, max_length=20, verbose_name='\u7f16\u7801')),
                ('start_vol', models.SmallIntegerField(default=0, verbose_name='\u8d77\u59cb\u518c\u7801')),
                ('start_page', models.SmallIntegerField(default=0, verbose_name='\u7ec8\u6b62\u518c\u7801')),
                ('end_vol', models.SmallIntegerField(default=0, verbose_name='\u7ec8\u6b62\u518c\u7801')),
                ('end_page', models.SmallIntegerField(default=0, verbose_name='\u7ec8\u6b62\u9875\u7801')),
                ('text_content_trad', models.TextField(default=b'', verbose_name='\u5377\u6587\u672c\uff08\u7e41\u4f53\uff09')),
                ('text_content_simpl', models.TextField(default=b'', verbose_name='\u5377\u6587\u672c\uff08\u7b80\u4f53\uff09')),
            ],
        ),
        migrations.CreateModel(
            name='Sutra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(default=b'', unique=True, max_length=16, verbose_name='\u7f16\u7801')),
                ('display', models.CharField(default=b'', max_length=128, verbose_name='\u7ecf\u672c\u540d\u79f0')),
                ('era', models.CharField(default=b'', max_length=12, verbose_name='\u5e74\u4ee3')),
                ('author', models.CharField(default=b'', max_length=32, verbose_name='\u4f5c\u8005')),
                ('translator', models.CharField(default=b'', max_length=32, verbose_name='\u8bd1\u8005')),
                ('reels_count', models.SmallIntegerField(default=0, verbose_name='\u603b\u5377\u6570')),
                ('start_vol', models.SmallIntegerField(default=0, verbose_name='\u8d77\u59cb\u518c\u7801')),
                ('start_page', models.SmallIntegerField(default=0, verbose_name='\u7ec8\u6b62\u518c\u7801')),
                ('end_vol', models.SmallIntegerField(default=0, verbose_name='\u7ec8\u6b62\u518c\u7801')),
                ('end_page', models.SmallIntegerField(default=0, verbose_name='\u7ec8\u6b62\u9875\u7801')),
                ('discription', models.CharField(default=b'', max_length=512, verbose_name='\u63cf\u8ff0\u4fe1\u606f')),
                ('normal_sutra', models.ForeignKey(verbose_name='\u9f99\u6cc9\u7ecf\u76ee', to='catalogue.LQSutra', null=True)),
            ],
            options={
                'verbose_name': '\u5b9e\u4f53\u7ecf\u672c',
                'verbose_name_plural': '\u5b9e\u4f53\u7ecf\u672c',
            },
        ),
        migrations.CreateModel(
            name='Tripitaka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u540d\u79f0')),
                ('code', models.CharField(unique=True, max_length=4, verbose_name='\u7f16\u7801')),
                ('era', models.CharField(max_length=32, verbose_name='\u5e74\u4ee3')),
            ],
            options={
                'verbose_name': '\u7ecf\u85cf',
                'verbose_name_plural': '\u7ecf\u85cf',
            },
        ),
        migrations.CreateModel(
            name='VariantTripitaka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=6, verbose_name='\u7f16\u7801')),
                ('vendor', models.CharField(max_length=64, verbose_name='\u51fa\u7248\u5546')),
                ('pub_date', models.DateField(verbose_name='\u51fa\u7248\u65e5\u671f')),
                ('pub_version', models.CharField(max_length=12, verbose_name='\u7248\u672c\u6279\u6b21')),
                ('display', models.CharField(max_length=64, verbose_name='\u540d\u79f0')),
                ('cover', models.ImageField(upload_to=b'cover', verbose_name='\u5c01\u9762\u4fe1\u606f')),
                ('volumes_count', models.SmallIntegerField(default=0, verbose_name='\u603b\u518c\u6570')),
                ('is_electronic', models.BooleanField(default=False, verbose_name='\u662f\u5426\u4e3a\u7535\u5b50\u7248')),
                ('tripitaka', models.ForeignKey(related_name='variants', verbose_name='\u7ecf\u85cf', to='catalogue.Tripitaka')),
            ],
            options={
                'verbose_name': '\u5b9e\u4f53\u7ecf\u85cf',
                'verbose_name_plural': '\u5b9e\u4f53\u7ecf\u85cf',
            },
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(default=b'', unique=True, max_length=12, verbose_name='\u7f16\u7801')),
                ('vol_num', models.SmallIntegerField(default=1, verbose_name='\u518c\u5e8f\u53f7')),
                ('pages_count', models.SmallIntegerField(default=0, verbose_name='\u603b\u9875\u6570')),
                ('start_page', models.SmallIntegerField(default=1, verbose_name='\u8d77\u59cb\u9875\u7801')),
                ('end_page', models.SmallIntegerField(default=1, verbose_name='\u7ec8\u6b62\u9875\u5417')),
                ('cover', models.ImageField(upload_to=b'cover', verbose_name='\u5c01\u9762\u4fe1\u606f')),
                ('tripitaka', models.ForeignKey(related_name='volumes', verbose_name='\u7ecf\u85cf', to='catalogue.VariantTripitaka')),
            ],
            options={
                'verbose_name': '\u518c',
                'verbose_name_plural': '\u518c',
            },
        ),
        migrations.AddField(
            model_name='sutra',
            name='tripitaka',
            field=models.ForeignKey(related_name='sutras', verbose_name='\u7ecf\u85cf', to='catalogue.VariantTripitaka'),
        ),
        migrations.AddField(
            model_name='reel',
            name='sutra',
            field=models.ForeignKey(related_name='reels', verbose_name='\u5b9e\u4f53\u7ecf\u672c', to='catalogue.Sutra'),
        ),
        migrations.AddField(
            model_name='page',
            name='reel',
            field=models.ForeignKey(related_name='pages', to='catalogue.Reel', null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='sutra',
            field=models.ForeignKey(related_name='pages', verbose_name='\u5b9e\u4f53\u7ecf\u672c', to='catalogue.Sutra', null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='volume',
            field=models.ForeignKey(related_name='pages', to='catalogue.Volume', null=True),
        ),
    ]
