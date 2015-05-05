# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20150504_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='leauge_name',
            new_name='league_name',
        ),
    ]
