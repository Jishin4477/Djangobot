# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-03 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_tutorial', '0017_auto_20210403_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='getuser',
            name='date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]