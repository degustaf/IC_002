"""
Models for controlling MadLib game in WordMadness.
"""
from django.db import models


class MadLib(models.Model):
    """
    Body of a MadLibs game.
    """
    @staticmethod
    def max_text_length():
        """
        Class level read only variable for max length of text fields.
        """
        return 1000

    title = models.CharField(max_length=20)
    text = models.CharField(max_length=max_text_length.__func__())


class WordBlank(models.Model):
    """
    Details of a removed word from a madlibs game.
    """
    parts_of_speech_choices = (
        ("Adjective", "Adjective"),
        ("Adjective: Ending in \"ing\"", "Adjective: Ending in \"ing\""),
        ("Adverb", "Adverb"),
        ("Color", "Color"),
        ("Noun", "Noun"),
        ("Number", "Number"),
        ("Plural Noun", "Plural Noun"),
        ("Verb", "Verb"),
        ("Verb: past tense", "Verb: past tense")
    )

    mad_lib = models.ForeignKey(MadLib)
    part_of_speech = models.CharField(max_length=20,
                                      choices=parts_of_speech_choices)
    original_word = models.CharField(max_length=20, default="")
    index_in_text = models.PositiveSmallIntegerField(default=0)
