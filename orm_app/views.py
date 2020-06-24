from django.shortcuts import render, HttpResponse, redirect
from .models import User

def index(request):
    
    context = {
        "all_users": User.objects.all()
    }
    
    return render(request, "index.html", context)


def create(request):
    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        age=request.POST['age'],
        email_address=request.POST['email_address'],
    )
    return redirect('/')
    
    
    
    