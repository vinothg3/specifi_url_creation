from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app_htpage(request):
    return render(request,'app_htpage.html')

def app_string(request):
    return HttpResponse('<h1>THIS IS SPEIFIC URL CRESTING METHODS<h1>')