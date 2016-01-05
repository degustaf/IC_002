"""
Module to allow admin to access WordMadness Data.
"""
from django.contrib import admin

from .models import MadLib, WordBlank

admin.site.register(MadLib)
admin.site.register(WordBlank)
