import django_tables2 as tables
from django.utils.html import format_html
from django.contrib.humanize.templatetags.humanize import intcomma

from .models import Item


class ItemTable(tables.Table):
    def price_sum(table):
        income = f"جمع درآمد:‌ {intcomma(sum([row.price for row in table.data if row.item_type == 'In']), False)} تومان"
        expense = f"جمع هزینه:‌ {intcomma(sum([row.price for row in table.data if row.item_type == 'Exp']), False)} تومان"
        return format_html(f"<div class='theme-color'>{income} <br/> {expense}</div>")

    tags = tables.Column(empty_values=(), verbose_name="تگ‌ها")
    commands = tables.Column(empty_values=(), verbose_name="عملیات")
    price = tables.Column(footer=price_sum)

    def render_commands(self, record):
        return format_html(f"<a href='items/update/{record.id}' class='btn btn-primary btn-sm' >ویرایش</a>&nbsp<a href='items/delete/{record.id}' class='btn btn-danger btn-sm' >حذف</a>")

    # def render_price(self, value):
    #     return intcomma(value)

    def render_tags(self, record):
        tags = [
            f'<span class="badge badge-pill badge-info">{tag.name}</span>' for tag in record.tags.all()]
        return format_html(' '.join(tags))

    class Meta:
        model = Item
        exclude = ('created', 'modified', 'user', 'id')
        per_page = 15
        template_name = 'django_tables2/bootstrap-responsive.html'
