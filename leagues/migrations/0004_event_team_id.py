# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_auto_20150504_1729'),
        ('leagues', '0003_auto_20150519_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='team_id',
            field=models.ForeignKey(default=12345, to='teams.Team'),
            preserve_default=False,
        ),
    ]
