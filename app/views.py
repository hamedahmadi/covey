from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.response import TemplateResponse


def home(request):
    return TemplateResponse(request, 'home.html')


def admin(request):
    return TemplateResponse(request, 'admin.html')

def user(request):
    return TemplateResponse(request, 'user.html')
