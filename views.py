from django.http import Http404
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.views.decorators.http import require_safe, require_http_methods
from .models import Mad_Lib, Word_blank
import re

@require_safe
def Word_Madness_Index(request):
    return render(request, 'Word_Madness/index.html')


@require_http_methods(["GET", "HEAD", "POST"])
def Create_Game(request):
    if request.method == 'GET':
        return render(request, 'Word_Madness/create_story.html', 
            {'text_length':Mad_Lib.max_text_length()})
    if request.method == 'POST':
        params = dict(request.POST)
        if 'id' in params:
            # Text was already entered, and we are removing words for the game
            game = Mad_Lib.objects.get(id=params['id'])
            text = params['story_body']
            game.text = re.sub('___\((\d+)\)___', '{\0}', text)
            game.save()
            match = re.compile('words_(\d+)')
            for key, values in params.items():
                if  match = re.match(key):
                    word = models.Word_blank()
        else:
            print(params)
            game = Mad_Lib(title=params['title'], text=params['body'])
            game.save()
            print(game.id)
            params['id'] = game.id
            params['parts_of_speech'] = [x[0] for x in Word_blank.parts_of_speech_choices]
            return render(request, 'Word_Madness/remove_words.html', params)
    raise Http404("Page Not Found")
