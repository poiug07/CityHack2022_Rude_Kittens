from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
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
    form = forms.AccessRequestForm(request.POST or None, request.FILES or None)
    context = {"form": form}
    if request.POST:
        print("post")
        if form.is_valid():
            print("is here")
            form.save()
            context["saved"] = True
        else:
            context["error"] = True
    return render(request, "predict/index.html", context)

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

def loading(request, id):
    return render(request, "predict/loading.html", {"id": id})

@login_required(login_url="/login")
def graph(request, datafile_id):
	return render(request, "predict/graph.html")

def get_data(request, key_id):
	d = models.DataPrediction.objects.get(datafile_id=key_id).predictionsJSON
	return JsonResponse(json.loads(d))

def delete_xlsx(request, id):
    models.DataFile.objects.filter(id=id).delete()
    return HttpResponseRedirect("/app")
from openpyxl import load_workbook, Workbook

def download_xlsx(request, key_id):
    d = json.loads(models.DataPrediction.objects.get(datafile_id=key_id).predictionsJSON)
    data = d["data"]

    wb = Workbook()
    sheet = wb.active

    sheet["A1"] = "Datetime"
    sheet["B1"] = "X1"
    sheet["C1"] = "X2"
    sheet["D1"] = "X3"
    sheet["E1"] = "X4"
    sheet["F1"] = "Y"

    for row, (datetime, x1, x2, x3, x4, y) in enumerate(data, start=2):
        sheet [f"A{row}"] = datetime
        sheet [f"B{row}"] = x1
        sheet [f"C{row}"] = x2
        sheet [f"D{row}"] = x3
        sheet [f"E{row}"] = x4
        sheet [f"F{row}"] = y

    path = settings.MEDIA_ROOT
    wb.save(path+"/files/"+str(key_id)+".xlsx")

    response = HttpResponse(wb, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xls"'


    return response