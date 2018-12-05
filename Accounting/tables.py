import re

import django_tables2 as tables
from django.utils.html import format_html
# from django.contrib.humanize.templatetags.humanize import intcomma

from .models import Item


class ItemTable(tables.Table):
    commands = tables.Column(empty_values=(), verbose_name="عملیات")

    def render_commands(self, record):
        return format_html(f"<a href='items/{record.id}/update' class='btn btn-info btn-sm' >ویرایش</a>")

    def render_price(self, value):
        orig = str(value)
        return re.sub(r"^(-?\d+)(\d{3})", r'\g<1>,\g<2>', orig)

    class Meta:
        model = Item
        exclude = ('created', 'modified', 'user')
        per_page = 20
        template_name = 'django_tables2/bootstrap-responsive.html'
