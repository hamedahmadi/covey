from django.conf.urls import url
from app import views


urlpatterns = [
    url(regex=r'^home$', view=views.home, name='home'),
    url(regex=r'^admin', view=views.admin, name='admin'),
    url(regex=r'^user', view=views.user, name='user'),
]
