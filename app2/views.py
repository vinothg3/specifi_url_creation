from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_string(request):
    return HttpResponse('second application html page')

def app2_htpage(request):
    return render(request,'app2_htpage.html')