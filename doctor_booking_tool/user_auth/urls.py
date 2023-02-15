from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_login),
    path('login', views.log_in, name='login'),
    path('signup', views.sign_up, name='signup'),
    path('logout', views.log_out, name='logout')
]
