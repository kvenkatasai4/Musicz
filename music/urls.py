from django.conf.urls import url
from . import views

app_name = "music"

urlpatterns = [
    #/music/
    url(r'^$', views.Indexview.as_view(), name="index"),

    #/music/register/
    url(r'^register/$', views.UserFormView.as_view(), name="register"),

    #/music/123
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="details"),

    # /music/album/add/
    url(r"^album/add/$", views.AlbumCreate.as_view(), name="album-add"),

    #/music/album/123/
    url(r"^album/(?P<pk>[0-9]+)/$", views.AlbumUpdate.as_view(), name="album-update"),

    #/music/album/123/delete
    url(r"^album/(?P<pk>[0-9]+)/delete/$", views.AlbumDelete.as_view(), name="album-delete"),
]