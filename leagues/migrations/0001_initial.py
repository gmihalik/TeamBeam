# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_auto_20150504_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_name', models.CharField(max_length=200)),
                ('event_date', models.DateTimeField(auto_now=True)),
                ('event_location', models.CharField(max_length=200)),
                ('event_time', models.DateTimeField(auto_now=True)),
                ('event_is_game', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('league_name', models.CharField(default=b'None', max_length=200)),
                ('season', models.CharField(default=b'None', max_length=200)),
                ('division', models.CharField(default=b'None', max_length=200)),
                ('current', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('team_id', models.ForeignKey(to='teams.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
