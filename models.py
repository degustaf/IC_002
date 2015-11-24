from django.db import models


class MadLib(models.Model):
    @staticmethod
    def max_text_length():
        return 1000

    title = models.CharField(max_length=20)
    text =  models.CharField(max_length=max_text_length.__func__())

class WordBlank(models.Model):
    parts_of_speech_choices = (
        ("Adjective", "Adjective"),
        ("Adverb", "Adverb"),
        ("Color", "Color"),
        ("Noun", "Noun"),
        ("Number", "Number"),
        ("Plural Noun", "Plural Noun"),
        ("Verb", "Verb")
    )

    mad_lib = models.ForeignKey(MadLib)
    part_of_speech = models.CharField(max_length=20, choices = parts_of_speech_choices)
    original_word = models.CharField(max_length=20, default="")
    index_in_text = models.PositiveSmallIntegerField(default=0)
