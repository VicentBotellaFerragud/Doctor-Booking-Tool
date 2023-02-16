from django.contrib.auth import authenticate
from django.contrib.auth import login


def authenticate_and_log_in_user(request, form, from_login_or_signup_form='login'):
    username = form.cleaned_data.get('username')
    password = password_or_password1(form, from_login_or_signup_form)
    user = authenticate(username=username, password=password)
    login(request, user)


def password_or_password1(form, from_login_or_signup_form):
    if from_login_or_signup_form == 'login':
        password = form.cleaned_data.get('password')
    else:
        password = form.cleaned_data.get('password1')

    return password
