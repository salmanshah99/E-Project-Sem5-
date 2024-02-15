# from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('modes', views.modes, name="modes"),
    path('register',views.register,name="register"),
    path('register_submit', views.register_submit, name="register_submit"),
    path('home', views.home, name="home"),
    path('login', views.login, name="login"),
    path('login_submit', views.login_submit, name="login_submit"),

]