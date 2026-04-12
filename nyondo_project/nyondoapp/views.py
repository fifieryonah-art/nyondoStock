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

def salesdashboard(request):
    return render(request,'salesdashboard.html')

def sales(request):
    return render(request, 'sales.html')

def suppliers(request):
    return render(request, 'suppliers.html')

def withdraw(request):
    return render(request, 'withdraw.html')

def deposit(request):
    return render(request, 'deposit.html')

def customer(request):
    return render(request, 'customer.html')