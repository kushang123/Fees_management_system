from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import student
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')





