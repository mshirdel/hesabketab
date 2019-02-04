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


class GroupForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'})
    )

    class Meta:
        model = Group
        fields = ['name']


class ItemForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    price = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    date = jforms.jDateField(widget=jforms.widgets.jDateInput(
        attrs={'class': 'form-control datepicker'}))
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    item_type = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control'}), choices=Item.ITEM_TYPE)

    def __init__(self, current_user=None, * args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        if current_user:
            self.fields['group'].queryset = Group.objects.filter(
                user=current_user)
            self.fields['tags'].queryset = Tag.objects.filter(
                user=current_user)

    class Meta:
        model = Item
        fields = ['name', 'price', 'date', 'group', 'tags', 'item_type']


class ImportCSVForm(forms.Form):
    file = forms.FileField()
