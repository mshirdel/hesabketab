from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.views import View
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError

from .models import Item, Group, Tag


def test(request):
    return HttpResponse("ok")


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard'))
    else:
        return render(request, 'Accounting/index.html', {'user': request.user})


def join(request):
    user = User.objects.create_user(
        request.POST['username'], request.POST['email'], request.POST['password'])
    return render(request, 'registration/join.html', {'username': user.username})


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


@login_required()
def dashboard(request):
    return render(request, 'Accounting/dashboard/index.html')


def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def about_us(request):
    return render(request, 'Accounting/aboutus.html', {'user': request.user})


@method_decorator(login_required(), name='dispatch')
class DashboardItemView(ListView):
    model = Item
    template_name = "Accounting/dashboard/sections/item_list.html"


@login_required()
def dashboard_groups(request):
    return render(request, "Accounting/dashboard/sections/groups.html")


@login_required()
def dashboard_tags(request):
    return render(request, 'Accounting/dashboard/sections/tags.html')


@login_required()
def dashboard_import_from_csv(request):
    return render(request, 'Accounting/dashboard/sections/import_scv.html')


@login_required()
def dashboard_profile(request):
    return render(request, 'Accounting/dashboard/sections/profile.html', {'user': request.user})


class DashboardItemNewView(View):
    def get(self, request):
        groups = Group.objects.all()
        tags = Tag.objects.all()
        return render(request, 'Accounting/dashboard/sections/item_new.html', {
            'groups': groups,
            'item_types': dict(Item.ITEM_TYPE),
            'tags': tags
        })

    def post(self, request):
        try:
            item = Item(
                name=request.POST["name"],
                price=request.POST["price"],
                date=request.POST["date"],
                item_type=request.POST["item_type"],
                group=Group.objects.get(id=request.POST["group"]),
                user=request.user
            )
            item.full_clean()
            item.save()
            for tagid in request.POST.getlist("item_tag"):
                tag = Tag.objects.get(id=tagid)
                item.tags.add(tag)
        except ValidationError as error:
            groups = Group.objects.all()
            tags = Tag.objects.all()
            print("***************")
            print(error.message_dict)
            return render(request, 'Accounting/dashboard/sections/item_new.html', {'errors': error.message_dict, 'groups': groups,
                                                                                   'item_types': dict(Item.ITEM_TYPE),
                                                                                   'tags': tags})

        return HttpResponseRedirect('/dashboard/items')
