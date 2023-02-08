from django.shortcuts import redirect, render
from django.http import JsonResponse

# Create your views here.

def redirect_to_login(request):
    return redirect('/login')

def login(request):
    return redirect('/api')

def register(request):
    return JsonResponse('register', safe=False)
