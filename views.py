from django.shortcuts import render, render_to_response
from django.http import Http404
from django.template.context_processors import csrf

def Word_Madness_Index(request):
    return render(request, 'Word_Madness/index.html')


def Create_Game(request):
    if request.method == 'GET':
        return render(request, 'Word_Madness/create_story.html')
    if request.method == 'POST':
        c={}
        c.update(csrf(request))
        return render_to_response(request, 'Word_Madness/create_story.html', c)
    raise Http404("Page Not Found")
