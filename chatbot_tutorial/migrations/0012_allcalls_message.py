# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-28 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_tutorial', '0011_allcalls_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='allcalls',
            name='message',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
