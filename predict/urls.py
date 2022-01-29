from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name='login'),
    path('app', views.app, name='app'),
    path('loading/<int:id>', views.loading, name='loading'),
    path("logout/", views.logout_user, name="logout"),
    path("graph/", views.graph, name="graph"),
    path("download-xlsx/<int:key_id>", views.download_xlsx, name='key_id'),
    path('get_data/<int:key_id>/', views.get_data, name='key_id'),
    path("graph/<int:datafile_id>", views.graph, name="graph"),
]