from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(requset):
    return render(requset,'index.html')
def about(requset):
    return render(requset,'about.html')
def contact(request):
    if request.method=='POST':
        email=request.POST.get('email')
        name=request.POST.get('name')
        phone=request.POST.get('Phone')
        desc=request.POST.get('desc')
        contact=Contact(email=email,name=name,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your request has been sent')
    return render(request,'contact.html')
def services(request):
    return render(request,'services.html')