from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm
from .utils import authenticate_and_log_in_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.


def redirect_to_login(request):
    return redirect('/login')


def log_in(request):
    if request.user.is_authenticated:
        return redirect('/api')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            authenticate_and_log_in_user(request, form)

            return redirect('/api')
        else:
            return render(request, 'login.html', {'login_or_signup_view': True, 'invalid_credentials': True})

    form = AuthenticationForm()

    return render(request, 'login.html', {'login_or_signup_view': True})


def sign_up_and_log_in(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()
            authenticate_and_log_in_user(request, form, 'signup')

            return redirect('/api')
        else:
            return render(request, 'signup.html', {'login_or_signup_view': True, 'form': form})

    form = NewUserForm()

    return render(request, 'signup.html', {'login_or_signup_view': True})


@login_required(login_url='/login')
def log_out(request):
    logout(request)

    return redirect('/login')
