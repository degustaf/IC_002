# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Word_Madness', '0004_auto_20151128_0520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wordblank',
            old_name='MadLib',
            new_name='mad_lib',
        ),
        migrations.AlterField(
            model_name='wordblank',
            name='part_of_speech',
            field=models.CharField(max_length=20, choices=[('Adjective', 'Adjective'), ('Adjective: Ending in "ing"', 'Adjective: Ending in "ing"'), ('Adverb', 'Adverb'), ('Color', 'Color'), ('Noun', 'Noun'), ('Number', 'Number'), ('Plural Noun', 'Plural Noun'), ('Verb', 'Verb'), ('Verb: past tense', 'Verb: past tense')]),
        ),
    ]
