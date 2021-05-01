from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from django.contrib import messages
import datetime

def profileIndex(request):
    return render(request, 'profile/profileIndex.html')

def staffIndex(request):
    return render(request, 'staff/staffIndex.html')