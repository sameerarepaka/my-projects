from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Sri/',views.firstpage,name='first'),
    path('Sameera/',views.secondpage,name='second'),
    path('Repaka/',views.htmlpage,name='last'),
    
]