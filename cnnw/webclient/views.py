from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Index CnNw.")

def search(request,search_id):
    return HttpResponse("search CnNw.")

def config(request):
    return HttpResponse("Config CnNw.")