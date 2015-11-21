from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Django Unchained")

def detail(request, note_id):
    return HttpResponse("This is note %s." % note_id)
