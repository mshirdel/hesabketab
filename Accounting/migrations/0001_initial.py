# Generated by Django 2.0.1 on 2018-03-03 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('price', models.BigIntegerField()),
                ('date', models.DateTimeField()),
                ('item_type', models.CharField(choices=[('In', 'Income'), ('Exp', 'Expense')], max_length=3)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounting.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(to='Accounting.Tag'),
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]