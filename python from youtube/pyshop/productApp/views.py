from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# hit to  /products -> call index function
def index(request):
    return HttpResponse("Hello First product Page")


def newFn(request):
    return HttpResponse("I am the NEW page :) 😉👏")
