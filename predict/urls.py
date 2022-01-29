from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name='login'),
    path('app', views.app, name='app'),
    path('predict', views.predict, name='predict'),
    path('add-xlsx', views.add_xlsx, name='upload_data'),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path('get_data/<key_id>/', views.get_data, name='key_id')
]