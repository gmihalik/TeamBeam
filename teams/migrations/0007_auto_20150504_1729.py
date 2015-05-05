# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_auto_20150504_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_name',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='player',
            name='player_position',
            field=models.CharField(default=b'', max_length=1),
            preserve_default=True,
        ),
    ]
