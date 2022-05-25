from django.http import HttpResponse
from django.shortcuts import render
def display_home(request):
    return render(request, 'Home.html')