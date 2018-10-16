from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        if request.POST.get('answer') == 'Kocham':
            return redirect('/ascii')
            # return render(request, 'home/wait.html')
        else:
            return render(request, 'home/index.html', {'context': 'Złe hasło... (wielkość liter ma znaczenie)'})
    return render(request, 'home/index.html')


def ascii(request):
    if request.method == 'POST':
        if request.POST.get('answer') == '779710611111410797':
            return redirect('/youtube')
        else:
            return render(request, 'home/ascii.html', {'context': 'Złe hasło... (wielkość liter ma znaczenie, cyfry bez spacji)'})
    return render(request, 'home/ascii.html')


def youtube(request):
    if request.method == 'POST':
        if request.POST.get('answer') == 'Portugalia':
            return render(request, 'home/youtube.html', {'good': 'Znudzona? Good! Teraz ładny buziak, bo nie powiem co dalej...'})
        else:
            return render(request, 'home/youtube.html', {'context': 'Zła odpowiedź... (wielkość liter ma znaczenie)'})
    return render(request, 'home/youtube.html')


def map(request):
    return render(request, 'home/map.html')

