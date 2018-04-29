from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/$', views.apilist),
    url(r'^api/(?P<pk>[0-9]+)/$', views.apidetails),
]
