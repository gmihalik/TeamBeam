# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_remove_player_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='division',
            field=models.CharField(default=b'None', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='leauge_name',
            field=models.CharField(default=b'None', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='season',
            field=models.CharField(default=b'None', max_length=200),
            preserve_default=True,
        ),
    ]
