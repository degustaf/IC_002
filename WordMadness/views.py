"""
Functions to control views of Pages
"""
from functools import partial
import re

from django.http import Http404
from django.shortcuts import render #, render_to_response
#from django.template.context_processors import csrf
from django.views.decorators.http import require_safe, require_http_methods
from .models import MadLib, WordBlank

@require_safe
def word_madness_index(request):
    """
    Render the main index page.
    """
    return render(request, 'WordMadness/index.html')


@require_http_methods(["GET", "HEAD", "POST"])
def create_game(request):
    """
    Process and render requests for creating a madlibs game.
    """
    if request.method == 'GET':
        return render(request, 'WordMadness/create_story.html',
                      {'text_length':MadLib.max_text_length()})
    if request.method == 'POST':
        params = dict(request.POST)
        if 'id' in params:
            # Text was already entered, and we are removing words for the game
            game_id = params['id'][0]
            game = MadLib.objects.get(id=game_id)
            text = params['story_body'][0]
            word_blanks = []
            repl = partial(substitution, word_blanks)
            game.text = re.sub('___\((\d+)\)___', repl, text)
            game.save()
            for idx, value in enumerate(word_blanks):
                word = WordBlank(
                    mad_lib=game, index_in_text=idx,
                    part_of_speech=params['Part_of_Speech_{}'.format(value)],
                    original_word=params['word_{}'.format(value)])
                word.save()
            return render(request, 'WordMadness/story_created.html', params)

        else:
            game = MadLib(title=params['title'], text=params['body'])
            game.save()
            params['id'] = game.id
            params['parts_of_speech'] = [x[0] for x in WordBlank.parts_of_speech_choices]
            return render(request, 'WordMadness/remove_words.html', params)
    raise Http404("Page Not Found")

def substitution(results, match):
    """
    Generate replacement text for Regex.
    The front-end does not handle missing indices created by removing word
    blanks.
    """
    i = len(results)
    results.append(match.group(1))
    return '{{{}}}'.format(i)

@require_safe
def play_index():
    """
    Render the index page for playing a game.
    """
#     params = dict(request.
#     return render(request, 'WordMadness/play_index.html')
