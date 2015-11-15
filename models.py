from django.db import models


class Mad_Lib(models.Model):
    @staticmethod
    def max_text_length():
        return 1000

    title = models.CharField(max_length=20)
    text =  models.CharField(max_length=max_text_length.__func__())

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
    original_word = models.CharField(max_length=20)
    index_in_text = models.PositiveSmallIntegerField()
