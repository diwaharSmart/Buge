from django.contrib import admin
from django.urls import path
from website.views import *

urlpatterns = [
    path("<str:key>", PageView , name="page"),
    path("api/", ApiRequest.as_view(), name="api"),
]
