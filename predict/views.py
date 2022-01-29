from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

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
                next_page = request.POST["next"]
                if not next_page:
                    return HttpResponseRedirect("/courses")
                return HttpResponseRedirect(next_page)
        else:
            context["wrong_credentials"] = True
    return render(request, "predict/login.html", context)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
	return render(request, "login/index.html")

def app(request):
    return render(request, "app/index.html")

def predict(request):
	return render(request, "predict/index.html")

def add_xlsx(request):
    return HttpResponse("Test")
