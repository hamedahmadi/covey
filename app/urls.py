from django.conf.urls import url
from app import views


urlpatterns = [
    url(regex=r'^home$', view=views.home, name='home'),
    url(regex=r'^admin', view=views.admin, name='admin'),
    url(regex=r'^send_push_notification', view=views.send_push_notification, name='send_push_notification'),
    url(regex=r'^user', view=views.user, name='user'),
]
