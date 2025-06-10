from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.


def Home(request):
    return render(request,'index.html')