from django.conf.urls import url
from . import views

app_name="blog"
urlpatterns = [
    url(r'^$', views.list, name="list"),
    url(r'^(?P<id>\d+)$', views.details, name="details"),
    url(r'^author/(?P<id>\d+)$', views.author, name="author"),
]
