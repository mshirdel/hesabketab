from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.utils.html import format_html
from django.views import View
from django.db.models import Sum

import jdatetime

from Accounting.forms import ImportCSVForm
from Accounting.models import Item, Group, Tag
from Accounting.utils import get_last_12_month_period


@login_required()
def dashboard(request):
    group_summary = {}
    groups = Group.objects.filter(user=request.user)
    for group in groups:
        group_summary[group.name] = Item.objects.filter(
            user=request.user, group=group).aggregate(Sum('price'))['price__sum']

    tag_summary = {}
    tags = Tag.objects.filter(user=request.user)
    for tag in tags:
        tag_summary[tag.name] = tag.item_set.aggregate(Sum('price'))['price__sum']

    expenses = Item.objects.filter(user=request.user,
        item_type='Exp').aggregate(Sum('price'))['price__sum']
    income = Item.objects.filter(user=request.user,item_type='In').aggregate(
        Sum('price'))['price__sum']
    if not income:
        income = 0
    if not expenses:
        expenses = 0
    if expenses and income:
        balance = income - expenses
    else:
        balance = 0
    
    chart_exp_data = []
    chart_in_data = []
    month_names = []
    today = jdatetime.date.today()
    period = get_last_12_month_period(today)
    for p in period:
        month_names.append(f"{p[0].j_months_fa[p[0].month-1]} {p[0].year}")
        chart_exp_data.append(Item.objects.filter(user=request.user, item_type='Exp', date__gte=p[0],date__lte=p[1]).aggregate(Sum('price'))['price__sum'])
        chart_in_data.append(Item.objects.filter(user=request.user, item_type='In', date__gte=p[0],date__lte=p[1]).aggregate(Sum('price'))['price__sum'])
    
    chart_exp_data = [0 if value is None else value for value in chart_exp_data]
    chart_in_data = [0 if value is None else value for value in chart_in_data]

    return render(request, 'Accounting/dashboard/index.html',
                  {'income': income, 'outcome': expenses, 'balance': balance, 
                  'group_summary': group_summary, 'tag_summary': tag_summary,
                  'chart1': chart_exp_data, 'chart2': chart_in_data, 'month_names':month_names})


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
