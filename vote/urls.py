from django.urls import path
from . import views

app_name="vote"
urlpatterns = [
    path("index/", views.index, name="index"),
    path("detail/<tpk>", views.detail, name="detail"),
    path("vote/<tpk>", views.vote, name="vote"),
    path("cancel/<tpk>", views.cancle, name="cancle"),
    path("vote/", views.create, name="create"),
    path("delete/<tpk>", views.delete, name="delete")
]