from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^create/$', views.create, name="create"),
    url(r'^new/$', views.new, name="new"),
    # url(r'^(?P<dojo_id>\d+)/edit/$', views.show, name="edit"),
    # url(r'^(?P<dojo_id>\d+)/show/$', views.show, name="show"),
    # url(r'^(?P<dojo_id>\d+)/update/$', views.update, name="update"),
    # url(r'^(?P<dojo_id>\d+)/delete/$', views.delete, name="delete"),
    url(r'^logout/$', views.logout, name="logout"),
]