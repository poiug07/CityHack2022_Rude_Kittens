from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/add-xlsx', views.upload_xlsx, name='upload_data'),
]