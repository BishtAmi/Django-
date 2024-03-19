from django.contrib import admin
from django.urls import path
from demoapp.views import demo,Financial  # Assuming your views are in a file named 'views.py' inside the 'demoapp' app

urlpatterns = [
    path('',Financial.as_view()),
    # path('', demo.as_view()),
    
]
