# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MadLib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='WordBlank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_of_speech', models.CharField(choices=[('Adjective', 'Adjective'), ('Adjective: Ending in "ing"', 'Adjective: Ending in "ing"'), ('Adverb', 'Adverb'), ('Color', 'Color'), ('Noun', 'Noun'), ('Number', 'Number'), ('Plural Noun', 'Plural Noun'), ('Verb', 'Verb'), ('Verb: past tense', 'Verb: past tense')], max_length=20)),
                ('original_word', models.CharField(default='', max_length=20)),
                ('index_in_text', models.PositiveSmallIntegerField(default=0)),
                ('mad_lib', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WordMadness.MadLib')),
            ],
        ),
    ]
