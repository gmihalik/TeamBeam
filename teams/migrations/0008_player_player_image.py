# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_auto_20150504_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='player_image',
            field=models.ImageField(default='none', upload_to=b''),
            preserve_default=False,
        ),
    ]
