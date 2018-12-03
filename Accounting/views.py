from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView

from .forms import GroupForm, ItemForm, TagForm
from .models import Group, Item, Tag


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


@method_decorator(login_required(), name='dispatch')
class DashboardItemView(ListView):
    model = Item
    template_name = "Accounting/dashboard/sections/item_list.html"


@method_decorator(login_required(), name='dispatch')
class DashboardGroupView(ListView):
    model = Group
    template_name = "Accounting/dashboard/sections/groups.html"


@method_decorator(login_required(), name="dispatch")
class DashboardTagView(ListView):
    model = Tag
    template_name = "Accounting/dashboard/sections/tags.html"


@login_required()
def dashboard_import_from_csv(request):
    return render(request, 'Accounting/dashboard/sections/import_scv.html')


@login_required()
def dashboard_profile(request):
    return render(request, 'Accounting/dashboard/sections/profile.html', {'user': request.user})


@method_decorator(login_required(), name="dispatch")
class DashboardGroupNewView(View):
    def get(self, request):
        form = GroupForm()
        return render(request, 'Accounting/dashboard/sections/group_new.html', {
            'form': form
        })

    def post(self, request):
        form = GroupForm(request.POST)
        if form.is_valid():
            group = Group(name=form.cleaned_data['name'])
            group.save()
            return HttpResponseRedirect('/dashboard/groups')
        else:
            return render(request, 'Accounting/dashboard/sections/group_new.html', {
                'form': form,
            })


@method_decorator(login_required(), name="dispatch")
class DashboardItemNewView(View):
    def get(self, request):
        form = ItemForm()
        return render(request, 'Accounting/dashboard/sections/item_new.html', {
            'form': form,
        })

    def post(self, request):
        form = ItemForm(request.POST)
        if form.is_valid():
            item = Item(
                name=form.cleaned_data["name"],
                price=form.cleaned_data["price"],
                date=form.cleaned_data["date"],
                item_type=form.cleaned_data["item_type"],
                # group=Group.objects.get(id=request.POST["group"]),
                group=Group.objects.get(name=form.cleaned_data["group"]),
                user=request.user
            )
            item.save()
            for tag in form.cleaned_data["tags"]:
                item.tags.add(tag)
            return HttpResponseRedirect('/dashboard/items')
        else:
            return render(request, 'Accounting/dashboard/sections/item_new.html', {
                'form': form,
                'errors': form.errors,
            })


@method_decorator(login_required(), name="dispatch")
class DashboardTagNewView(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'Accounting/dashboard/sections/tag_new.html', {'form': form})

    def post(self, request):
        form = TagForm(request.POST)
        if form.is_valid():
            tag = Tag(name=form.cleaned_data['name'])
            tag.save()
            return HttpResponseRedirect('/dashboard/tags')
        else:
            return render(request, 'Accounting/dashboard/sections/tag_new.html', {'form': form})


@method_decorator(login_required(), name="dispatch")
class DashboardGroupUpdateVew(View):
    def get(self, request, id):
        group = get_object_or_404(Group, pk=id)
        form = GroupForm({'name': group.name})
        return render(request, 'Accounting/dashboard/sections/group_update.html', {'form': form})

    def post(self, request):
        form = GroupForm(request.POST)
        if form.is_valid():
            return render(request, 'Accounting/dashboard/sections/group_update.html', {'form': form})
        else:
            return render(request, 'Accounting/dashboard/sections/group_update.html', {'form': form})


@method_decorator(login_required(), name="dispatch")
class GroupUpdateView(UpdateView):
    model = Group
    fields = ['name']
    # form_class = GroupForm
    template_name = 'Accounting/dashboard/sections/group_update.html'


@method_decorator(login_required(), name="dispatch")
class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('dashboard_groups')
    template_name = 'Accounting/dashboard/sections/group_delete.html'
