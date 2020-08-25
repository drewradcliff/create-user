from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate

from custom_users.forms import LoginForm, SignupForm
from custom_users.models import MyUser
from mysite import settings


def index(request):
    return render(request, "index.html", {"settings": settings.AUTH_USER_MODEL})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                "username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
            else:
                print(user)
        else:
            print(form.errors)

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(username=data.get("username"), password=data.get(
                "password"), name=data.get("name"), age=data.get("age"), homepage=data.get("homepage"))
        else:
            print(form.errors)
        login(request, new_user)
        return HttpResponseRedirect(reverse("homepage"))

    form = SignupForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
