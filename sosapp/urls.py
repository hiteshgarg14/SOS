from django.conf.urls import url
from . import views

app_name = 'sos'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^report_once/$',views.report_once, name='report_once'),
    url(r'^i_experienced/$', views.i_experienced, name='i_experienced')
]
