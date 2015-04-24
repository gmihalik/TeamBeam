# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0003_auto_20150424_1950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='join',
            old_name='ipaddress',
            new_name='ip_address',
        ),
    ]
