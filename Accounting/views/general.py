from django.contrib.auth.models import User
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib import messages

from Accounting.filters import ItemFilter
from Accounting.models import Item


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard'))
    else:
        return render(request, 'Accounting/index.html', {'user': request.user})


def contactus(request):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def signup(request):
    return render(request, 'registration/signup.html')


def test(request):
    return render(request, 'Accounting/test.html', {'data': 'ok'})
