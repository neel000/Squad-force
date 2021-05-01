from django.urls import path

from . import views

urlpatterns = [
   
    path('', views.profileIndex, name='profileIndex'),
    path('Staff-Panel/', views.staffIndex, name='staffIndex'),
]