# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_my_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_user',
            name='user_section',
            field=models.CharField(max_length=50),
        ),
    ]
