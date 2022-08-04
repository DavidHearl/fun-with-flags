from django.shortcuts import render
from .models import Flag


def game(request):

    flags = Flag.objects.all()

    context = {
        'flags': flags
    }

    return render(request, 'game/game.html', context)


def easy(request):

    flags = Flag.objects.all()

    context = {
        'flags': flags
    }

    return render(request, 'game/easy.html', context)
