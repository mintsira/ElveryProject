from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from app_users.forms import RegisterForm, UserProfileForm

from store.models import *

def register(request: HttpRequest):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer, created = Customer.objects.get_or_create(user=user)
            customer.name = user.username
            customer.email = user.email
            customer.save()
            
            return HttpResponseRedirect(reverse('login'))
    else:
        form = RegisterForm()

    context = {"form": form}
    return render(request,"app_users/register.html", context)

@login_required
def dashboard(request: HttpRequest):
    
    return render(request, "app_users/dashboard.html")

@login_required
def profile(request: HttpRequest):
    user = request.user

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user)
        
        if form.is_valid():
            form.save()
           
            return HttpResponseRedirect(reverse("profile"))
    else:
        form = UserProfileForm(instance=user)

    context = {
        "form": form
    }
    return render(request, "app_users/profile.html", context)