# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-27 16:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160827_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titles',
            new_name='title',
        ),
    ]
