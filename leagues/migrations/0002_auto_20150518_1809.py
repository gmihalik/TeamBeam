# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 18, 9, 12, 687427, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 18, 9, 20, 161036, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='league',
            name='league_name',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
