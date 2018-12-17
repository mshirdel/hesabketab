import django_tables2 as tables
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import UpdateView
from django_tables2.paginators import LazyPaginator

from Accounting.forms import ItemForm
from Accounting.models import Group, Item
from Accounting.tables import ItemTable


@method_decorator(login_required(), name='dispatch')
class DashboardItemView(tables.SingleTableView):
    table_class = ItemTable
    pagination_class = LazyPaginator
    template_name = "Accounting/dashboard/sections/item_list.html"

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user).prefetch_related('group', 'tags') \
            .order_by('-date')
            #.exclude('tags', 'tags').only('id', 'name', 'date', 'price', 'group', '')


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
    # form_class = ItemForm
    fields = ['name', 'price', 'group', 'tags', 'item_type', 'date']
    template_name = 'Accounting/dashboard/sections/item_update.html'
    success_url = '/dashboard/items'
