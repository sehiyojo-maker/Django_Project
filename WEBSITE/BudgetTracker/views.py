from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home_view(request):
    return render(request, 'BudgetTracker/home.html')

def about_view(request):
    return render(request, 'BudgetTracker/about.html')

def features_view(request):
    return render(request, 'BudgetTracker/features.html')

def contact_view(request):
    return render(request, 'BudgetTracker/contact.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'BudgetTracker/register.html', {'form': form})