from django.shortcuts import render

# Create your views here.
from App04.models import User


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.filter(username=username).first()
        if
    return None


def login(request):
    return None


def index(request):
    return None


def logout(request):
    return None