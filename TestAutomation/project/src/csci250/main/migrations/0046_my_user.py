# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 14:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0045_student_assignment_answers_last_submit_date_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='My_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_section', models.CharField(max_length=30)),
                ('active_member', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]