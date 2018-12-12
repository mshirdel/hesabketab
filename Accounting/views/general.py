from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, reverse


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard'))
    else:
        return render(request, 'Accounting/index.html', {'user': request.user})


def contactus(request):
    return HttpResponseNotFound('<h1>Page not found</h1>')
