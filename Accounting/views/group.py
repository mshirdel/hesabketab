from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, UpdateView
from django.views.generic import ListView
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from Accounting.models import Group
from Accounting.forms import GroupForm


@method_decorator(login_required(), name='dispatch')
class GroupListView(ListView):
    model = Group
    template_name = "Accounting/dashboard/sections/groups.html"

    def get_queryset(self):
        return Group.objects.filter(user=self.request.user)


@method_decorator(login_required(), name="dispatch")
class GroupUpdateView(UpdateView):
    model = Group
    # fields = ['name']
    form_class = GroupForm
    template_name = 'Accounting/dashboard/sections/group_update.html'
    success_url = reverse_lazy("dashboard_groups")


@method_decorator(login_required(), name="dispatch")
class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('dashboard_groups')
    template_name = 'Accounting/dashboard/sections/group_delete.html'


@method_decorator(login_required(), name="dispatch")
class GroupNewView(View):
    def get(self, request):
        form = GroupForm()
        return render(request, 'Accounting/dashboard/sections/group_new.html', {
            'form': form
        })

    def post(self, request):
        form = GroupForm(request.POST)
        if form.is_valid():
            group = Group(
                name=form.cleaned_data['name'], user=self.request.user)
            group.save()
            return HttpResponseRedirect('/dashboard/groups')
        else:
            return render(request, 'Accounting/dashboard/sections/group_new.html', {
                'form': form,
            })
