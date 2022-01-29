from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import json

from predict import models
from predict import forms
from predict.model_predict import predict_data

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
    if request.user.is_authenticated:
        return HttpResponseRedirect("/app")
    return render(request, "predict/index.html")

@login_required(login_url="/login")
def app(request):
    form = forms.FileForm(request.POST or None, request.FILES or None)
    context = {"form": form}
    if form.is_valid():
        file = form.save(commit=False)
        file.user = request.user
        file.save()
        job = models.RunningJobs(datafile = file)
        job.save()
        predict_data(job.datafile_id)
        context["succes"] = True
        context["form"] = forms.FileForm(None, None)
    context["datafiles"] = models.DataFile.objects.all()
    return render(request, "predict/app.html", context)

@login_required(login_url="/login")
def graph(request):
	return render(request, "predict/graph.html")

def get_data(request, key_id):
	d = models.DataPrediction.objects.get(datafile_id=key_id).predictionsJSON
	return JsonResponse(json.loads(d))

