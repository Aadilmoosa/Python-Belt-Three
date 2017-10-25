from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^Dashboard$', views.Dashboard),
    url(r'^user/(?P<user_id>[^/]+)(?:/)*$', views.user),
    url(r'^addfriend/(?P<user_id>[^/]+)(?:/)*$', views.addfriend),
    url(r'^deletefriend/(?P<user_id>[^/]+)(?:/)*$', views.deletefriend),
    ]
