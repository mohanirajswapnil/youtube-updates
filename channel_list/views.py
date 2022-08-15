from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import channels


# Create your views here.

def test(request):
    return HttpResponse("<h1>Test Home Page</h1>")


def get_channels(request):
    return JsonResponse(channels.get_channels())
