# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_auto_20150504_1729'),
        ('leagues', '0006_auto_20150521_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('availability', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('event_id', models.ForeignKey(to='leagues.Event')),
                ('player_id', models.ForeignKey(to='teams.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
