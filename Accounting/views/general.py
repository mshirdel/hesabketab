from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, reverse

from django.contrib.auth.models import User
from Accounting.models import Item
from Accounting.filters import ItemFilter


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard'))
    else:
        return render(request, 'Accounting/index.html', {'user': request.user})


def contactus(request):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def test(request):
    user = User.objects.get(pk=1)
    items = Item.objects.filter(user=user).prefetch_related('group', 'tags') \
            .order_by('-date')
    item_filter = ItemFilter({}, queryset = items)
    # import pdb
    # pdb.set_trace()
    return render(request, 'Accounting/test.html', {'filter': item_filter})


def demo(request):
    return render(request, 'Accounting/demo.html')