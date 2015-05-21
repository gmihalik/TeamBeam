# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0004_event_team_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_opponent',
            field=models.CharField(default='None', max_length=200),
            preserve_default=False,
        ),
    ]
