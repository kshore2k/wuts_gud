from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^news$', views.news),
    url(r'^tech$', views.tech),
    url(r'^lifestyle$', views.lifestyle),
    url(r'^quotes$', views.quotes),
]