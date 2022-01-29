from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core import serializers
import json

def login_user(request):
    context = {}
    email = password = ""
    if request.POST:
        email = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                next_page = request.POST["next"] or "app"
                return HttpResponseRedirect(next_page)
        else:
            context["wrong_credentials"] = True
    return render(request, "predict/login.html", context)

def logout_user(request):
	logout(request)
	return HttpResponseRedirect("/login")

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def app(request):
    return render(request, "predict/index.html")

def predict(request):
	return render(request, "predict/index.html")

def graph(request):
	return render(request, "predict/graph.html")

from predict import models
from predict import forms
from predict.model_predict import predict_data

def add_xlsx(request):
    form = forms.FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        file = form.save(commit=False)
        file.user = request.user
        file.save()
        job = models.RunningJobs(datafile = file)
        job.save()
        predict_data(job.id)

    context = {"form": form}
    
    return render(request, 'predict/upload.html', context)

def get_data(request, key_id):
	d = json.loads(models.DataPrediction.objects.get(datafile_id=key_id).predictionsJSON)
	return JsonResponse(d)

