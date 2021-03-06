from django.conf.urls import url
from . import views

app_name = 'sos'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^chat/$', views.chatIndex, name='chatIndex'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^report_once/$',views.report_once, name='report_once'),
    url(r'^i_experienced/$', views.i_experienced, name='i_experienced'),
    url(r'^eduction/$',views.education,name='education'),
    url(r'^exp_stories/$', views.exp_stories, name='exp_stories'),
    url(r'^rep_stories/$', views.rep_stories, name='rep_stories'),
    url(r'^story/(?P<id>\d+)/$', views.story, name ='story'),
]
