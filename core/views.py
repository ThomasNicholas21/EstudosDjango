from django.http import HttpRequest
from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse('\n<h1>TESTE!\nTESTE!<h1>')


