# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-04 10:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20170704_1034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment_question',
            old_name='question_title',
            new_name='title',
        ),
    ]
