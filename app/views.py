from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.response import TemplateResponse


def home(request):
    return TemplateResponse(request, 'home.html')


def user(request):
    _type = request.GET.get('type', None)
    if _type == 'current':
        return TemplateResponse(request, 'current-user.html')
    return TemplateResponse(request, 'new-user.html')


