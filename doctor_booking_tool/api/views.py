from django.shortcuts import redirect, render
from django.http import JsonResponse

# Create your views here.

def test(request):
    return JsonResponse('test', safe=False)
