from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('app', views.app, name='app'),
    path('predict', views.predict, name='predict')
]