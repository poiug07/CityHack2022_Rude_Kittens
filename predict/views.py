from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
	return render(request, "login/index.html")

def app(request):
    return render(request, "app/index.html")

def predict(request):
	return render(request, "predict/index.html")