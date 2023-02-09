from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .forms import NewUserForm
from django.contrib.auth import login

# Create your views here.


def redirect_to_login(request):
    return redirect('/login')


def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        print(form)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('/api/overview')

        else:
            return render(request, 'login.html')

    form = AuthenticationForm()

    return render(request, 'login.html')


def sign_up(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            return redirect('/login')

        else:
            return render(request, 'signup.html')

    form = NewUserForm()

    return render(request, 'signup.html')
