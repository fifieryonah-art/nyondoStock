from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def creditsales(request):
    return render(request,'creditsales.html')

def dashboard(request):
    return render(request,'dashboard.html')

def salesregistration(request):
    return render(request,'salesregistration.html')

def stockregistration(request):
    return render(request,'stockregistration.html')