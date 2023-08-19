from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer, Comment
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "index.html")

def aboutus(request):
    return render(request,"aboutus.html")
def registration(request):
    return render(request,"registration.html")

def eventdetail(request):
    return render(request,"eventdetail.html")

def contact(request):
    cdata = Comment.objects.all()
    cont = {"data": cdata}
    return render(request,"contact.html", cont)

@csrf_exempt
def insertComment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)
        query = Comment(name=name, email=email, message=message)
        query.save()
        messages.success(request, "Comment Successful.")
    return render(request, "contact.html")


def login(request):
    data = Customer.objects.all()
    context = {"data": data}
    return render(request, "login.html", context)

@csrf_exempt
def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        gender = request.POST.get('gender')
        event = request.POST.get('event')
        location = request.POST.get('location')
        print(name, email, phone, date, gender, event, location)
        query = Customer(name=name, email=email, phone=phone, date=date, gender=gender, event=event, location=location)
        query.save()
        messages.success(request, "Registration Successful.")
    return render(request,"login.html")
