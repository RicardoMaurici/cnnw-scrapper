from django.shortcuts import render

def index(request):
	context = {}
	return render(request, 'webclient/index.html', context)

def search(request):
	context = {}
	return render(request, 'webclient/search.html', context)

def config(request):
	context = {}
	return render(request, 'webclient/config.html', context)