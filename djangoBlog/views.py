from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    # return HttpResponse('home')
    return render(request, 'home.html')


def about(request):
    # return HttpResponse('hi there!')
    return render(request, 'about.html')
