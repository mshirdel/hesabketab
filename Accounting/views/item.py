import django_tables2 as tables
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import UpdateView, DeleteView
from django_tables2.paginators import LazyPaginator
from django.urls import reverse_lazy

from Accounting.forms import ItemForm
from Accounting.models import Group, Item
from Accounting.tables import ItemTable
from Accounting.utils import convert_string_date_to_jdate


@method_decorator(login_required(), name='dispatch')
class DashboardItemView(tables.SingleTableView):
    table_class = ItemTable
    pagination_class = LazyPaginator
    template_name = "Accounting/dashboard/sections/item_list.html"

    def get_queryset(self):
        result = Item.objects.filter(user=self.request.user).prefetch_related('group', 'tags') \
            .order_by('-date')
        if 'filter_name' in self.request.GET:
            filter_name = self.request.GET['filter_name']
            result = result.filter(name__contains=filter_name)
        if 'filter_price_from' in self.request.GET:
            filter_price_from = self.request.GET['filter_price_from']
            if filter_price_from:
                result = result.filter(price__gte = int(filter_price_from))
        if 'filter_price_to' in self.request.GET:
            filter_price_to = self.request.GET['filter_price_to']
            if filter_price_to:
                result = result.filter(price__lte = int(filter_price_to))
        if 'filter_date_from' in self.request.GET:
            filter_date_from = self.request.GET['filter_date_from']
            if filter_date_from:
                date_from = convert_string_date_to_jdate(filter_date_from)
                if date_from:
                    result = result.filter(date__gte=date_from)
        if 'filter_date_to' in self.request.GET:
            filter_date_to = self.request.GET['filter_date_to']
            if filter_date_to:
                date_to = convert_string_date_to_jdate(filter_date_to)
                if date_to:
                    result = result.filter(date__lte=date_to)
        return result


@method_decorator(login_required(), name="dispatch")
class NewItemView(View):
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
                group=form.cleaned_data["group"],
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
class ItemUpateView(UpdateView):
    model = Item
    form_class = ItemForm
    # fields = ['name', 'price', 'group', 'tags', 'item_type', 'date']
    template_name = 'Accounting/dashboard/sections/item_update.html'
    success_url = reverse_lazy("dashboard_items")


@method_decorator(login_required(), name="dispatch")
class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'Accounting/dashboard/sections/item_delete.html'
    success_url = reverse_lazy("dashboard_items")

