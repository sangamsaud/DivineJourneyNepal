from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', about, name = 'about'),
    path('service', service, name = 'service'),
    path('destination', destination, name = 'destination'),
    path('team', team, name = 'team'),
    path('contact', contact, name = 'contact'),
    path('package', package, name = 'package'),
    path('testimonial', testimonial, name = 'testimonial'),
    path('booking', booking, name = 'booking'),
    path('signup',signup, name = 'signup')
]