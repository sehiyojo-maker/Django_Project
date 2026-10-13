from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('features/', views.features_view, name='features'),
    path('contact/', views.contact_view, name='contact'),
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='BudgetTracker/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]