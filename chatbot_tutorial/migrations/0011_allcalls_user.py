# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2021-03-28 06:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatbot_tutorial', '0010_auto_20210326_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='allcalls',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
