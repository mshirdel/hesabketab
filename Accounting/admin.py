from django.contrib import admin
from .models import Item, Group, Tag, UserProfile

admin.site.register(Item)
admin.site.register(Group)
admin.site.register(Tag)