# Generated by Django 2.1.3 on 2018-12-03 09:05

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'گروه',
                'verbose_name_plural': 'گروه\u200cها',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('modified', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=500)),
                ('price', models.BigIntegerField()),
                ('date', django_jalali.db.models.jDateField()),
                ('item_type', models.CharField(choices=[('In', 'درآمد'), ('Exp', 'هزینه')], max_length=3)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounting.Group')),
            ],
            options={
                'verbose_name': 'دخل و خرج',
                'verbose_name_plural': 'دخل و خرج',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'تگ',
                'verbose_name_plural': 'تگ\u200cها',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cell_phone', models.CharField(blank=True, max_length=15)),
                ('avatar_url', models.CharField(blank=True, max_length=500)),
                ('address', models.CharField(blank=True, max_length=1000)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
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
