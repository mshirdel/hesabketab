from django.contrib import admin
from .models import Item, Group, Tag, UserProfile
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin

class ItemAdmin(admin.ModelAdmin):
    list_filter = (
        ('date', JDateFieldListFilter),
    )

admin.site.register(Item, ItemAdmin)
admin.site.register(Group)
admin.site.register(Tag)