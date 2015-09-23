# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mad_Lib',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Word_blank',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('part_of_speech', models.CharField(choices=[('Adjective', 'Adjective'), ('Adverb', 'Adverb'), ('Color', 'Color'), ('Noun', 'Noun'), ('Number', 'Number'), ('Plural Noun', 'Plural Noun'), ('Verb', 'Verb')], max_length=20)),
                ('mad_lib', models.ForeignKey(to='Word_Madness.Mad_Lib')),
            ],
        ),
    ]
