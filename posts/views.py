from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def post(request):
    data={'result':"ok"}
    return JsonResponse(data)