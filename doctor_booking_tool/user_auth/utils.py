from django.contrib.auth import authenticate
from django.contrib.auth import login


def authenticate_and_log_in_user(request, form):
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')
    user = authenticate(username=username, password=password)
    login(request, user)
