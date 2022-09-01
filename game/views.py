from django.shortcuts import render
from .models import Flag


def game(request):

    flags = Flag.objects.all()
    return render(request, 'game/game.html', {'flags': flags})


def easy(request):

    flags = Flag.objects.all()
    return render(request, 'game/easy.html', {'flags': flags})


def medium(request):

    flags = Flag.objects.all()
    return render(request, 'game/medium.html', {'flags': flags})


def hard(request):

    flags = Flag.objects.all()
    return render(request, 'game/hard.html', {'flags': flags})


def extreme(request):

    flags = Flag.objects.all()
    return render(request, 'game/extreme.html', {'flags': flags})
