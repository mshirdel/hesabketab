from django import forms
from django.utils.translation import gettext_lazy as _

from django_jalali import forms as jforms

from Accounting.models import Group, Item, Tag


class TagForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Tag
        fields = ['name']


class GroupForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'})
    )


class ItemForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    price = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
    date = jforms.jDateField(widget=jforms.widgets.jDateInput(attrs={'class': 'form-control datepicker'}))
    group = forms.ModelChoiceField(queryset=Group.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-control'}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(
    ), widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    item_type = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control'}), choices=Item.ITEM_TYPE)


class ImportCSVForm(forms.Form):
    file = forms.FileField()
