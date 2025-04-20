from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
  
    path("", views.registerUser, name="register" ),
    path('login/', views.index, name="login"),
    path('homepage_pincode_search/', views.homepage_pincode_search, name="pincode_search" ),
    path('loggedin/', views.loggedIn, name="loggedin" ),
    path('logout/', views.logoutUser, name="logout" ),
    
    
    
    # path('feedback/', views.feedback, name="feedback" )
    
]
