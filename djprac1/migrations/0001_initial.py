# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb')),
            ],
            options={
                'verbose_name': '\u535a\u5ba2\u5206\u7c7b',
                'verbose_name_plural': '\u535a\u5ba2\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe9\xa2\x98')),
                ('img', models.ImageField(upload_to=b'blog_img', null=True, verbose_name=b'\xe5\x8d\x9a\xe5\xae\xa2\xe9\x85\x8d\xe5\x9b\xbe', blank=True)),
                ('body', models.TextField(verbose_name=b'\xe6\xad\xa3\xe6\x96\x87')),
                ('abstract', models.TextField(max_length=256, null=True, verbose_name=b'\xe6\x91\x98\xe8\xa6\x81', blank=True)),
                ('visiting', models.PositiveIntegerField(default=0, verbose_name=b'\xe8\xae\xbf\xe9\x97\xae\xe9\x87\x8f')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('modifyed_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('author', models.ForeignKey(verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='djprac1.Category', verbose_name=b'\xe5\x8d\x9a\xe5\xae\xa2\xe5\x88\x86\xe7\xb1\xbb')),
            ],
            options={
                'ordering': ['-created_time'],
                'verbose_name': '\u535a\u5ba2\u6b63\u6587',
                'verbose_name_plural': '\u535a\u5ba2\u6b63\u6587',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe')),
            ],
            options={
                'verbose_name': '\u535a\u5ba2\u6807\u7b7e',
                'verbose_name_plural': '\u535a\u5ba2\u6807\u7b7e',
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='djprac1.Tag', verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe'),
        ),
    ]
