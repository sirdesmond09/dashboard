from django.shortcuts import render, redirect
from .models import *
import datetime

def index(request): 
    time = datetime.datetime.now() 

    content = { 
        'time': time
    }                               
    return render(request, 'dashboard.html', content )

def add_lawyer(request):

    if request.method == "POST":
        firstname     = request.POST.get('fname')
        lastname      = request.POST.get('lname')
        email         = request.POST.get('email')
        gender        = request.POST.get('gender')
        date_of_birth = request.POST.get('birthday')
        phone         = request.POST.get('phone')
        languages     = request.POST.get('languages')
        nationality   = request.POST.get('nationality')
        country       = request.POST.get('country')
        city          = request.POST.get('city')
        address       = request.POST.get('adress')

        Lawyers.objects.create( firstname = firstname, lastname = lastname, email = email, gender = gender, date_of_birth = date_of_birth, phone = phone, languages = languages, nationality = nationality, country = country, city = city, address = address)
        
        return redirect('/')

    return render(request, 'dashboard_add_lawyer.html')

def lawyers_profile(request):
    lawyers = Lawyers.objects.all()
    context = {
        'lawyers': lawyers,
    }


    return render(request, 'dashboard_lawyers.html', context )

def profile(request):

    return render(request, 'dashboard_lawyer_profile.html')


def add_user(request):

    if request.method == "POST":
        firstname     = request.POST.get('fname')
        lastname      = request.POST.get('lname')
        email         = request.POST.get('email')
        gender        = request.POST.get('gender')
        date_of_birth = request.POST.get('birthday')
        phone         = request.POST.get('phone')
        languages     = request.POST.get('languages')
        nationality   = request.POST.get('nationality')
        country       = request.POST.get('country')
        city          = request.POST.get('city')
        address       = request.POST.get('adress')

        Users.objects.create( firstname = firstname, lastname = lastname, email = email, gender = gender, date_of_birth = date_of_birth, phone = phone, languages = languages, nationality = nationality, country = country, city = city, address = address)
        
        return redirect('/')

    return render(request, 'dashboard_user-add.html')

def user_profile(request):
    users = Users.objects.all()
    context = {
        'users': users,
    }


    return render(request, 'dashboard_users.html', context )
         
          
             