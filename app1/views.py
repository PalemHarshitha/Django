from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Harshitha(request):
    return HttpResponse('Harshitha is a simple girl<marquee>Hello</marquee>')

def honey(request):
    return HttpResponse('Honey Bunny')

def image(request):
    return HttpResponse("<h1>Siva</h1><img src='https://tse2.mm.bing.net/th?id=OIP.t7MleCFAPbXdMipDxfZ5xgHaHa&pid=Api&P=0&h=180'>")