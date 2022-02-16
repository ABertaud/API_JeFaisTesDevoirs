from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django import forms
from .forms import UserRegistrationForm

# from django.conf import settings
# from django.core.mail import send_mail
# subject = 'welcome to GFG world'
# message = f'Hi {user.username}, thank you for registering in geeksforgeeks.'
# email_from = settings.EMAIL_HOST_USER
# recipient_list = [user.email, ]
# send_mail( subject, message, email_from, recipient_list )

class SignUpView(generic.CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'