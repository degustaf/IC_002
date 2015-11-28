# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Word_Madness', '0003_auto_20151115_2322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wordblank',
            old_name='mad_lib',
            new_name='MadLib',
        ),
    ]
