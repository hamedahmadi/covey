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
        "to": "f2EuH9nOWn0:APA91bGXzlP00lEmTAvpVPno2ySFIup6usem012F0j547ZqqkXbwdrd5aQIHsKz7LHkJGTLUesKQyXXHsVc6qlC8IMRiL8eoAgbN8eR2d4uAof-NLznqCE3OSj8aneOGadoai0sbcyrq",
        "notification" : {
            "title": "Flock to Caltrain",
            "body": "Take the Caltrain today and receive 100 points."
        },
    }
    response = requests.post('https://fcm.googleapis.com/fcm/send',
                             headers=headers, data=json.dumps(data))
    return HttpResponse('')
