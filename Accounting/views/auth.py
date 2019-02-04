from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from Accounting.forms import LoginForm


def join(request):
    user = User.objects.create_user(
        request.POST['username'], request.POST['email'], request.POST['password'])
    return render(request, 'registration/join.html', {'username': user.username})


def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        next_url = ''
        if request.GET.get('next'):
            next_url = request.GET.get('next')
        return render(request, 'registration/login_no_captcha.html',
                      {
                          'form': form,
                          'next': next_url,
                      })

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                if request.POST['next']:
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    return HttpResponseRedirect(reverse('dashboard'))
            else:
                return render(request, 'registration/login.html',
                              {
                                  'form': form,
                                  'next': request.POST['next'],
                                  'errors': form.errors,
                              })
        else:
            return render(request, 'registration/login.html',
                          {
                              'form': form,
                              'next': request.POST['next'],
                              'errors': form.errors,
                          })
