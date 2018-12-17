from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from django_jalali.db import models as jmodels


class TimeStampedModel(models.Model):
    objects = jmodels.jManager()
    created = jmodels.jDateTimeField(auto_now_add=True)
    modified = jmodels.jDateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Group(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "گروه"
        verbose_name_plural = "گروه‌ها"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dashboard_groups_update', kwargs={'pk': self.pk})


class Tag(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "تگ"
        verbose_name_plural = "تگ‌ها"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dashboard_tag_update', kwargs={'pk': self.pk})


class Item(TimeStampedModel):
    ITEM_TYPE = (
        ('In', 'درآمد'),
        ('Exp', 'هزینه')
    )

    name = models.CharField(max_length=500, verbose_name="نام")
    price = models.BigIntegerField(verbose_name="مقدار")
    date = jmodels.jDateField(verbose_name="تاریخ")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, verbose_name="دسته‌بندی")
    tags = models.ManyToManyField(Tag)
    item_type = models.CharField(
        max_length=3, choices=ITEM_TYPE, verbose_name="نوع")

    class Meta:
        verbose_name = "دخل و خرج"
        verbose_name_plural = "دخل و خرج"
        indexes = [
            models.Index(fields=['name', 'date'])
        ]

    def __str__(self):
        return f"{self.name} - {self.price}"


class UserProfile(User):
    cell_phone = models.CharField(max_length=15, blank=True)
    avatar_url = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=1000, blank=True)
