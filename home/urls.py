from django.urls import path

from . import views

urlpatterns = [

    path('', views.homeIndex, name='homeIndex'),
    path('LoginAction/', views.hadleLogin, name='hadleLogin'),
    path('Logout/', views.handleLogout, name='handleLogout'),
]