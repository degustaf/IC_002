# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Word_Madness', '0002_auto_20151115_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordBlank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('part_of_speech', models.CharField(choices=[('Adjective', 'Adjective'), ('Adverb', 'Adverb'), ('Color', 'Color'), ('Noun', 'Noun'), ('Number', 'Number'), ('Plural Noun', 'Plural Noun'), ('Verb', 'Verb')], max_length=20)),
                ('original_word', models.CharField(default='', max_length=20)),
                ('index_in_text', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='Mad_Lib',
            new_name='MadLib',
        ),
        migrations.RemoveField(
            model_name='word_blank',
            name='mad_lib',
        ),
        migrations.DeleteModel(
            name='Word_blank',
        ),
        migrations.AddField(
            model_name='wordblank',
            name='mad_lib',
            field=models.ForeignKey(to='Word_Madness.MadLib'),
        ),
    ]
