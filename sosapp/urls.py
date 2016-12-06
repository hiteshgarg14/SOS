from django.conf.urls import url
from . import views

app_name = 'sos'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
]