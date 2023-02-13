from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm
from .utils import authenticate_and_log_in_user
from . import password_validation

# Create your views here.


def redirect_to_login(request):
    return redirect('/login')


def log_in(request):
    if request.user.is_authenticated:
        return redirect('/api/overview')

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            authenticate_and_log_in_user(request, form)

            return redirect('/api/overview')

        else:
            return render(request, 'login.html', {'false_credentials': True})

    form = AuthenticationForm()

    return render(request, 'login.html')


def sign_up(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login')

        else:
            return render(request, 'signup.html', {'form': form})

    form = NewUserForm()

    return render(request, 'signup.html')
