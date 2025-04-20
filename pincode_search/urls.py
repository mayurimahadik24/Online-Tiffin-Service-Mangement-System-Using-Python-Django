from django.urls import path
from pincode_search import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.pincode_search, name="pincode_search"),
    path('match/',views.match, name="match"),
    path('notmatch/',views.notmatch ,name="notmatch"),
]