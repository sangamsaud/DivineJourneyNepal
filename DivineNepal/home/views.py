from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from .models import *
from .models import Booking




class BaseView(View):
    views = {}
    # views['information'] = Information.objects.all()
    
    


class HomeView(BaseView):
    def get(self, request):
        self.views
        self.views['abouts'] = About.objects.all()
        self.views['service'] = Service.objects.all()
        self.views['destination'] = Destination.objects.all()
        self.views['teams'] = Team.objects.all()
        self.views['review'] = Review.objects.all()
        self.views['package'] = PackageDetail.objects.all()
        return render(request, 'index.html', self.views)


def about(request):
    views = {}
    views['abouts'] = About.objects.all()
    views['teams'] = Team.objects.all()
    return render(request ,'about.html', views)


def service(request):
    views = {}
    views['service'] = Service.objects.all()
    views['review'] = Review.objects.all()
    return render(request ,'service.html', views)



def destination(request):
    views = {}
    views['destination'] = Destination.objects.all()
    return render(request ,'destination.html', views)


def team(request):
    views = {}
    views['teams'] = Team.objects.all()
    return render(request ,'team.html', views)

def package(request):
    views ={}
    views['package'] = PackageDetail.objects.all()
    return render(request,'package.html', views)


def testimonial(request):
    views = {}
    views['review'] = Review.objects.all()
    return render(request ,'testimonial.html', views)

def booking(request):
    views = {}
    views['aboutBook'] = AboutBooking.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['date']
        destination = request.POST['destination']
        special_request = request.POST['special_request']

        book = Booking(
            name=name,
            email=email,
            date=date,
            destination=destination,
            special_request=special_request
        )
        book.save()
        messages.success(request, f"Dear {name},Your Booking is Placed")
        return redirect('booking')


    return render(request,'booking.html', views)



def contact(request):
    views = {}
    views['information'] = Information.objects.all()

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        data.save()
        messages.success(request, f"Dear {name}, Thanks for your time!")
        return redirect('contact')

    return render(request, 'contact.html', views)



def signup(request):
    if request.method == "POST":
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username is already taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'The email is already used.')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=password,
                )
                # messages.success(request, 'Sign up successful! Please log in.')
                return redirect('login')
        else:
            messages.error(request, 'The password does not match.')
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')