# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-10-25 20:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20171025_2044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='birth_year',
            new_name='birth_date',
        ),
    ]