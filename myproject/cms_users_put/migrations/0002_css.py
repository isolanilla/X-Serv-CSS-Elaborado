# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_users_put', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Css',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('page', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
