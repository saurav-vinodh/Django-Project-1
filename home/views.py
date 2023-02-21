from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.

def index(request):
    context={'name': 'Harry', 'course':'Django'}
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')
def project(request):
    return render(request,'project.html')

def contact(request):
    if request.method=="POST":
        print("This is post")
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        #print(name,phone,email,desc)
        ins=Contact(name=name,email=email,phone=phone,desc=desc)
        ins.save()
        print("The data has been written to the db")
    return render(request,'contact.html')

