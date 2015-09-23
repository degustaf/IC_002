from django.db import models


class Mad_Lib(models.Model):
    title = models.CharField(max_length=20)
    text =  models.CharField(max_length=1000)


class Word_blank(models.Model):
    parts_of_speech_choices = (
        ("Adjective", "Adjective"),
        ("Adverb", "Adverb"),
        ("Color", "Color"),
        ("Noun", "Noun"),
        ("Number", "Number"),
        ("Plural Noun", "Plural Noun"),
        ("Verb", "Verb")
    )

    mad_lib = models.ForeignKey(Mad_Lib)
    part_of_speech = models.CharField(max_length=20, choices = parts_of_speech_choices)
