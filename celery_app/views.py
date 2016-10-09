#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .tasks import hello_world
def index(request):
    hello_world.delay()
    return HttpResponse(u"Fuck the GFW")
