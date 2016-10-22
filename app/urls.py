from django.conf.urls import url
from app import views


urlpatterns = [
    url(regex=r'^home$', view=views.home, name='home'),
    url(regex=r'^user', view=views.user, name='user'),
]
