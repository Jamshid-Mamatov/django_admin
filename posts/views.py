from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
# Create your views here.
def post(request):
    post=Posts.objects.all()
    data=serializers.serialize('json',post)
    print(type(post),post)
    return HttpResponse(data,content_type='text/json')