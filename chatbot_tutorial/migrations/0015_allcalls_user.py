# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-02 15:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatbot_tutorial', '0014_remove_allcalls_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='allcalls',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
