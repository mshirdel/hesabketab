from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'Accounting/index.html', {'user': request.user})


def join(request):
    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    return render(request, 'registration/join.html', {'username': user.username})


def signin(request):
    if request.method == 'POST':
        user = authenticate(username = request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            # TODO: redirect to the given url in next field of query string
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            return render(request, 'registration/login.html', {'errors': True })
    elif request.method == 'GET':
        return render(request, 'registration/login.html')

@login_required(login_url= "/accounts/signin")
def dashboard(request):
    return render(request, 'Accounting/dashboard/index.html')

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def about_us(request):
    return render(request, 'Accounting/aboutus.html', {'user': request.user})

@login_required(login_url= "/accounts/signin")
def dashboard_items(request):
    return render(request, "Accounting/dashboard/sections/items.html")

@login_required(login_url= "/accounts/signin")
def dashboard_groups(request):
    return render(request, "Accounting/dashboard/sections/groups.html")

@login_required(login_url= "/accounts/signin")
def dashboard_tags(request):
    return render(request, 'Accounting/dashboard/sections/tags.html')

@login_required(login_url= "/accounts/signin")
def dashboard_import_from_csv(request):
    return render(request, 'Accounting/dashboard/sections/import_scv.html')

@login_required(login_url= "/accounts/signin")
def dashboard_profile(request):
    return render(request, 'Accounting/dashboard/sections/profile.html', {'user': request.user})