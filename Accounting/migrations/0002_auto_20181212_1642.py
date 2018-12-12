# Generated by Django 2.1.3 on 2018-12-12 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Accounting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='date',
            field=django_jalali.db.models.jDateField(verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='item',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounting.Group', verbose_name='دسته\u200cبندی'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.CharField(choices=[('In', 'درآمد'), ('Exp', 'هزینه')], max_length=3, verbose_name='نوع'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=500, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.BigIntegerField(verbose_name='مقدار'),
        ),
    ]