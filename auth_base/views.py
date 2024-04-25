from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from django.contrib.auth.models import User


# Create your views here.
def login_view(request):
    return HttpResponse("login")


class LoginView(APIView):
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=request.POST.get("username"),
                                password=request.POST.get("password"))
            if user is not None:
                login(request, user)
                return redirect('index')
        return render(request, "login.html", {"form": form})

    def get(self, request):
        form = UserForm()
        return render(request, "login.html", {"form": form})


class RegisterView(APIView):
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            existing_user = User.objects.filter(username=username)
            if len(existing_user) == 0:
                password = request.POST.get("password")
                user = User.objects.create_user(username, '', password)
                user.save()
                user = authenticate(request,
                                    username=username,
                                    password=password)
                login(request, user)
                return redirect('index')
            
        return render(request, "register.html", {"form": form})

    def get(self, request):
        form = UserForm()
        return render(request, "register.html", {"form": form})


def register_view(request):
    return HttpResponse("register")
