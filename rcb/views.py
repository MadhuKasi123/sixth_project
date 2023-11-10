from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.




def virat(request):
    return render(request,'virat.html')


def maxi(request):
    return HttpResponse('<h1>mat max</h1>')