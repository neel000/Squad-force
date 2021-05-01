from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from django.contrib import messages
import datetime

def socialIndex(request):
    return render(request, 'social/socialIndex.html')

def post(request):
    return render(request, 'social/post.html')

def news(request):
    return render(request, 'social/news.html')

def vdo(request):
    return render(request, 'social/vdo.html')
