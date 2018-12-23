from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.db.models import Sum

from Accounting.forms import ImportCSVForm
from Accounting.models import Item, Group, Tag


@login_required()
def dashboard(request):
    group_summary = {}
    groups = Group.objects.filter(user=request.user)
    for group in groups:
        group_summary[group.name] = Item.objects.filter(
            user=request.user, group=group).aggregate(Sum('price'))['price__sum']

    expenses = Item.objects.filter(
        item_type='Exp').aggregate(Sum('price'))['price__sum']
    income = Item.objects.filter(item_type='In').aggregate(
        Sum('price'))['price__sum']
    if not income:
        income = 0
    if not expenses:
        expenses = 0
    if expenses and income:
        balance = income - expenses
    else:
        balance = 0
    return render(request, 'Accounting/dashboard/index.html',
                  {'income': income, 'outcome': expenses, 'balance': balance, 'group_summary': group_summary})


@method_decorator(login_required(), name="dispatch")
class DashboardImportCSV(View):
    def get(self, request):
        form = ImportCSVForm()
        return render(request, 'Accounting/dashboard/sections/import_scv.html', {
            'form': form
        })

    def post(self, request):
        form = ImportCSVForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            import uuid
            file_name = str(uuid.uuid4()) + '.csv'
            with open(file_name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            try:
                from Accounting.utils import import_items
                import_items(request.user, file_name)
            except:
                return render(request, 'Accounting/dashboard/sections/import_scv.html', {
                    'form': form,
                    'errors': "",
                })
            return HttpResponseRedirect("/dashboard/items")
        else:
            return render(request, 'Accounting/dashboard/sections/import_scv.html', {
                'form': form,
                'errors': form.errors,
            })


@login_required()
def dashboard_profile(request):
    return render(request, 'Accounting/dashboard/sections/profile.html', {'user': request.user})
