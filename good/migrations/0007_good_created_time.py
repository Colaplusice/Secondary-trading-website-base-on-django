# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-10 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0006_auto_20190408_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='created_time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
