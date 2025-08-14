from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),       # Home page -> index.html
    path('home/', views.home, name='home'),    # Home page route -> home.html
    path('about/', views.about, name='about'), # About page
    path('skills/', views.skills, name='skills'), # skills page
    path('contact/', views.contact, name='contact'),  # Contact form
]
