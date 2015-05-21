# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0002_auto_20150518_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='league_id',
            field=models.ForeignKey(default='12345', to='leagues.League'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='league',
            name='league_id',
            field=models.CharField(default=b'12345', max_length=200),
            preserve_default=True,
        ),
    ]
