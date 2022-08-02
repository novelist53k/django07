from django.urls import path, include
from . import views

app_name="board"
urlpatterns = [
    path("index/", views.index, name="index"),
    path("detail/<bpk>", views.detail, name="detail"),
    path("delete/<bpk>", views.delete, name="delete"),
    path("create/", views.create, name="create"),
    path("update/<bpk>", views.update, name="update"),
    path("dreply/<bpk>/<rpk>", views.deleteReply, name="dreply"),
    path("creply/<bpk>", views.creply, name="creply"),
    path("ureply/<bpk>/<rpk>", views.ureply, name="ureply"),
]