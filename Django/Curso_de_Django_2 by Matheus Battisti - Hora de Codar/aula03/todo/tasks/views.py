from django.shortcuts import render
from django.http import HttpResponse

def helloWord(request):
    return HttpResponse('Hello World!')
