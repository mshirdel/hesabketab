from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    return render(request, 'Accounting/index.html')


def signup(request):
    # username = request.POST['username']
    # email = request.POST['email']
    # password = request.POST['password']
    # data = {username: username, email: email, password: password}
    return render(request, 'registration/join.html', { 'username': 'mshirdel' })
