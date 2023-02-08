from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_login),
    path('login', views.login, name='login'),
    path('register', views.register, name='register')
]