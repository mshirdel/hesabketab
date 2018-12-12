from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View


def join(request):
    user = User.objects.create_user(
        request.POST['username'], request.POST['email'], request.POST['password'])
    return render(request, 'registration/join.html', {'username': user.username})


def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


class SignIn(View):
    def post(self, request):
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            if request.POST['next']:
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('dashboard'))
        else:
            return render(request, 'registration/login.html', {'errors': True})

    def get(self, request):
        data = {}
        if request.GET.get('next'):
            data['next'] = request.GET.get('next')
        return render(request, 'registration/login.html', data)
