import django_filters
from django import forms

from Accounting.models import Item, Group, Tag
from Accounting.utils import convert_string_date_to_jdate


ITEM_TYPE = (
    ('In', 'درآمد'),
    ('Exp', 'هزینه')
)

class ItemFilter(django_filters.FilterSet):
    def get_groups(request):
        if request:
            return Group.objects.filter(user=request.user)
        return Group.objects.all()

    def get_tags(request):
        if request:
            return Tag.objects.filter(user=request.user)
        return Tag.objects.all()

    def date_gte_filter(queryset, name, value):
        if value:
            date_from = convert_string_date_to_jdate(value)
            if date_from:
                return queryset.filter(date__gte=date_from)

    def date_lte_filter(queryset, name, value):
        if value:
            date_from = convert_string_date_to_jdate(value)
            if date_from:
                return queryset.filter(date__lte=date_from)

    name = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm'}))
    price_gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm'}))
    price_lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm'}))
    group = django_filters.ModelChoiceFilter(queryset=get_groups, widget=forms.Select(
        attrs={'class': 'form-control form-control-sm'}))
    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=get_tags, widget=forms.SelectMultiple(attrs={'class': 'form-control form-control-sm'}))
    item_type = django_filters.ChoiceFilter(choices=ITEM_TYPE, widget=forms.Select(
        attrs={'class': 'form-control form-control-sm'}))
    date_gte = django_filters.CharFilter(method=date_gte_filter, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm datepicker'}))
    date_lte = django_filters.CharFilter(method=date_lte_filter, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm datepicker'}))

    class Meta:
        model = Item
        fields = ['name']
