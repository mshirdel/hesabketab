from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    ITEM_TYPE = (
        ('In', 'درآمد'),
        ('Exp', 'هزینه')
    )
    
    name = models.CharField(max_length=500)
    price = models.BigIntegerField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    item_type = models.CharField(max_length=3, choices=ITEM_TYPE)

    def __str__(self):
        return f"{self.name} - {self.price}"
