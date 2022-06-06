from django.http import HttpRequest
from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse('<h1>JONINHAS FUDEU!<h1>')
