from django.urls import path

from . import views

urlpatterns = [
   
    path('', views.socialIndex, name='socialIndex'),
    path('Post/', views.post, name='post'),
    path('News/', views.news, name='news'),
    path('Vedio/', views.vdo, name='vdo'),
]