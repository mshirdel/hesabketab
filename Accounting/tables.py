import re

import django_tables2 as tables
from django.utils.html import format_html

from .models import Item


class ItemTable(tables.Table):
    tags = tables.Column(empty_values=(), verbose_name="تگ‌ها")
    commands = tables.Column(empty_values=(), verbose_name="عملیات")

    def render_commands(self, record):
        return format_html(f"<a href='items/{record.id}/update' class='btn btn-primary btn-sm' >ویرایش</a>&nbsp<a href='items/{record.id}/delete' class='btn btn-danger btn-sm' >حذف</a>")

    def render_price(self, value):
        orig = str(value)
        return re.sub(r"^(-?\d+)(\d{3})", r'\g<1>,\g<2>', orig)

    def render_tags(self, record):
        tags = [f'<span class="badge badge-pill badge-info">{tag.name}</span>' for tag in record.tags.all()]
        return format_html(' '.join(tags))

    class Meta:
        model = Item
        exclude = ('created', 'modified', 'user', 'id')
        per_page = 15
        template_name = 'django_tables2/bootstrap-responsive.html'
