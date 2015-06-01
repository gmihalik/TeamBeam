# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0009_auto_20150531_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_image',
            field=models.ImageField(default=b'./static/teambeam/img/blank.jpg', upload_to=b'./static/teambeam/img/user_images'),
            preserve_default=True,
        ),
    ]
