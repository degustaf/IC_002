from django.http import Http404
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.views.decorators.http import require_safe, require_http_methods
from .models import Mad_Lib

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
