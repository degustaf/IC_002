from django.shortcuts import render, render_to_response
from django.http import Http404
from django.template.context_processors import csrf
from .models import Mad_Lib

def Word_Madness_Index(request):
    return render(request, 'Word_Madness/index.html')


def Create_Game(request):
    if request.method == 'GET':
        return render(request, 'Word_Madness/create_story.html')
    if request.method == 'POST':
        params = dict(request.POST)
        if 'Words' in params:
            pass
        else:
            print(params)
            game = Mad_Lib(title=params['title'], text=params['body'])
            game.save()
            print(game.id)
            params['id'] = game.id
            return render(request, 'Word_Madness/remove_words.html', params)
    raise Http404("Page Not Found")
