from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable': " This is variable porsion"
    }
    return render(request, 'index.html', context)

# def home(request):
#     return HttpResponse("This is home page")    

def about(request):
    # return HttpResponse("This is About page")
    return render(request, 'about.html')

def contactMe(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, phone=phone, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been uploaded...')
        
    return render(request, 'contact.html')

def python(request):
    return render(request, 'python.html')

def java(request):
    return render(request, 'java.html')

def other(request):
    return render(request, 'other.html')