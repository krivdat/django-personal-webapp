from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Adjective1, Adjective2, Adjective3, Position
import random


def index(request):
    adj1 = Adjective1.objects.order_by('?').first()
    adj2 = Adjective2.objects.order_by('?').first()
    adj3 = Adjective3.objects.order_by('?').first()
    pos = Position.objects.order_by('?').first()
    jobtitle = adj1.word + ' ' + adj2.word + ' ' + adj3.word + ' ' + pos.word
    return render(request, 'jobtitlegenerator/base.html', {'jobtitle': jobtitle})


@login_required
def loaddata(request):
    with open('jobtitlegenerator/media/adjective1.txt') as f:
        Adjective1.objects.all().delete()
        entries = f.readlines()
        for line in entries:
            new_entry = Adjective1(word = line)
            new_entry.save()
    with open('jobtitlegenerator/media/adjective2.txt') as f:
        Adjective2.objects.all().delete()
        entries = f.readlines()
        for line in entries:
            new_entry = Adjective2(word = line)
            new_entry.save()
    with open('jobtitlegenerator/media/adjective3.txt') as f:
        Adjective3.objects.all().delete()
        entries = f.readlines()
        for line in entries:
            new_entry = Adjective3(word = line)
            new_entry.save()
    with open('jobtitlegenerator/media/position.txt') as f:
        Position.objects.all().delete()
        entries = f.readlines()
        for line in entries:
            new_entry = Position(word = line)
            new_entry.save()

    return render(request, 'jobtitlegenerator/filldata.html', {
        'adj1': Adjective1.objects.all(),
        'adj2': Adjective2.objects.all(),
        'adj3': Adjective3.objects.all(),
        'pos': Position.objects.all(),
        })
