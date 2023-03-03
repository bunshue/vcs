# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='urlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('src_url', models.URLField()),
                ('short_url', models.CharField(max_length=20)),
                ('count', models.PositiveIntegerField()),
            ],
        ),
    ]
