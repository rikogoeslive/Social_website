from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Welcome To Social Website :) !</h1>')