import django_tables2 as tables
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import UpdateView, DeleteView
from django_tables2.paginators import LazyPaginator
import django_tables2
from django.urls import reverse_lazy

from Accounting.forms import ItemForm
from Accounting.models import Group, Item
from Accounting.tables import ItemTable
from Accounting.utils import convert_string_date_to_jdate
from Accounting.filters import ItemFilter


class FilteredSingleTableView(django_tables2.SingleTableView):
    filter_class = None

    def get_table_data(self):
        data = super(FilteredSingleTableView, self).get_table_data()
        self.filter = self.filter_class(self.request.GET, queryset=data, request=self.request)
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(FilteredSingleTableView,
                        self).get_context_data(**kwargs)
        context['filter'] = self.filter
        return context

    def get_queryset(self):
        result = Item.objects.filter(user=self.request.user).prefetch_related('group', 'tags') \
            .order_by('-date')
        return result


@method_decorator(login_required(), name='dispatch')
class ItemFilteredSingleTableView(FilteredSingleTableView):
    model = Item
    table_class = ItemTable
    filter_class = ItemFilter
    template_name = "Accounting/dashboard/sections/item_list.html"


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
            if '_save' in request.POST:
                return HttpResponseRedirect('/dashboard/items')
            elif '_addanother' in request.POST:
                return HttpResponseRedirect('/dashboard/items/new')
            elif '_continue' in request.POST:
                pass
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
