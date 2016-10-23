import json
import requests

from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.response import TemplateResponse


def home(request):
    return TemplateResponse(request, 'home.html')


def admin(request):
    return TemplateResponse(request, 'admin.html')


def user(request):
    _type = request.GET.get('type', None)
    if _type == 'new':
        return TemplateResponse(request, 'new-user.html')
    return TemplateResponse(request, 'current-user.html')


def send_push_notification(request):
    headers = {
        'Authorization': 'key=AIzaSyAxJyzPAclQsMyoNos6DJT4Zh-gLEty_Go',
        'Content-Type': 'application/json',
    }
    data = {
        "to" : "",
        "notification" : {
            "title": "Portugal vs. Denmark",
            "body": "5 to 1"
        },
    }
    response = requests.post('https://fcm.googleapis.com/fcm/send',
                             headers=headers, data=json.dumps(data))
    print response.content
    return HttpResponse('')
