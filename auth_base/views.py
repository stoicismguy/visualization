from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .forms import UserForm


# Create your views here.
def login_view(request):
    return HttpResponse("login")


class LoginView(APIView):
    def post(self, request):
        pass

    def get(self, request):
        form = UserForm()
        return render(request, "login.html", {"form": form})


def register_view(request):
    return HttpResponse("register")
