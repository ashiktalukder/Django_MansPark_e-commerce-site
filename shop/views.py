from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,"shop/index.html")

def about(request):
    return render(request,"shop/aboutus.html")

def productv(request):
    return HttpResponse("Product hi")    
