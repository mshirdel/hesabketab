import django_tables2 as tables
from django.utils.html import format_html

from .models import Item


class ItemTable(tables.Table):
    commands = tables.Column(empty_values=(), verbose_name="عملیات")

    def render_commands(self, record):
        return format_html(f"<a href='items/{record.id}/update' class='btn btn-info btn-sm' >ویرایش</a>")

    class Meta:
        model = Item
        exclude = ('created', 'modified', 'user')
        # order_by = 'price'

        template_name = 'django_tables2/bootstrap-responsive.html'
