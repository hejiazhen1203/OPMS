# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-02 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_userloginrecord_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userloginrecord',
            name='agent',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='客户端'),
        ),
    ]