# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2021-03-26 15:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_tutorial', '0004_allcalls'),
    ]

    operations = [
        migrations.CreateModel(
            name='FatClick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_call', models.IntegerField(blank=True, null=True)),
                ('fat_val', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chatbot_tutorial.FatCalls')),
            ],
        ),
        migrations.RemoveField(
            model_name='allcalls',
            name='dumb_val',
        ),
        migrations.RemoveField(
            model_name='allcalls',
            name='fat_val',
        ),
        migrations.RemoveField(
            model_name='allcalls',
            name='stupid_val',
        ),
        migrations.DeleteModel(
            name='AllCalls',
        ),
    ]
