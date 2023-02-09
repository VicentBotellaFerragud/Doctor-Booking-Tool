from rest_framework.reverse import reverse
from django.shortcuts import redirect, render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
@api_view(['GET'])
def api_overview(request):
    data = {
        'year-summary-url': reverse('doctors', request=request)
    }
    return Response(data)


@api_view(['GET', 'POST', 'DELETE'])
def get_all_doctors(request):
    return Response('here you can see all the doctors')
