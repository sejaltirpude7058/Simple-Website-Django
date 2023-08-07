from http.client import HTTPResponse
from django.shortcuts import render
from home.models import Home
from home.models import Registration
from home.models import Contact

# Create your views here.

def home(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        print(name, email, password)
        ins = Home(name=name, email=email, password=password)
        ins.save()
        print("The data has been written to the db")
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')


def gallery(request):
    return render(request, 'home/gallery.html')


def registration(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        repeat = request.POST['repeat']
        print(email, password, repeat)
        ins = Registration(email=email, password=password, repeat=repeat)
        ins.save()
        print("The data has been written to the db")
    return render(request, 'home/registration.html')


def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        phone = request.POST['phone']
        country = request.POST['country']
        write = request.POST['write']
       # print(name, phone, country, write)
        ins = Contact(name=name, phone=phone, country=country, write=write)
        ins.save()
        print("The data has been written to the db")
    return render(request, 'home/contact.html')

