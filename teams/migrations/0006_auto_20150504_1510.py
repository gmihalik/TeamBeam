# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_auto_20150504_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_id',
            field=models.CharField(default=b'ABC', unique=True, max_length=120),
            preserve_default=True,
        ),
    ]
