# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Word_Madness', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word_blank',
            name='index_in_text',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='word_blank',
            name='original_word',
            field=models.CharField(default='', max_length=20),
        ),
    ]
