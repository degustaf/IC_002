from django.shortcuts import render

def Word_Madness_Index(request):
    return render(request, 'Word_Madness/index.html')
