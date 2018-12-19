import django_filters

from Accounting.models import Item


class ItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Item
        fields = ['name', 'price']
