from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('', views.index, name = "home"),
    path('signup', views.signup, name = "signup"),
    path('signin', views.signin, name = "signin"),
    path('signout', views.signout, name = "signout"),
    path('activate/<uidb64>/<token>', views.activate, name = "activate"),
]
